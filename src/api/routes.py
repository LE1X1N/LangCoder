from flask import Blueprint, request, jsonify
import random
import time
from multiprocessing import Process, Manager, Lock, Queue
from concurrent.futures import ThreadPoolExecutor
import logging
import uuid

from config import conf, SYSTEM_PROMPT
from src.llm import build_prompt, call_chat_completion , history_to_messages, messages_to_history
from src.llm import History, Messages
from src.browser.manager import init_driver, capture_screenshot
from src.browser.renderer import launch_sandbox_demo
from src.util import get_random_available_port, wait_for_port

logger = logging.getLogger(conf["service_name"])
api_bp = Blueprint('v1', __name__)
max_workers = 5    # number of threads to request LLM
max_turn = 3


# read jsx template
with open('tmpls/小程序模板.jsx', 'r', encoding='utf-8') as f:
    tmpl0 = f.read()

# read jsx template
with open('tmpls/网页模板-管理系统（上下）.jsx', 'r', encoding='utf-8') as f:
    tmpl1 = f.read()
    
# read jsx template
with open('tmpls/网页模板-管理系统（左右）.jsx', 'r', encoding='utf-8') as f:
    tmpl2 = f.read()
    
tmpls = [tmpl0, tmpl1, tmpl2]

def parseJSON(data, request_id=None):
    # 1. parse input JSON to pages
    pages = []
    for mid, module in enumerate(data["web_pages"]):
        for pid, page in enumerate(module['page']):
            pages.append(
                {
                    "request_id" : request_id,
                    "page_id" : f'{mid}_{pid}',
                    "web_title": data["title"], 
                    "web_detail": data["page_detail"] ,
                    "module_name": module["page_name"],
                    "page_name": page["name"],
                    "page_desc": page["text"],
                    "page_tmpl": tmpls[int(module["style"])],
                }
            )
    return pages
    


def task_thread(task):
    start_time = time.time()    
    request_id = task["request_id"]
    task_id = task["page_id"]
    
    logger.info(f"Request ID: {request_id} -> Task_{task_id}: ********* 任务 {task_id} 开始！*********")
    
    # 1. assemble prompt
    query = build_prompt(task)
                
    # 2. create messages
    messages = [{"role": 'system', "content": SYSTEM_PROMPT}]
    messages.append({"role": "user", "content": query})
    
    # Multi-turn generation
    render_success = False
    for turn in range(max_turn):
        logger.info(f"Request ID: {request_id} -> Task_{task_id}: 进行第 {turn+1} 轮尝试...")
    
        # 3. code generation
        code = call_chat_completion(messages)
        messages.append({"role": "assistant", "content": code})
        logger.info(f"Request ID: {request_id} -> Task_{task_id}: 代码生成成功！耗时：{time.time() - start_time} s")
        
        port = get_random_available_port()       # a random port to bind with gradio
        logger.info(f"Request ID: {request_id} ->, Task ID: {task_id}, Gradio Port: {port}")
        
        browser_registry = Queue()               #  communication between main process and browser process
        browser_lock = Lock()
        
        
        try:
            # 4. Launch brower to render react  
            browser = Process(target=launch_sandbox_demo, 
                            args=(request_id, task_id, code, port, browser_registry, browser_lock))
            browser.start()
            
            # wait port connected (15s)
            if not wait_for_port(port, timeout=15): 
                raise ConnectionRefusedError("Gradio端口连接失败")
            logger.info(f"Request ID: {request_id} -> Task_{task_id}: Gradio 初始化成功！")
        
            # 5. Try screenshot
            driver = init_driver()
            driver.get(f'http://localhost:{port}')
            logger.info(f"Request ID: {request_id} -> Task_{task_id}: Chrome driver 初始化成功！")
            
            # wait rendering (25s)
            for _ in range(25):
                with browser_lock:
                    logger.info(f"Request ID: {request_id} -> Task_{task_id}: 检查渲染状态...")
                    
                    if not browser_registry.empty():
                        
                        completed_flag = browser_registry.get()
                        
                        if completed_flag != task_id:
                            # render / compile error
                            render_success = False
                            raise ValueError(completed_flag)
                        
                        if completed_flag == task_id:
                            # compile success
                            
                            wait_rounds = 0
                            while wait_rounds < 3:
                                logger.info(f"Request ID: {request_id} -> Task_{task_id}: 编译成功，等待渲染成功信号...")
                                if not browser_registry.empty():
                                    new_flag = browser_registry.get()
                                    if new_flag != task_id:
                                        raise ValueError(new_flag)
                                wait_rounds += 1
                                time.sleep(1) 
                                
                                
                            logger.info(f"Request ID: {request_id} -> Task_{task_id}: 渲染成功，启动Selenium捕捉...")
                            capture_screenshot(request_id, task_id, driver)
                            render_success = True
                            break
                time.sleep(1)
            
            if not render_success:
                raise TimeoutError("Gradio渲染超时！")
        
        except ValueError as e:
            logger.error(f"Request ID: {request_id} -> Task_{task_id}: 【前端错误】{e}")
            messages.append({"role": "user", "content": str(e)})
        except TimeoutError as e:
            logger.error(f"Request ID: {request_id} -> Task_{task_id}: 【渲染超时错误】{e}")
            messages.pop()      # exclude assistanct generated code
        except ConnectionRefusedError as e:
            logger.error(f"Request ID: {request_id} -> Task_{task_id}: 【端口连接错误】{e}")
            messages.pop()      # exclude assistanct generated code
        except Exception as e:
            logger.error(f"Request ID: {request_id} -> Task_{task_id}: 【其他错误】{e}")
            messages.pop()   
        finally:
            browser.kill()
            logger.info(f"Request ID: {request_id} -> Task_{task_id}: Gradio浏览器 退出! 错误码: {browser.exitcode}")
              
            if driver:
                driver.close() 
                driver.quit()   
                logger.info(f"Request ID: {request_id} -> Task_{task_id}: Chrome Driver 退出!")

        # exit judge
        if render_success:
            logger.info(f"Request ID: {request_id} -> Task_{task_id}: 第 {turn+1} 轮成功！")
            return {"task_id": task_id, "status": render_success}
        else:
            logger.info(f"Request ID: {request_id} -> Task_{task_id}: 第 {turn+1} 轮失败！")
    
    return {"task_id": task_id, "status": render_success, "msg": "失败重试超过最大测试轮次！"}




@api_bp.route('/gen_images', methods=['POST'])
def gen_images():
    """
        MainThread(输入JSON -> 数据解析) -> Thread(Prompt构建 -> 代码生成 -> 截屏渲染 -> 输出图片) -> MainThread(结果保存)
    """
    start_time = time.time()
    request_id = str(uuid.uuid4())
    logger.info(f"Request ID: {request_id} ->: 开始处理请求")
    
    # 1. Parse JSON into multiple tasks
    data = request.get_json()   
    tasks = parseJSON(data, request_id)
    
    # 2. Multi-thread rendering
    executor = ThreadPoolExecutor(max_workers=max_workers)
    futures = executor.map(task_thread, tasks)
    results = []
    for cur_result in futures:
        results.append(cur_result)
    
    # TODO 3. check status

    logger.info(f"Request ID: {request_id} -> 请求完成，耗时 {time.time() - start_time} s")
    return jsonify({"request_id" : request_id, "response": results})



@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "picture_processor"})


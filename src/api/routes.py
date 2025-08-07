from flask import Blueprint, request, jsonify
import random
import time
from multiprocessing import Process, Manager, Lock, Queue
from concurrent.futures import ThreadPoolExecutor
import logging
import uuid

from config import conf, SYSTEM_PROMPT
from src.llm import build_prompt, call_chat_completion , history_to_messages
from src.llm import History, Messages
from src.browser.manager import init_driver, capture_screenshot
from src.browser.renderer import launch_sandbox_demo
from src.util import get_random_available_port, wait_for_port

logger = logging.getLogger(conf["service_name"])
api_bp = Blueprint('v1', __name__)
max_workers = 5    # number of threads to request LLM


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
    history = []    # chat history
    request_id = task["request_id"]
    task_id = task["page_id"]
    
    # 1. assemble prompt
    query = build_prompt(task)
    
    # 2. create messages
    messages = history_to_messages(history, system=SYSTEM_PROMPT)
    messages.append({"role": "user", "content": query})
    
    # 3. code generation
    code = call_chat_completion(messages)
    
    logger.info(f"Request ID: {request_id} -> Task_{task_id}: 代码生成成功！耗时：{time.time() - start_time} s")
    
    port = get_random_available_port()      # a random port to bind with gradio
    browser_registry = Queue() #  communication between main process and browser process
    browser_lock = Lock()
        
    logger.info(f"Request ID: {request_id} ->, Task ID: {task_id}, Gradio Port: {port}")
        
    # 2. Launch brower to render react  
    browser = Process(target=launch_sandbox_demo, 
                    args=(request_id, task_id, code, port, browser_registry, browser_lock))
    browser.start()
    
    if not wait_for_port(port, timeout=15): 
        browser.kill()      # wait the port is ready
        return jsonify({"status": "error", "message": f"Error: Gradio launch failed at port {port}!"})
    
    try:
        # Try screenshot
        driver = init_driver()
        driver.get(f'http://localhost:{port}')
        # driver.get("http://www.baidu.com")
        
        # wait rendering
        render_success = False
        for _ in range(100):
            with browser_lock:
                logger.info(f"Request ID: {request_id} -> Task_{task_id}: 检查渲染状态...")
                if not browser_registry.empty():
                    completed_task_id = browser_registry.get()
                    if completed_task_id == task_id:
                        logger.info(f"Request ID: {request_id} -> Task_{task_id}: 渲染成功，启动Selenium捕捉...")
                        time.sleep(3)   # wait animation
                        capture_screenshot(request_id, task_id, driver)
                        render_success = True
                        break
            time.sleep(1)
        
        if render_success is False:
            raise TimeoutError("Browser rendering timeout!")
    
    except Exception as e:
        return {"task ID": task_id, "status": False, "error": e}
        
    finally:
        browser.kill()
        logger.info(f"Request ID: {request_id} -> Task_{task_id}: Gradio浏览器 退出!")
        
        driver.close() 
        driver.quit()   
        logger.info(f"Request ID: {request_id} -> Task_{task_id}: Chrome Driver 退出!")
    return {"task_id": task_id, "status": True}



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


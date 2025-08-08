from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process, Manager, Lock, Queue
import logging
import time


from config import conf, SYSTEM_PROMPT
from src.core.parser import DataParser
from src.llm import build_prompt, call_chat_completion 
from src.browser.manager import init_driver, capture_screenshot
from src.browser.renderer import launch_sandbox_demo
from src.utils import get_random_available_port, wait_for_port, get_logger
from src.tmpl import TemplateManager


logger = get_logger()

class FrontendError(Exception):
    # frontend render/compile error
    pass  

class TaskManager:
    def __init__(self):
        self.parser = DataParser(tmpl_manager=TemplateManager())
        self.executor = ThreadPoolExecutor(conf["max_workers"])
        
    
    def process_tasks(self, data: dict, request_id: str) -> list:        
        """
            Multi-thread processing tasks
            
            MainThread(输入JSON -> 数据解析) -> Thread(Prompt构建 -> 代码生成 -> 截屏渲染 -> 输出图片) -> MainThread(结果保存)
        """
        tasks = self.parser.parse(data, request_id)
        futures = [self.executor.submit(self._process_single_task, task) for task in tasks]
        return [future.result() for future in futures]
        
        
    def _process_single_task(self, task: dict) -> dict:

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
        for turn in range(conf["max_retries"]):
            logger.info(f"Request ID: {request_id} -> Task_{task_id}: 进行第 {turn+1} 轮尝试...")
        
            # 3. code generation
            start_time = time.time()
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
                if not wait_for_port(port, timeout=conf["connect_timeout"]): 
                    raise ConnectionRefusedError("Gradio端口连接失败")
                logger.info(f"Request ID: {request_id} -> Task_{task_id}: Gradio 初始化成功！")
            
                # 5. Try screenshot
                driver = init_driver()
                driver.get(f'http://localhost:{port}')
                logger.info(f"Request ID: {request_id} -> Task_{task_id}: Chrome driver 初始化成功！")
                
                # wait rendering 
                for _ in range(conf["render_timeout"]):
                    with browser_lock:
                        logger.info(f"Request ID: {request_id} -> Task_{task_id}: 检查渲染状态...")
                        
                        if not browser_registry.empty():
                            
                            completed_flag = browser_registry.get()
                            
                            if completed_flag != task_id:
                                # render / compile error
                                render_success = False
                                raise FrontendError(completed_flag)
                            
                            if completed_flag == task_id:
                                # compile success
                                
                                wait_rounds = 0
                                while wait_rounds < 3:
                                    logger.info(f"Request ID: {request_id} -> Task_{task_id}: 编译成功，等待渲染成功信号...")
                                    if not browser_registry.empty():
                                        new_flag = browser_registry.get()
                                        if new_flag != task_id:
                                            raise FrontendError(new_flag)
                                    wait_rounds += 1
                                    time.sleep(1) 
                                    
                                logger.info(f"Request ID: {request_id} -> Task_{task_id}: 渲染成功，启动Selenium捕捉...")
                                capture_screenshot(request_id, task_id, driver)
                                render_success = True
                                break
                    time.sleep(1)
                
                if not render_success:
                    raise TimeoutError("Gradio渲染超时！")
            
            except FrontendError as e:
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
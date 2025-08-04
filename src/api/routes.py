from flask import Blueprint, request, jsonify
import random
import time
from multiprocessing import Process, Manager, Lock, Queue


from src.llm import build_prompt, call_chat_completion
from src.browser.manager import init_driver, capture_screenshot
from src.browser.renderer import launch_sandbox_demo
from src.util import get_random_available_port, wait_for_port

api_bp = Blueprint('v1', __name__)


@api_bp.route('/gen_images', methods=['POST'])
def gen_images():
    # 1. get the parameters
    data = request.get_json()
    
    title = data["title"]               # paper title
    page_detail = data["page_detail"]   # web description
    web_pages = data["web_pages"]       # modules 
    
    # 2. generate corresponding prompt
    modules = []
    for page in web_pages:
        # split into different JSON
        module_json = {
            "title" : title, 
            "page_detail" : page_detail,
            **page
        }
        modules.append(module_json)
    
    module_prompts = [build_prompt(module) for module in modules]
    
    # 3. Call LLM to generate code
    # gen_code = []
    # for prompt in module_prompts:
    #     gen_code.append([call_chat_completion(p) for p in prompt])
    
    print("Starting generate code...")
    start_time = time.time()
    gen_code = call_chat_completion(prompt=module_prompts[0][0])
    print(f"Code generation finished! {time.time() - start_time} s")
    
    # 4. Init task id and browser port
    task_id = random.randint(1000, 9999)    
    port = get_random_available_port()      # a random port to bind with gradio
    elem_id = "sandbox-iframe"              # sandbox ID in HTML
            
    browser_registry = Queue()  #  communication between main process and browser process
    browser_lock = Lock()
        
    print(f"Task ID: {task_id}")
    print(f"Gradio Port: {port}")
        
    #5. Start the browser in a new process    
    browser = Process(target=launch_sandbox_demo, 
                    args=(gen_code, task_id, port, elem_id, browser_registry, browser_lock))
    browser.start()
    
    if not wait_for_port(port, timeout=15): 
        browser.kill()  # wait the port is ready
        return jsonify({"status": "error", "message": f"Error: Gradio launch failed at port {port}!"})
    
    try:
        # 7. Try screenshot
        driver = init_driver()
        driver.get(f'http://localhost:{port}')
        # driver.get("http://www.baidu.com")
        
        render_success = False
        # wait rendering
        for _ in range(100):
            with browser_lock:
                print(f"检查渲染状态...")
                if not browser_registry.empty():
                    completed_task_id = browser_registry.get()
                    if completed_task_id == task_id:
                        print(f"Task_{task_id} 渲染成功，启动Selenium捕捉...")
                        capture_screenshot(task_id, driver)
                        render_success = True
                        break
            time.sleep(1)
        
        if render_success is False:
            raise TimeoutError("Browser rendering timeout!")
    
    except Exception as e:
        return jsonify({"status": "error", "message" : f"Error: {e}"})
        
    finally:
        
        browser.kill()
        print("Gradio浏览器 退出!")
        
        driver.close() 
        driver.quit()   
        print("Chrome Driver 退出!")
    return jsonify({"status": "success", "message" : f"Task ID: {task_id}"})



@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "picture_processor"})


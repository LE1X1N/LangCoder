from flask import Blueprint, request, jsonify
import random

from llm import build_prompt, call_chat_completion
from browser.manager import init_driver, driver_registry, driver_lock
from browser.renderer import create_sandbox_demo
import multiprocessing

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


api_bp = Blueprint('v1', __name__)

@api_bp.route('/gen_images', methods=['POST'])
def gen_images():
    
    # 1. get the parameters
    data = request.get_json()
    
    title = data["title"]
    page_detail = data["page_detail"]
    web_pages = data["web_pages"]
    
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
    
    # build prompts for each module
    module_prompts = [build_prompt(module) for module in modules]
    
    # 3. Call LLM to generate code
    # gen_code = []
    # for prompt in module_prompts:
    #     gen_code.append([call_chat_completion(p) for p in prompt])
    gen_code = call_chat_completion(prompt=module_prompts[0][0])
    
    # 4. Init task id and browser port
    task_id = random.randint(1000, 9999)
    port = 7860
    elem_id = "sandbox-iframe" # sandbox ID in HTML
    
    # 5. Init chrome driver
    driver = init_driver()
    with driver_lock:
        driver_registry[task_id] = driver
    
    # 6. Start the browser in a new process
    browser_process = multiprocessing.Process(target=create_sandbox_demo, args=(gen_code, task_id, port, elem_id))
    browser_process.start()
    
    # 7. Try screenshot
    try:
        driver.get(f'http://localhost:{port}')
        WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, elem_id))
            )
    except Exception as e:
        print(f"Task_{task_id}: 截屏失败 - {str(e)}")
    finally:
        browser_process.kill()
        driver = driver_registry.pop(task_id)
        driver.quit()
    
    return jsonify({"status": "success"})



@api_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "service": "picture_processor"})


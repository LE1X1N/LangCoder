from flask import Blueprint, request, jsonify
import yaml
import requests
from openai import OpenAI

api_bp = Blueprint('v1', __name__)

with open("config/system_conf.yaml", "r") as f:
    conf = yaml.safe_load(f)

client = OpenAI(
    base_url=conf["base_url"],  
    api_key=conf["api_key"] 
)

def build_prompt(module):
    """
        transform JSON to prompt
    """
    title = module["title"]
    page_detail = module["page_detail"]
    page_name = module["page_name"]
    style = module["style"]
    
    # TODO convert style to corresponding template
    
    pages = module["page"]
    
    # convert to prompt
    prompts = []
    for page in pages:
        prompts.append(f"""
            任务：设计【{title}】的静态页面。
            项目背景：{page_detail}
            当前渲染模块：【{page_name}】
            当前渲染页面：【{page["name"]}】
            渲染需求：{page["text"]} (仅展示UI，无需交互)
        """)
    return prompts


def call_chat_completion(prompt):
    """
        Call LLM to generate code
    """
    try:
        # openai compatible
        response = client.chat.completions.create(
                model=conf["model"],  
                messages=[
                        {"role": "system", "content": f"{conf["system_prompt"]}"},
                        {"role": "user", "content": prompt}
                    ],
                stream=False
            )
        res = response.choices[0].message.content
        return res
    
    except Exception as e:
        raise Exception(f"处理响应失败: {str(e)}")



@api_bp.route('/gen_images', methods=['POST'])
def gen_images():
    data = request.get_json()
    
    title = data["title"]
    page_detail = data["page_detail"]
    web_pages = data["web_pages"]
    
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
    
    # call Coder LLM
    gen_code = []
    for prompt in module_prompts:
        gen_code.append([call_chat_completion(p) for p in prompt])
    
    # rendering
    
    
    
    return jsonify({"status": "success", "data": gen_code})




@api_bp.route('/health', methods=['GET'])
def health_check():
    print(1)
    return jsonify({"status": "healthy", "service": "picture_processor"})


# if __name__ == "__main__":
#     test = call_chat_completion("绘制一个贪吃蛇")
#     print(test)
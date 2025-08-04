from config import conf, client, SYSTEM_PROMPT
import time

def build_prompt(module):
    """
        Build prompt based on JSON
    """
    title = module["title"]
    page_detail = module["page_detail"]
    page_name = module["page_name"]
    pages = module["page"]
    
    prompts = []
    for page in pages:
        prompts.append(f"""
            任务：基于React设计【{title}】的前端界面。
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
                        {"role": "system", "content": f"{SYSTEM_PROMPT}"},
                        {"role": "user", "content": prompt}
                    ],
                stream=False
            )
        res = response.choices[0].message.content
        return res
    
    except Exception as e:
        raise Exception(f"处理响应失败: {str(e)}")
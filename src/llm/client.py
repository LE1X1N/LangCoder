from config import conf, client, SYSTEM_PROMPT
import time
from typing import Dict, List, Optional, Tuple


History = List[Tuple[str, str]]
Messages = List[Dict[str, str]]


def build_prompt(page):
    """
        Build prompt based on JSON
    """
    prompt = f"""
            任务：基于React设计【{page["web_title"]}】的前端界面。
            项目背景：{page["web_detail"]}
            当前渲染模块：【{page["module_name"]}】
            当前渲染页面：【{page["page_name"]}】
            渲染需求：{page["page_desc"]} (仅展示UI，无需交互)
            参考模板：<begin> {page["page_tmpl"]} <end>
        """
    return prompt



def history_to_messages(history: History, system: str) -> Messages:
    messages = [{"role": 'system', "content": system}]
    for h in history:
        messages.append({"role": 'user', "content": h[0]})
        messages.append({"role": 'assistant', "content": h[1]})
    return messages



def messages_to_history(messages: Messages) -> Tuple[str, History]:
    assert messages[0]["role"] == "system"
    history = []
    for q, r in zip(messages[1::2], messages[2::2]):
        history.append([q["content"], r["content"]])
    return history


def call_chat_completion(messages):
    """
        Call LLM to generate code
    """
    try:
        # openai compatible
        response = client.chat.completions.create(
                model=conf["model"],  
                messages=messages,
                stream=False
            )
        res = response.choices[0].message.content
        return res
    
    except Exception as e:
        raise Exception(f"处理响应失败: {str(e)}")
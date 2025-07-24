import re
from typing import Dict, List, Optional, Tuple

import gradio as gr
from dashscope.api_entities.dashscope_response import Role
import random
from openai import OpenAI

import modelscope_studio.components.base as ms
import modelscope_studio.components.legacy as legacy
import modelscope_studio.components.antd as antd
import modelscope_studio.components.pro as pro

from config.app_conf import DEMO_LIST, SYSTEM_PROMPT, REACT_IMPORTS

# open-ai client
# you can launch a local openai server with vLLM
client = OpenAI(
    base_url="http://localhost:8000/v1",  
    api_key="token-xxxxx" 
)
MODEL = "Qwen2.5-Coder-7B-Instruct"

History = List[Tuple[str, str]]
Messages = List[Dict[str, str]]

def history_to_messages(history: History, system: str) -> Messages:
    messages = [{"role": Role.SYSTEM, "content": system}]
    for h in history:
        messages.append({"role": Role.USER, "content": h[0]})
        messages.append({"role": Role.ASSISTANT, "content": h[1]})
    return messages

def messages_to_history(messages: Messages) -> Tuple[str, History]:
    assert messages[0]["role"] == Role.SYSTEM
    history = []
    for q, r in zip(messages[1::2], messages[2::2]):
        history.append([q["content"], r["content"]])
    return history

def remove_code_block(text):
    pattern = r"```html\n(.+?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    else:
        return text.strip()

def history_render(history: History):
    return gr.update(open=True), history


def get_generated_files(text):
    patterns = {
        'html': r'```html\n(.+?)\n```',
        'jsx': r'```jsx\n(.+?)\n```',
        'tsx': r'```tsx\n(.+?)\n```',
    }
    result = {}

    for ext, pattern in patterns.items():
        matches = re.findall(pattern, text, re.DOTALL)
        if matches:
            content = '\n'.join(matches).strip()
            result[f'index.{ext}'] = content

    if len(result) == 0:
        result["index.html"] = text.strip()
    return result


def clear_history():
    gr.Success("History Cleared.")
    return [], ""


def demo_card_click(e: gr.EventData, ):
    index = e._data["component"]["index"]
    return DEMO_LIST[index]["prompt"]


"""
    Handle Sandbox compile or render error
"""
def handle_compile_error(e: gr.EventData, task_id: int):
    error_msg = e._data  # 
    print(f"Task_{task_id}【编译错误】： {error_msg}")
    return {last_error: f"Compile Error: {error_msg}"}

def handle_render_error(e: gr.EventData, task_id: int):
    error_msg = e._data['payload'][0] 
    print(f"Task_{task_id}:【渲染错误】: {error_msg}")
    return {last_error: f"Render Error: {error_msg}"}

def handle_compile_success(task_id: int):
    print(f"Task_{task_id}:【编译成功】: 代码编译成功，无语法错误，开始渲染...")


with gr.Blocks(css_paths="config/app.css") as demo:
    history = gr.State([])      # chat history
    setting = gr.State({"system": SYSTEM_PROMPT,})
    last_error = gr.State("")   # error 
    current_task_id = gr.State("")      # task 

    with ms.Application() as app:
        with antd.ConfigProvider():
            with antd.Row(gutter=[32, 12]) as layout:
                
                """Left side (input area)"""
                with antd.Col(span=24, md=8):
                    with antd.Flex(vertical=True, gap="middle", wrap=True):
                        # header
                        header = gr.HTML(
                            # """
                            #     <div class="left_header">
                            #         <img src="//img.alicdn.com/imgextra/i2/O1CN01KDhOma1DUo8oa7OIU_!!6000000000220-1-tps-240-240.gif" width="200px" />
                            #         <h1>网站界面设计</h2>
                            #     </div>
                            # """
                            """
                                <div class="left_header">
                                    <h1>网站界面设计</h2>
                                </div>
                            """
                        )
                        
                        # input
                        input = antd.InputTextarea(
                            size="large",
                            allow_clear=True,
                            placeholder="Please enter what kind of application you want",
                            elem_style={"height": "200px"} 
                        )
                        btn = antd.Button("发送", type="primary", size="large")
                        clear_btn = antd.Button("清除对话记录", type="default", size="large", danger=True)

                        # examples
                        antd.Divider("应用案例")
                        with antd.Flex(gap="small", wrap=True):
                            with ms.Each(DEMO_LIST):
                                with antd.Card(hoverable=True, as_item="card" ) as demoCard:
                                    antd.CardMeta()
                                demoCard.click(demo_card_click, outputs=[input])
                        
                        
                        # settings
                        antd.Divider("设置")
                        with antd.Flex(gap="small", wrap=True):
                            settingPromptBtn = antd.Button("⚙️ 设置系统提示词", type="default")
                            codeBtn = antd.Button("🧑‍💻 浏览代码", type="default")
                            historyBtn = antd.Button("📜 对话历史", type="default")

                    # set system Prompt buttons
                    with antd.Modal(
                        open=False, title="set system Prompt", width="800px"
                    ) as system_prompt_modal:
                        systemPromptInput = antd.InputTextarea(
                            SYSTEM_PROMPT, auto_size=True
                        )

                    settingPromptBtn.click(
                        lambda: gr.update(open=True),
                        inputs=[],
                        outputs=[system_prompt_modal],
                    )
                    system_prompt_modal.ok(
                        lambda input: ({"system": input}, gr.update(open=False)),
                        inputs=[systemPromptInput],
                        outputs=[setting, system_prompt_modal],
                    )
                    system_prompt_modal.cancel(
                        lambda: gr.update(open=False), outputs=[system_prompt_modal]
                    )

                    # view code button
                    with antd.Drawer(
                        open=False, title="code", placement="left", width="750px"
                    ) as code_drawer:
                        code_output = legacy.Markdown()

                    codeBtn.click(
                        lambda: gr.update(open=True), inputs=[], outputs=[code_drawer]
                    )
                    code_drawer.close(
                        lambda: gr.update(open=False), inputs=[], outputs=[code_drawer]
                    )

                    # history button
                    with antd.Drawer(
                        open=False, title="history", placement="left", width="900px"
                    ) as history_drawer:
                        history_output = legacy.Chatbot(
                            show_label=False,
                            flushing=False,
                            height=960,
                            elem_classes="history_chatbot",
                        )

                    historyBtn.click(
                        history_render,
                        inputs=[history],
                        outputs=[history_drawer, history_output],
                    )
                    history_drawer.close(
                        lambda: gr.update(open=False),
                        inputs=[],
                        outputs=[history_drawer],
                    )

                """ Right side (output area) """
                with antd.Col(span=24, md=16):
                    with ms.Div(elem_classes="right_panel"):
                        # header
                        gr.HTML('<div class="render_header"><span class="header_btn"></span><span class="header_btn"></span><span class="header_btn"></span></div>')                          
                        
                        # tabs for different states
                        with antd.Tabs(active_key="empty", render_tab_bar="() => null") as state_tab:
                            # 1. empty
                            with antd.Tabs.Item(key="empty"):
                                empty = antd.Empty(description="empty input", elem_classes="right_content")
                            # 2. loading
                            with antd.Tabs.Item(key="loading"):
                                loading = antd.Spin(True, tip="coding...", size="large", elem_classes="right_content")
                            # 3. render
                            with antd.Tabs.Item(key="render"):
                                sandbox = pro.WebSandbox(
                                    height="600",
                                    elem_classes="output-html",
                                    template="html",
                                )
                                # error process
                                sandbox.compile_success(handle_compile_success, inputs=[current_task_id], outputs=[last_error])
                                sandbox.compile_error(handle_compile_error, inputs=[current_task_id], outputs=[last_error])
                                sandbox.render_error(handle_render_error, inputs=[current_task_id], outputs=[last_error])



            def generation_code(query: Optional[str], _setting: Dict[str, str], _history: Optional[History],):
                if query is None:
                    query = ""
                if _history is None:
                    _history = []

                task_id = random.randint(1000, 9999)
                    
                messages = history_to_messages(_history, _setting["system"])
                messages.append({"role": Role.USER, "content": query})
   
                # open-ai compatible generation
                gen = client.chat.completions.create(
                        model=MODEL,  
                        messages=messages, 
                        stream=True
                    )

                full_content = ""  
                
                for chunk in gen:
                    content = chunk.choices[0].delta.content or ""
                    full_content += content
                    
                    finish_reason = chunk.choices[0].finish_reason
                    
                    if finish_reason == "stop":
                        # finish state
                        _history = messages_to_history(
                            messages + [{"role": "assistant", "content": full_content}]
                        )
                        # print("history")
                        # print(_history)
                        
                        generated_files = get_generated_files(full_content)
                        react_code = generated_files.get("index.tsx") or generated_files.get("index.jsx")
                        html_code = generated_files.get("index.html")
                        
                        yield {
                            code_output: full_content,
                            history: _history,
                            # sandbox: send_to_sandbox(remove_code_block(full_content)),                  
                            sandbox: gr.update(template="react" if react_code else "html",
                                                imports=REACT_IMPORTS if react_code else {},
                                                height=900,
                                                value={
                                                    "./index.tsx": """import Demo from './demo.tsx'
                                                                    import "@tailwindcss/browser"
                                                                    export default Demo
                                                                    """,
                                                    "./demo.tsx": react_code
                                                    } if react_code else {"./index.html": html_code},
                                                ),
                            state_tab: gr.update(active_key="render"),
                            code_drawer: gr.update(open=False),
                            current_task_id: task_id,
                        }
                    else:
                        # loading state
                        yield {
                            code_output: full_content,  
                            state_tab: gr.update(active_key="loading"),
                            code_drawer: gr.update(open=True),
                            current_task_id: task_id,
                        }
                
            btn.click(
                generation_code,
                inputs=[input, setting, history],
                outputs=[code_output, history, sandbox, state_tab, code_drawer, current_task_id],
            )

            clear_btn.click(clear_history, inputs=[], outputs=[history, input])


if __name__ == "__main__":
    demo.queue(default_concurrency_limit=20).launch(ssr_mode=False, share=False, debug=False)

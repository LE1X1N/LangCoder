import gradio as gr

import modelscope_studio.components.antd as antd
import modelscope_studio.components.base as ms
import modelscope_studio.components.pro as pro

from config import REACT_IMPORTS
from browser.manager import driver_registry, driver_lock, capture_screenshot
from util import get_generated_files


def handle_compile_error(e: gr.EventData, task_id: int):
    """ Compile Error """
    error_prompt = f"【编译错误】：{e._data['payload'][0]}"
    print(f"Task_{task_id} {error_prompt}")

def handle_render_error(e: gr.EventData, task_id: int):
    """ Render error """
    error_prompt = f"【渲染错误】：{e._data['payload'][0]}"
    print(f"Task_{task_id} :{error_prompt}")


def handle_compile_success(task_id: str, port: int):
    """ Compile Success """
    print(f"Task_{task_id}:【编译成功】: 代码编译成功，无语法错误，开始渲染...")
    with driver_lock:
        driver = driver_registry.get(task_id)
    if driver:
        capture_screenshot(task_id, driver)

def create_sandbox_demo(code_snippet, task_id, port, elem_id: str= "sandbox-iframe"):
    """
        Sandbox based on modelscope_studio sandboxs
    """
    generated_files = get_generated_files(code_snippet)
    react_code = generated_files.get("index.tsx") or generated_files.get("index.jsx")
    html_code = generated_files.get("index.html")
    
    with gr.Blocks() as demo:
        with ms.Application():
            with antd.ConfigProvider():
                task_id_state = gr.State(value=task_id)
                port_state = gr.State(value=port)
                
                # init sandbox
                sandbox = pro.WebSandbox(
                    height=1080,
                    template="react" if react_code else "html",
                    imports=REACT_IMPORTS,
                    value={
                        "./index.tsx": """import Demo from './demo.tsx'
                                        import "@tailwindcss/browser"
                                        export default Demo
                                        """,
                        "./demo.tsx": react_code
                    } if react_code else {"./index.html": html_code},
                    elem_id=elem_id
                )
                # trigger
                sandbox.compile_error(handle_compile_error, inputs=[task_id_state])
                sandbox.render_error(handle_render_error, inputs=[task_id_state])
                sandbox.compile_success(handle_compile_success, inputs=[task_id_state, port_state])
    
    print("Gradio starts!")
    demo.launch(
        ssr_mode=False,
        share=False,
        debug=False,
        prevent_thread_lock=True,
        server_port=port,
        server_name="0.0.0.0"
    )
    return demo
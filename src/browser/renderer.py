import gradio as gr

import modelscope_studio.components.antd as antd
import modelscope_studio.components.base as ms
import modelscope_studio.components.pro as pro

from config import REACT_IMPORTS
from src.util import get_generated_files


def launch_sandbox_demo(code_snippet, task_id, port, elem_id, browser_registry, browser_lock):
    """
        Sandbox based on modelscope_studio sandboxs
    """

    generated_files = get_generated_files(code_snippet)
    react_code = generated_files.get("index.tsx") or generated_files.get("index.jsx")
    html_code = generated_files.get("index.html")
    
    # compile / render 
    def handle_compile_error(e: gr.EventData, task_id: int):
        """ Compile Error """
        error_prompt = f"【编译错误】：{e._data['payload'][0]}"
        print(f"Task_{task_id} {error_prompt}")

    def handle_render_error(e: gr.EventData, task_id: int):
        """ Render error """
        error_prompt = f"【渲染错误】：{e._data['payload'][0]}"
        print(f"Task_{task_id} :{error_prompt}")

    def handle_compile_success(task_id: int):
        """ Compile Success """
        print(f"Task_{task_id}:【编译成功】: 代码编译成功，无语法错误，开始渲染...")
        with browser_lock:
            browser_registry.put(task_id)   # compile success flag
    
    with gr.Blocks() as demo:
        with ms.Application():
            with antd.ConfigProvider():
                task_id_state = gr.State(value=task_id)

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
                sandbox.compile_success(handle_compile_success, inputs=[task_id_state])
    
    print("Gradio starts!")
    demo.launch(
        ssr_mode=False,
        share=False,
        debug=False,
        prevent_thread_lock=False,
        server_port=port,
        server_name="0.0.0.0",
        quiet=True,
    )
    return demo
# Coder Artifacts with OpenAI Compatibility

This repository is a modified version of [Qwen2.5-Coder-Artifacts](https://huggingface.co/spaces/Qwen/Qwen2.5-Coder-Artifacts), adapted to support OpenAI-style API requests. This allows integration with OpenAI-compatible LLM server (such as vLLM) while maintaining the original interactive code generation capabilities.

## ⚙️ Installation

1. Clone this repo
``` bash
git clone <repository-url>
``` 

2. Install dependencies
``` bash
pip install -r requirements.txt
``` 

3. Ensure vLLM is installed for model serving
``` bash
pip install vllm
``` 

## 📖 Usage Guide

### 1. Launch a vLLM Server with OpenAI Compatibility
Start your model with vLLM's OpenAI-compatible API endpoint. Example command:

``` bash
# Launch with 2 GPUs (adjust based on your hardware)s
CUDA_VISIBLE_DEVICES=0,1 vllm serve path/to/your/Qwen2.5-Coder-7B-Instruct --port 8000  --gpu-memory-utilization 0.95  --served-model-name Qwen2.5-Coder-7B-Instruct  --enable_prefix_caching -tp 2 
```
### 2. Veify the Server
Test if the model server is running correctly with a sample request:

``` bash
# one simpe request
curl http://localhost:8000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
"model": "Qwen2.5-Coder-7B-Instruct",
"messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "Build a Snake game"}]
}'
```
You should receive a JSON response with generated content if the server is working properly.

### 3. Configure the Application
Modify the OpenAI client configuration in **app.py** to match your vLLM server:

``` python
# in app.py
client = OpenAI(
    base_url="http://localhost:8000/v1",   #  Your vLLM server URL
    api_key="token-xxxxx"   # Can be any
)

MODEL = "Qwen2.5-Coder-7B-Instruct"   #  Must match --served-model-name from vLLM command
```

###  4. Launch the Gradio Interface

``` python
python app.py
```

If successful, you'll see output similar to:

``` bash
* Running on local URL:  http://127.0.0.1:7860
* To create a public link, set `share=True` in `launch()`.
```

Open the provided URL in your browser to use the interface.
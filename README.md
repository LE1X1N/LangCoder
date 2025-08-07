# 代码界面渲染

## 1. Demo测试

基于gradio的可视化界面渲染流程Demo。

```shell
# 启动前端可视化界面
python launch_app.py
```


## 2. 服务启动

依赖 selenium/standalone-chrome 镜像作为浏览器访问代理，提供了全套 selenium+webdriver+headless 浏览器的功能

### 2.1 容器启动
``` bash
# 启动
docker run -d --network host --name selenium-chrome selenium/standalone-chrome

# 停止 
docker stop selenium-chrome
docker rm selenium-chrome
```

### 2.2 提供API服务
使用uwsgi / Flask 提供接口服务
``` bash
# 启动
uwsgi --ini config/uwsgi_service.ini

# 停止
uwsgi --stop log/uwsgi.pid
```


### 模型启动

``` bash

CUDA_VISIBLE_DEVICES=2,3 vllm serve ~/huggingface/Qwen3-Coder-30B-A3B-Instruct/  --port 8001  --gpu-memory-utilization 0.90  --served-model-name Qwen3 --enable_chunked_prefill --enable_prefix_caching

```


### 2.3 测试JSON访问服务

``` bash
curl -X POST http://localhost:50086/v1/gen_images -H "Content-Type: application/json"  -d @data.json

curl -X POST http://localhost:8687/v1/gen_images -H "Content-Type: application/json"  -d @test/data.json
```
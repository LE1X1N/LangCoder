# 代码界面渲染


## 1. 前端启动

基于gradio的可视化界面渲染流程

```shell
# 启动前端可视化界面
python launch_app.py
```



# 停止旧容器
docker stop selenium-chrome

# 启动新容器（添加 --add-host 映射宿主机 IP 到 host.docker.internal）
docker run -d -p 4444:4444 --add-host=host.docker.internal:host-gateway  --name selenium-chrome selenium/standalone-chrome


# 测试接口

``` bash
curl -X POST http://localhost:8687/v1/gen_images -H "Content-Type: application/json"  -d @data.json
```
from frontend.app import demo
import yaml

with open("config/system_conf.yaml", "r") as f:
    conf = yaml.safe_load(f)


if __name__ == "__main__":
    demo.launch(ssr_mode=False, share=False, debug=False, server_port=conf["port"])
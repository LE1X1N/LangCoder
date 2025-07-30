from flask import Flask
import yaml
from backend.api import api_bp

backend_app = Flask(__name__)
backend_app.register_blueprint(api_bp, url_prefix='/v1')

with open("config/system_conf.yaml", "r") as f:
    conf = yaml.safe_load(f)

if __name__ == "__main__":
    backend_app.run(host="0.0.0.0", port=conf["port"], debug=False)
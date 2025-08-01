from flask import Flask
from api.routes import api_bp
from config import conf

backend_app = Flask(__name__)
backend_app.register_blueprint(api_bp, url_prefix='/v1')

if __name__ == "__main__":
    backend_app.run(host="0.0.0.0", port=conf["port"], debug=False)
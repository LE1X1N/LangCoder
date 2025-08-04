from flask import Flask
from src.api.routes import api_bp
from config import conf
import multiprocessing

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_bp, url_prefix='/v1')
    return app
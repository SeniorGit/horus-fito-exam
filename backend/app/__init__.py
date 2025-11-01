from flask import Flask
from .config import Config
from .routes import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # REGISTER
    app.register_blueprint(users_bp, url_prefix='/api/users')

    return app
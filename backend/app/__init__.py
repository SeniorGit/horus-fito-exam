from flask import Flask
from .config import Config
from .routes import users_bp, protected_bp
from .extensions import jwt, close_db, cors
# from .models.user_model import User 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # db.init_app(app)
    # migrate.init_app(app, db)
    jwt.init_app(app)
    cors.init_app(app, 
                  origins=app.config['CORS_ORIGINS'],
                  methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], 
                  allow_headers=["Content-Type", "Authorization"],
                  supports_credentials=True
                  )
    app.teardown_appcontext(close_db)

    # REGISTER
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(protected_bp, url_prefix='/api/protected')
    return app
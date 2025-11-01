import psycopg2
import psycopg2.extras
from flask import g
from app.config import Config
from flask_cors import CORS
from flask_jwt_extended import JWTManager

jwt = JWTManager()
cors = CORS()

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME,
            port=Config.DB_PORT
        )
        g.db.cursor_factory = psycopg2.extras.RealDictCursor
        print("✅ Database connected successfully!")
        
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
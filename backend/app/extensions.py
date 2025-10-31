import psycopg2
import psycopg2.extras
from flask import g
from app.config import Config

# database connection
def get_db():
    if 'db' not in g:
        try:
            g.db = psycopg2.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,  # ← PASTIKAN INI ADA!
                database=Config.DB_NAME,
                port=Config.DB_PORT
            )
            g.db.cursor_factory = psycopg2.extras.RealDictCursor
            print("✅ Database connected successfully!")
        except psycopg2.Error as e:
            print(f"❌ Database connection failed: {e}")
            raise
    return g.db

# close database
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
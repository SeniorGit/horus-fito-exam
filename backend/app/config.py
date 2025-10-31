import os

class Config:
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'postgres')  
    DB_PASSWORD = os.getenv('DB_PASSWORD', '123')
    DB_NAME = os.getenv('DB_NAME', 'horus_fito_db')
    DB_PORT = int(os.getenv('DB_PORT', 5432))  
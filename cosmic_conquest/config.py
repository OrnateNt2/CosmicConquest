# cosmic_conquest/config.py

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "super_secret_key")
    DEBUG = True
    
    # Используем SQLite в корне проекта
    SQLALCHEMY_DATABASE_URI = "sqlite:///cosmic_conquest.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

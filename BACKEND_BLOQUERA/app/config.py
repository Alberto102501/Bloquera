import os
from pathlib import Path
from dotenv import load_dotenv

# Obtiene la ruta de la carpeta BACKEND_BLOQUERA y apunta a su .env
basedir = Path(__file__).resolve().parent.parent
load_dotenv(basedir / '.env')

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt_secret_default')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
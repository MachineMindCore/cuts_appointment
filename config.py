import os
from dotenv import load_dotenv 
load_dotenv()  # Carga todo el contenido de .env en variables de entorno


class Config:
    #SERVER_NAME = "localhost:5000"
    DEBUG = True
    SECRET_KEY = os.urandom(32).hex()
    #DATABASE_PATH = "src/database/contact_book.db"
    #DB_TOKEN = os.environ.get("DB_TOKEN", "")  # Para Encriptar la DB
    #ENCRYPT_DB = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///databases/users.db"
    SQLALCHEMY_BINDS = {"appointments" : "sqlite:///databases/appointments.db"}
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"

class DatabaseInitConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///databases/admin.db"
    SQLALCHEMY_BINDS = {"users" : "sqlite:///databases/users.db",
                        "appointments" : "sqlite:///databases/appointments.db"}
     

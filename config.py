import os
from dotenv import load_dotenv  # Instalar con pip install python-dotenv

load_dotenv()  # Carga todo el contenido de .env en variables de entorno


class Config:
    #SERVER_NAME = "localhost:5000"
    DEBUG = True

    #DATABASE_PATH = "src/database/contact_book.db"
    #DB_TOKEN = os.environ.get("DB_TOKEN", "")  # Para Encriptar la DB
    #ENCRYPT_DB = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///databases/admin.db"
    SQLALCHEMY_BINDS = {"users" : "sqlite:///databases/users.db",
                        "appointments" : "sqlite:///databases/appointments.db"}
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"

class DatabaseInitConfig:
    SQLALCHEMY_DATABASE_URI = "sqlite:///databases/admin.db"
    SQLALCHEMY_BINDS = {"users" : "sqlite:///databases/users.db",
                        "appointments" : "sqlite:///databases/appointments.db"}
     

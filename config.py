import os

class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(32).hex()
    SQLALCHEMY_DATABASE_URI = "sqlite:///databases/barber.db"
    TEMPLATE_FOLDER = "templates/"
    STATIC_FOLDER = "static/"

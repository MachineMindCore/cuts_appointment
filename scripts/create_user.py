import sys, os
sys.path.append(os.path.join(sys.path[0],'..'))
from src import app
from src.models.users import User
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import DatabaseInitConfig

demo = Flask(__name__)
demo.config.from_object(DatabaseInitConfig)
db = SQLAlchemy()
db.init_app(demo)
try:
    db.create_all()
except:
    print("could not create tables")

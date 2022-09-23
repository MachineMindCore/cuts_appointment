import sys, os, touch, getopt
sys.path.append(os.path.join(sys.path[0],'..'))

from pathlib import Path
from src import app
from src.models.entities import User, Appointment
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from config import DatabaseInitConfig
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import create_engine

def set_db(path, file):
    if os.path.exists(path+file):
        os.remove(path+file)
    touch.touch(path+file)
    return

data_path = "src/databases/"
file = None
engine = None
opts, args = getopt.getopt(sys.argv[1:], "b:p")
print(opts)
for opt, arg in opts:
    if opt == "-b":
        file = arg
        set_db(data_path, file)
        engine = create_engine('sqlite://'+data_path+file)
        meta.engine = engine
    if opt == "-t":
        create_tables(meta_obj, arg, engine)


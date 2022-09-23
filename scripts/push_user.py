import sys, os, argparse
sys.path.append(os.path.join(sys.path[0],'..'))

from src.models.entities import User, Appointment
from flask_sqlalchemy import SQLAlchemy
from config import DatabaseInitConfig
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy import create_engine

parser = argparse.ArgumentParser()
parser.add_argument("-user")
parser.add_argument("-pass")
parser.add_argument("-name")
parser.add_argument("-sur")
parser.add_argument("-number")
parser.add_argument("-email")
parser.add_argument("-access")

path = "src/databases/user.db"
engine = create_engine(path)

new_user = User(
    username = args.user
)


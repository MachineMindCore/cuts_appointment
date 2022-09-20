from src.extentions.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __bind_key__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
   
    def __init__(self, username, password, first_name, last_name, number, email):
        self.username = username
        self.password_hash = self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(db.Model):
    __bind_key__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    number = db.Column(db.String)
    email = db.Column(db.String)
    

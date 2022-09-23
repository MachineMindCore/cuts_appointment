from src.extentions.extentions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False, unique=True)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    number = db.Column(db.String(200), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    priority = db.Column(db.String(200), nullable=False)
   
    def __init__(self, username, password, first_name, last_name, number, email, priority="customer"):
        self.username = username
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.priority = priority

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        return

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def check_priority(self):
        if self.priority == "admin":
            return True
        else:
            return False

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
        return

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)
    
    @staticmethod
    def get_by_phone(phone):
        return User.query.filter_by(number=phone).first()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_by_user(user):
        return User.query.filter_by(username=user).first()
    
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Appointment(db.Model):
    __bind_key__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    price = db.Column(db.Integer)
    service = db.Column(db.String)
    number = db.Column(db.String)
    email = db.Column(db.String)
    

            


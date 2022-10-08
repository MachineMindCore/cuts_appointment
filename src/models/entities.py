import datetime as dt
from src.extentions.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    number = db.Column(db.String(10), unique=True, nullable=False)
    flag = db.Column(db.String(80), nullable=False)


    def __init__(self, username, password, firstName, lastName, number, email, flag="customer"):
        self.username = username
        self.set_password(password)
        self.firstName = firstName
        self.lastName = lastName
        self.number = number
        self.email = email
        self.flag = flag

    def set_password(self, in_password):
        self.password = generate_password_hash(in_password)
        return

    def check_password(self, in_password):
        return check_password_hash(self.password, in_password)

    def check_priority(self):
        if self.flag == "admin":
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
        return f"{self.firstName} {self.lastName}"


class Appointment(db.Model):
    __tablename__ = "appointments"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String) #service : username
    description = db.Column(db.String)
    value = db.Column(db.Integer)
    date = db.Column(db.DateTime, unique=True)
    init_hour = db.Column(db.Integer)
    end_hour = db.Column(db.Integer)
    status = db.Column(db.String)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, name, date, status="apartado"):
        self.name = name
        self.date = date
        self.status = status
        self.set_value()
        self.set_init_hour()
        self.set_end_hour()
        self.set_id_user()
        return

    def set_value(self):
        service = self.name.split(":")[0]
        if service == "rasurada":
            self.value = 20000
            self.description = "razurada simple"
        elif service == "corte":
            self.value = 35000
            self.description = "corte completo"
        elif service == "limpieza":
            self.value = 25000
            self.description = "limpieza completa"
        else:
            self.value = 0
            self.description = "servicio personalizado"
        return

    def set_init_hour(self):
        self.init_hour = self.date.hour
        return
    
    def set_end_hour(self):
        self.end_hour = self.date.hour + 1
        return

    def set_id_user(self):
        username = self.name.split(":")[1]
        print(username)
        self.id_user = User.get_by_user(username).id
        return
    
    @staticmethod
    def get_all():
        return Appointment.query.all()
    
    @staticmethod
    def check_date(date):
        appointment = Appointment.query.filter_by(date=date).first()
        if appointment and appointment["date"] == date:
            return True
        return False

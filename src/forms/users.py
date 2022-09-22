from flask import Blueprint, request, render_template
from flask_sqlalchemy import SQLAlchemy
from src.models.users import User 
from src.extentions.database import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from src.utils.error_handling import error_handler

userform = Blueprint("userform", __name__)

@userform.route('/log_in', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        pass
    else:
        return render_template("users/log_in.html")

@userform.route('/sign_up', methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        try:
            new_user = User(
                username = request.form.get("username"),
                password = request.form.get("password"),
                first_name = request.form.get("first_name"),
                last_name = request.form.get("last_name"),
                number = request.form.get("number"),
                email = request.form.get("email"),
            )
            db.session.add(new_user)
            db.session.commit() 
            return "<p> USer created for {}<p>".format(new_user)
            #Change return for HTML file
        except IntegrityError as e:
            error = error_handler(e)
            return "<p> Lo siento, {} <p>".format(error)
    else:
        return render_template("users/sign_up.html")

@userform.route('/log_in', methods=["GET", "POST"])
def log_in():
    try:
        appointment = Appointment(
            username = request.form.get("username"),
            service = request.form.get("service"),
        )
        db.session.add(apoointment)
        db.session.commit()
        return  "<p> Welcome {} <p>".format()
    except SQLAlchemyError as e:
        error = error_handler(e)
        return "<p> Lo siento, {} <p>".format(error)
    

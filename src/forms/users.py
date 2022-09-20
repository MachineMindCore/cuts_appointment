from flask import Blueprint, request, render_template
from flask_sqlalchemy import SQLAlchemy
from src.models.users import User 
from src.extentions.database import db

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
        print(request.form.get("password"))
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
        #Change return for HTML file
        return "<p>Welcome {}<p>".format(new_user.username)
    else:
        return render_template("users/sign_up.html")



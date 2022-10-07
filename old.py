from src.models.entities import User


from src.models.forms import SignupForm, LoginForm
from src.extentions.extentions import db, login_manager
from src.utils.handlers import signup_handler
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from werkzeug.urls import url_parse


from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user, login_user, logout_user
from flask import (render_template, redirect, url_for,
                   request, current_app)


def sign_up():
    form = SignupForm()
    error = None
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        number = form.number.data

        access, error = signup_handler(username, email, number)
        if not access:
            pass
        else:
            # Creamos el usuario y lo guardamos
            new_user = User(
                username = username, 
                password = password,
                first_name = first_name,
                last_name = last_name,
                email = email,
                number = number,
                priority = "customer",
            )
            new_user.save()
            return redirect("/log_in")
    return render_template("users/sign_up.html", form=form, error=error)

def log_in():
    print(current_user)
    if current_user.is_authenticated:
        return render_template("public/index.html")
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_user(form.username.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return render_template("public/index.html")


#################
from flask import render_template, url_for, request

def home():
    template_vars = { 
        "title": "Barber",
        "state": "inicio"
    }
    return render_template("public/index.html", **template_vars)

def salon():
    template_vars = { 
        "title": "Barber - Salon",
        "state": "salon"
    }
    return render_template("public/salon.html", **template_vars)




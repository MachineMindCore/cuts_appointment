from flask import render_template, redirect, url_for
from src.extentions.extentions import db
from src.models.forms import LoginForm, SignupForm
from src.models.entities import User

# Authentication functions


def register():
    registro = SignupForm()

    if registro.validate_on_submit():
        new_user = User(
            username=registro.username.data,
            email=registro.email.data, password=registro.password.data,
            firstName=registro.firstName.data,
            lastName=registro.lastName.data,
            number=registro.number.data, flag="1"
        )
        db.session.add(new_user)
        db.session.commit()
        db.session.close()
        return redirect(url_for('home.index'))
    return render_template('register.html', formi=registro)


def login():
    login = LoginForm()

    if login.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', formi=login)

# Public sites


def index():
    template_vars = {
        "title": "Barber",
        "state": "inicio"
    }
    return render_template("index.html", **template_vars)


def salon():
    template_vars = {
        "title": "Barber - Salon",
        "state": "salon"
    }
    return render_template("salon.html", **template_vars)

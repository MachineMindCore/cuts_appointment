from flask import render_template, redirect, url_for, flash
from src.extentions.database import db
from src.extentions.userstore import user_datastore
from src.models.forms import LoginForm, SignupForm
from src.models.entities import User
from flask_security import current_user, login_user, login_required, logout_user

# Authentication functions


def register():
    registro = SignupForm()

    if registro.validate_on_submit():
        new_user = User(
            username=registro.username.data,
            email=registro.email.data, password=registro.password.data,
            firstName=registro.firstName.data,
            lastName=registro.lastName.data,
            number=registro.number.data,
        )
        db.session.add(new_user)
        db.session.commit()
        db.session.close()

        flash('Registro logrado exitosamente', "success")
        return render_template('regis_ success.html')
    return render_template('register.html', formi=registro)


def login():
    login = LoginForm()
    username = login.username.data
    password = login.password.data

    if login.validate_on_submit():
        user = User.get_by_user(username)
        if user.check_password(password):
            login_user(user, remember=True)
            flash("looged in")
            print(current_user)
            return redirect(url_for('home.index'))
        else:
            return "Incorrect Password"

    return render_template('login.html', formi=login)

@login_required
def logout():
    logout_user()
    return redirect(url_for("home.index"))

# Private sites
@login_required
def dash():
    return f"{current_user}"

# Public sites

def get_user_storage():
    return f"{user_datastore}"

def get_user():
    return current_user


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

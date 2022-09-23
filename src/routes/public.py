<<<<<<< HEAD
from re import template
from flask import Blueprint, render_template, url_for

public_blueprint = Blueprint('public_blueprint', __name__)

@public_blueprint.route('/')
def home():
    template_vars = { 
        "title": "Barber",
        "state": "inicio"
    }
    return render_template("public/index.html", **template_vars)

@public_blueprint.route('/salon')
def salon():
    template_vars = { 
        "title": "Barber - Salon",
        "state": "salon"
    }
    return render_template("public/salon.html", **template_vars)
 
=======
from flask import Blueprint, render_template, url_for, request
from src.controllers.public import home, salon

public_blueprint = Blueprint('public_blueprint', __name__)

public_blueprint.add_url_rule('/', view_func=home)
public_blueprint.add_url_rule('/salon', view_func=salon)


>>>>>>> 5f32aff (sign_up changed, models changed, mvc added)


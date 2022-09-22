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
 


from flask import Blueprint, render_template, url_for

public_blueprint = Blueprint('public_blueprint', __name__)

@public_blueprint.route('/')
def home():
    return render_template("public/index.html", title = "Barber")

@public_blueprint.route('/salon')
def salon():
    return render_template("public/salon.html", title = "Barber - Salon")



from flask import Blueprint, render_template, url_for

public_blueprint = Blueprint('public_blueprint', __name__)

@public_blueprint.route('/')
def home():
    try:
        return render_template("public/index.html")
    except:
        return "index not found"


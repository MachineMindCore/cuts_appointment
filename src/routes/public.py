from flask import Blueprint, render_template

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def home():
    return render_template("public/index.html")

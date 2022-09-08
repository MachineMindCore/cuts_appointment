from flask import Blueprint, render_template, url_for
msg= "no se"

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def home():
    return render_template("public/index.html")

@blueprint.route('/PATH')
def get_path():
    return f"<h1>{msg}<h1>"

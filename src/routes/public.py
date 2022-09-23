from flask import Blueprint, render_template, url_for, request
from src.controllers.public import home, salon

public_blueprint = Blueprint('public_blueprint', __name__)

public_blueprint.add_url_rule('/', methods=["GET", "POST"], view_func=home)
public_blueprint.add_url_rule('/salon', methods=["GET", "POST"], view_func=salon)




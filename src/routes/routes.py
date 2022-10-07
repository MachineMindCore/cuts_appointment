from flask import Blueprint
from src.controllers.functions import *

home = Blueprint('home', __name__, template_folder='templates',
                 static_folder='static')

home.add_url_rule('/', methods=['GET', 'POST'], view_func=index)
home.add_url_rule('/salon', methods=['GET', 'POST'], view_func=salon)
home.add_url_rule('/login', methods=['GET', 'POST'], view_func=login)
home.add_url_rule('/registro', methods=['GET', 'POST'], view_func=register)

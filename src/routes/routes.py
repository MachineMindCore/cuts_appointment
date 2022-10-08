from flask import Blueprint
from src.controllers.functions import (
    index,
    salon,
    login,
    register,
    get_user,
    get_user_storage,
    logout,
    dash,
    availability,
)

home = Blueprint('home', __name__, template_folder='templates',
                 static_folder='static')

home.add_url_rule('/', methods=['GET', 'POST'], view_func=index)
home.add_url_rule('/salon', methods=['GET', 'POST'], view_func=salon)
home.add_url_rule('/login', methods=['GET', 'POST'], view_func=login)
home.add_url_rule('/registro', methods=['GET', 'POST'], view_func=register)
home.add_url_rule('/user', methods=['GET'], view_func=get_user)
home.add_url_rule('/userstorage', methods=['GET'], view_func=get_user_storage)
home.add_url_rule('/logout', methods=['GET', 'POST'], view_func=logout)
home.add_url_rule('/dash', methods=['GET', 'POST'], view_func=dash)
home.add_url_rule('/avaliable', methods=['GET'], view_func=availability)
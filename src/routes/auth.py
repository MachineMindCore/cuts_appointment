from flask import Blueprint, request, render_template
from flask_sqlalchemy import SQLAlchemy
from src.models.entities import User 
from src.extentions.extentions import db
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from src.controllers.auth import log_in, sign_up
#from src.utils.error_handling import error_handler

auth_blueprint = Blueprint("userform", __name__)

auth_blueprint.add_url_rule('/log_in', methods=["GET", "POST"], view_func=log_in)
auth_blueprint.add_url_rule('/sign_up', methods=["GET", "POST"], view_func=sign_up)


from .routes.public import public_blueprint
from .routes.auth import auth_blueprint
from .models.forms import LoginForm, SignupForm
from .models.entities import User
from .extentions.extentions import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
# from flask_bootstrap import Bootstrap
from config import Config

app = Flask(
    __name__,
    static_url_path = "",
)


# bootstrap =  Bootstrap(app)
app.config.from_object(Config)
app.register_blueprint(public_blueprint)
app.register_blueprint(auth_blueprint)
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user):
    return User.get_by_user(user)

@app.before_first_request
def create_tables():
    db.create_all()

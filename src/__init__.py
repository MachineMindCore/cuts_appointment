from .routes.routes import home
from .extentions.extentions import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config

app = Flask(
    __name__,
    static_url_path = "",
)


bootstrap =  Bootstrap(app)
app.config.from_object(Config)
app.register_blueprint(home)
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

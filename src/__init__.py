from .routes.public import public_blueprint
from flask import Flask
# from flask_bootstrap import Bootstrap
from config import Config

app = Flask(
    __name__,
    static_url_path = "",
    static_folder = Config.STATIC_FOLDER,
    template_folder = Config.TEMPLATE_FOLDER,
)

# bootstrap =  Bootstrap(app)
app.config.from_object(Config)
app.register_blueprint(public_blueprint)



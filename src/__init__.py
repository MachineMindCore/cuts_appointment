from .routes.routes import home
from .extentions.database import db
from .extentions.userstore import user_datastore
from .controllers.functions import update_appointments_status, test_daemon
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_security import Security
from threading import Thread 
app = Flask(
    __name__,
    static_url_path = "",
)


bootstrap =  Bootstrap(app)
app.config.from_object(Config)
app.register_blueprint(home)
app.security = Security(app, user_datastore)

db.init_app(app)


#db_updater = Thread(target=update_appointments_status, kwargs={"db": db, "app": app})
#db_updater.start()
#db_updater.join()

@app.before_first_request
def create_tables():
    db.create_all()

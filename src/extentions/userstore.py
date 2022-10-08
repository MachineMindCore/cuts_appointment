from src.extentions.database import db
from flask_security import current_user, auth_required, SQLAlchemySessionUserDatastore
from src.models.entities import User, Appointment

user_datastore = SQLAlchemySessionUserDatastore(db, User, Appointment)
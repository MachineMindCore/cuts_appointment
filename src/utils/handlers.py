from src.models.entities import User

def signup_handler(username: str, email: str, number: str):
    access = True
    error = "Not error"
    if User.get_by_user(username) != None:
        access = False
        error = "Lo siento, el usuario {} ya esta en uso".format(username)
    if User.get_by_email(email) != None:
        access = False
        error = "Lo siento, el email {} ya esta en uso".format(email)
    if User.get_by_phone(number) != None:
        access = False
        error = "Lo siento, el numero de telefono {} ya esta en uso".format(number)
    return access, error

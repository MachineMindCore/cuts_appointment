def error_handler(exception):
    exc_type = str(type(exception))
    if "IntegrityError" in exc_type:
        msg = str(exception.__dict__["orig"])
        entity = ""
        atributte = ""

        if "UNIQUE" in msg:
            entity = msg.split('.')[-1]

        if entity == "email": 
            atributte = "correo"
        elif entity == "number": 
            atributte = "numero"
        elif entity == "username": 
            atributte ="usuario"
        error = "el {} ya esta en uso".format(atributte)

    return error

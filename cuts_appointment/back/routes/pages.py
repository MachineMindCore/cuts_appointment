from flask import Blueprint

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def home():
    return "<h1>Aqui va mi pagina principal (っ◕‿◕)っ<h1>"

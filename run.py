from src.routes.public import blueprint
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.register_blueprint(blueprint)

if __name__=="__main__":
    app.run()

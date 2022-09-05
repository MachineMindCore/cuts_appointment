from src.routes.public import blueprint
from flask import Flask

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__=="__main__":
    app.run()

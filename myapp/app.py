from flask import Flask

from api.routes import api
from client.routes import client


def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(client)

    return app

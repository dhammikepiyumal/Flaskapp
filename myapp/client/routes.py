from flask import Blueprint

client = Blueprint('client', __name__)


@client.route('/')
def index():
    return '<h1>Welcome to the homepage!</h1>'

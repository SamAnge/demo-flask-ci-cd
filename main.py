"""This module does blah blah."""

from flask import Flask

APP = Flask(__name__)

@APP.route('/home')
def home():
    """return greetings."""
    return 'Hello World'

APP.run(host='0.0.0.0',port=5000)

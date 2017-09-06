#!/usr/bin/python3
from flask import Flask
"""
starting the flask application
"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def non_hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def default(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int: num>', strict_slashes=False)
def number(num):
    return "{} is a number".format(num)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

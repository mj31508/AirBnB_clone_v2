#!/usr/bin/python3
from flask import Flask
from flask import render_template
"""
starting the flask application
"""
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hbnb():
    return "Hello HBNB!"


@app.route('/hbnb')
def non_hbnb():
    return "HBNB"


@app.route('/c/<text>')
def ctext(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/')
@app.route('/python/<text>')
def default(text="is cool"):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:num>')
def number(num):
        return "{} is a number".format(num)

@app.route('/number_template/<int: number>')
def render(number):
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

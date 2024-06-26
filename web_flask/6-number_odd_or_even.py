#!/usr/bin/python3
"""Start a Flask application.
Routes: /, /hbnb, /c/<text>,
        /python/<text>, /number/<n>,
                /number_template/<n>, /number_odd_or_even/<n>
                """

from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Display "Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c_text(text):
    """Display custom text given"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """Display 'Python' followed by the value of <text>"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def num(n):
    """Display text only if int is supplied"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    info = ""
    if n % 2 == 0:
        info = '{} is even'.format(n)
    else:
        info = '{} is odd'.format(n)
    return render_template('6-number_odd_or_even.html', info=info)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

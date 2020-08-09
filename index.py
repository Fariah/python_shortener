#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, make_response, render_template
app = Flask(__name__, template_folder="templates")

@app.route('/')
def hello_world():
    return 'Hello World!</br>It would be a new telegram bot.'

@app.errorhandler(404)
def not_found(self):
    """Page not found."""
    return make_response(render_template("404.html"), 404)

if __name__ == '__main__':
    app.run(debug=True)
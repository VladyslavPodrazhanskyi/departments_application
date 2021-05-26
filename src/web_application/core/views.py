# src/web_application/core/__init__.py

from flask import render_template
from src.web_application.core import core


@core.route('/')
def index():
    """ View function for home page. """
    return render_template('index.html')


@core.route('/api')
def api():
    """ View function for API page. """
    return render_template('api.html')


@core.app_errorhandler(404)
def error_404(error):
    """ View function for page error 404. """
    return render_template("404.html"), 404

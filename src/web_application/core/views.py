from flask import render_template
from src.web_application.core import core


@core.route('/')
def index():
    return render_template('index.html')


@core.app_errorhandler(404)
def error_404(error):
    return render_template("404.html"), 404

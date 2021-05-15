from flask import Blueprint, render_template, current_app, redirect, url_for

# from src.services.department import DepartmentService

core = Blueprint('core', __name__)


@core.route('/home')
@core.route('/')
def index():
    # return render_template('index.html')
    print(current_app.config)
    return 'Hello, this is home page'


@core.route('/about')
def about():
    # return render_template('index.html')
    return render_template('about.html')

# @core.app_errorhandler(404)
# def error_404(error):
#     return render_template("404.html"), 404

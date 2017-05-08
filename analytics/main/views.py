from flask import render_template

from . import main
from ..models import get_summary

@main.route('/')
def index():
    petsafe = get_summary('petsafe')
    sportdog = get_summary('sportdog')
    return render_template('index.html', petsafe=petsafe, sportdog=sportdog)

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

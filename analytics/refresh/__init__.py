from flask import Blueprint

refresh = Blueprint('refresh', __name__)

from . import views
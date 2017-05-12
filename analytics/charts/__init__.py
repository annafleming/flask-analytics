from flask import Blueprint

charts = Blueprint('charts', __name__)

from . import views
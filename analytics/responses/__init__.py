from flask import Blueprint

responses = Blueprint('responses', __name__)

from . import views
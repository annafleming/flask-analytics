from flask import render_template
from flask import jsonify

from . import refresh
from ..models.summary import get_summary
from ..config import Config
from .. import db
import json


@refresh.route('/')
def index():
    return 'refresh'


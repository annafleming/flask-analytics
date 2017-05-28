from flask import render_template
from flask import jsonify

from . import refresh
from ..models.summary import get_summary
from ..config import Config
from .. import db
import json
import time


@refresh.route('/')
def index():
    trends = {
        'petsafe': get_summary('petsafe'),
        'sportdog': get_summary('sportdog'),
    }
    db.analytics.delete_many({"type": "summary"})
    db.analytics.insert_one({'type': 'summary', 'data': trends})
    return 'True'


from . import charts
from ..models.trends import get_finished, get_completed, get_feedback_types, get_website_rating, get_product_rating
from ..models.summary import get_summary
import json
from flask import jsonify
from .. import db

@charts.route('/summary')
def summary():
    entry = db.analytics.find_one({'type': 'summary'})
    if not entry:
        trends = {
            'petsafe': get_summary('petsafe'),
            'sportdog': get_summary('sportdog'),
        }
        db.analytics.insert_one({'type': 'summary', 'data': trends})
    return jsonify(db.analytics.find_one({'type': 'summary'})['data'])

@charts.route('/finished')
def finished():
    trends = {
        'petsafe': get_finished('petsafe'),
        'sportdog': get_finished('sportdog'),
    }
    return jsonify(trends)


@charts.route('/completed')
def completed():
    trends = {
        'petsafe': get_completed('petsafe'),
        'sportdog': get_completed('sportdog'),
    }
    return jsonify(trends)

@charts.route('/feedback_type')
def feedback_type():
    trends = {
        'petsafe': get_feedback_types('petsafe'),
        'sportdog': get_feedback_types('sportdog'),
    }
    return jsonify(trends)

@charts.route('/website_rating')
def website_rating():
    trends = {
        'petsafe': get_website_rating('petsafe'),
        'sportdog': get_website_rating('sportdog'),
    }
    return jsonify(trends)


@charts.route('/product_rating')
def product_rating():
    trends = {
        'petsafe': get_product_rating('petsafe'),
        'sportdog': get_product_rating('sportdog'),
    }
    return jsonify(trends)

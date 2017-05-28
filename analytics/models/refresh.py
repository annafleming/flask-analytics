from ..models.summary import get_summary
from ..models.trends import get_finished, get_completed, get_feedback_types, get_website_rating, get_product_rating
from flask import jsonify
from .. import db


def refresh_all():
    db.analytics.delete_many({})
    db.analytics.insert_one({'type': 'summary', 'data': {
        'petsafe': get_summary('petsafe'),
        'sportdog': get_summary('sportdog'),
    }})
    db.analytics.insert_one({'type': 'finished', 'data': {
        'petsafe': get_finished('petsafe'),
        'sportdog': get_finished('sportdog'),
    }})
    db.analytics.insert_one({'type': 'completed', 'data': {
        'petsafe': get_completed('petsafe'),
        'sportdog': get_completed('sportdog'),
    }})
    db.analytics.insert_one({'type': 'feedback_types', 'data': {
        'petsafe': get_feedback_types('petsafe'),
        'sportdog': get_feedback_types('sportdog'),
    }})
    db.analytics.insert_one({'type': 'website_rating', 'data': {
        'petsafe': get_website_rating('petsafe'),
        'sportdog': get_website_rating('sportdog'),
    }})
    db.analytics.insert_one({'type': 'product_rating', 'data': {
        'petsafe': get_product_rating('petsafe'),
        'sportdog': get_product_rating('sportdog'),
    }})
    return 'True'


def get_data(key):
    entry = db.analytics.find_one({'type': key})
    if not entry:
        return ''
    else:
        return jsonify(entry['data'])


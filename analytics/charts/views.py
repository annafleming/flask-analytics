from . import charts
from ..services import db_operations
from flask import jsonify


@charts.route('/summary')
def summary():
    return jsonify(db_operations.fetch_analytics('summary'))


@charts.route('/finished')
def finished():
    return jsonify(db_operations.fetch_analytics('finished'))


@charts.route('/completed')
def completed():
    return jsonify(db_operations.fetch_analytics('completed'))


@charts.route('/feedback_type')
def feedback_type():
    return jsonify(db_operations.fetch_analytics('feedback_types'))


@charts.route('/website_rating')
def website_rating():
    return jsonify(db_operations.fetch_analytics('website_rating'))


@charts.route('/product_rating')
def product_rating():
    return jsonify(db_operations.fetch_analytics('product_rating'))

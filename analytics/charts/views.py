from . import charts
from ..models.refresh import get_data


@charts.route('/summary')
def summary():
    return get_data('summary')


@charts.route('/finished')
def finished():
    return get_data('finished')


@charts.route('/completed')
def completed():
    return get_data('completed')


@charts.route('/feedback_type')
def feedback_type():
    return get_data('feedback_types')


@charts.route('/website_rating')
def website_rating():
    return get_data('website_rating')


@charts.route('/product_rating')
def product_rating():
    return get_data('product_rating')

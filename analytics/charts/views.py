from . import charts
from ..models.trends import get_finished, get_completed
import json


@charts.route('/finished')
def finished():
    trends = {
        'petsafe': get_finished('petsafe'),
        'sportdog': get_finished('sportdog'),
    }
    return json.dumps(trends)


@charts.route('/completed')
def completed():
    trends = {
        'petsafe': get_completed('petsafe'),
        'sportdog': get_completed('sportdog'),
    }
    return json.dumps(trends)

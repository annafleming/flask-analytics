from . import charts
from ..models.trends import get_finished
import json


@charts.route('/finished')
def finished():
    trends = {
        'petsafe': get_finished('petsafe'),
        'sportdog': get_finished('sportdog'),
    }
    return json.dumps(trends)

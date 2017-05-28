from . import refresh
from ..models.refresh import refresh_all, get_update_timestamp


@refresh.route('/')
def index():
    return refresh_all()


@refresh.route('/last_updated')
def last_updated():
    return get_update_timestamp()

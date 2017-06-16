from . import refresh
from ..models.refresh import refresh_all
from ..services import db_operations

@refresh.route('/')
def index():
    return refresh_all()


@refresh.route('/last_updated')
def last_updated():
    return str(db_operations.fetch_timestamp('updated_analytics'))

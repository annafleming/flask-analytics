from . import refresh
from ..models.refresh import refresh_all


@refresh.route('/')
def index():
    return refresh_all()



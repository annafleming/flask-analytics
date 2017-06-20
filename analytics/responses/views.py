import json
from . import responses
from ..services import db_operations


@responses.route('/fetch/<name>')
def fetch(name):
    return json.dumps(
        list(db_operations.fetch_surveys(
            site_name=name,
            columns=['site', 'survey_type', 'EndDate', 'ProductRating', 'WebsiteRating'])),
        separators=(',', ':'))

from . import responses
from ..services import db_operations
from flask import jsonify


@responses.route('/fetch/<name>')
def fetch(name):
    # columns = ['site', 'survey_type', 'EndDate', 'ProductRating', 'WebsiteRating']
    columns = ['site', 'survey_type', 'EndDate']
    surveys = list(db_operations.fetch_surveys(site_name=name, columns=columns))
    response = {
        'survey_responses': surveys,
        'columns': columns,
    }
    return jsonify(response)


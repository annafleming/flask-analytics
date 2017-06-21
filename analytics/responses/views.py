from . import responses
from ..services import db_operations
from flask import jsonify, request


@responses.route('/fetch/<name>')
def fetch(name):
    page = 1
    if request.args.get('page'):
        page = request.args.get('page')
    limit = 20
    if request.args.get('limit'):
        limit = request.args.get('limit')
    # columns = ['site', 'survey_type', 'EndDate', 'ProductRating', 'WebsiteRating']
    columns = ['site', 'survey_type', 'EndDate']
    surveys = list(db_operations.fetch_surveys(site_name=name, columns=columns, page=page, limit=limit))
    response = {
        'survey_responses': surveys,
        'columns': columns,
        'total': int(db_operations.fetch_surveys_count(site_name=name))
    }
    return jsonify(response)


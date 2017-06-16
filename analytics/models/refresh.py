from flask import jsonify
from .. import db
from ..helpers.datetime_helper import get_timestamp
from ..models.csv_reader import load_dataset_from_csv
from .dataset_settings import file_names, column_rename
from ..models.dataset_loader import load_dataset
from analytics.config import Config
from ..models.api_loader import import_surveys
from .stats import get_summary, get_finished, get_completed, get_feedback_types, get_website_rating, get_product_rating
from ..services import db_operations


def refresh_all():
    import_surveys()
    save_survey_entries()
    db_operations.remove_analytics()
    db_operations.insert_analytics([
        {'type': 'summary', 'data': get_summary([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'finished', 'data': get_finished([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'completed', 'data': get_completed([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'feedback_types', 'data': get_feedback_types([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'website_rating', 'data': get_website_rating([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'product_rating', 'data': get_product_rating([Config.PETSAFE_APP, Config.SPORTDOG_APP])}])
    timestamp = get_timestamp()
    db.analytics.insert_one({'type': 'timestamp', 'data': timestamp})
    return str(timestamp)


def get_data(key):
    entry = db.analytics.find_one({'type': key})
    if not entry:
        return ''
    else:
        return jsonify(entry['data'])


def get_update_timestamp():
    return get_data('timestamp')


def save_survey_entries():
    surveys = [
        {'site': Config.PETSAFE_APP, 'survey_type': Config.VOC_SURVEY},
        {'site': Config.PETSAFE_APP, 'survey_type': Config.COMMENT_CARD_SURVEY},
        {'site': Config.SPORTDOG_APP, 'survey_type': Config.VOC_SURVEY},
        {'site': Config.SPORTDOG_APP, 'survey_type': Config.COMMENT_CARD_SURVEY},
    ]
    for survey in surveys:
        ds = load_dataset(survey['site'], survey['survey_type'],
                          list(column_rename[survey['site']][survey['survey_type']].values()))
        for index, row in ds.iterrows():
            data = {}
            for column in list(column_rename[survey['site']][survey['survey_type']].values()):
                data['site'] = survey['site']
                data['survey_type'] = survey['survey_type']
                data[column] = row[column]
            db.surveys.insert_one(data)


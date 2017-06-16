from ..models.summary import get_summary
from ..models.trends import get_finished, get_completed, get_feedback_types, get_website_rating, get_product_rating
from flask import jsonify
from .. import db
from ..helpers.datetime_helper import get_timestamp
from ..models.csv_reader import load_dataset_from_csv
from .dataset_settings import file_names, column_rename
from ..models.dataset_loader import load_dataset
from analytics.config import Config
from ..models.api_loader import import_surveys

def refresh_all():
    import_surveys()
    save_survey_entries()
    db.analytics.delete_many({})
    db.analytics.insert_one({'type': 'summary', 'data': {
        'petsafe': get_summary('petsafe'),
        'sportdog': get_summary('sportdog'),
    }})
    db.analytics.insert_one({'type': 'finished', 'data': {
        'petsafe': get_finished('petsafe'),
        'sportdog': get_finished('sportdog'),
    }})
    db.analytics.insert_one({'type': 'completed', 'data': {
        'petsafe': get_completed('petsafe'),
        'sportdog': get_completed('sportdog'),
    }})
    db.analytics.insert_one({'type': 'feedback_types', 'data': {
        'petsafe': get_feedback_types('petsafe'),
        'sportdog': get_feedback_types('sportdog'),
    }})
    db.analytics.insert_one({'type': 'website_rating', 'data': {
        'petsafe': get_website_rating('petsafe'),
        'sportdog': get_website_rating('sportdog'),
    }})
    db.analytics.insert_one({'type': 'product_rating', 'data': {
        'petsafe': get_product_rating('petsafe'),
        'sportdog': get_product_rating('sportdog'),
    }})
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


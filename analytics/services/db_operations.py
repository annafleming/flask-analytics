from .. import db
from ..helpers.datetime_helper import get_timestamp


def insert_analytics(data):
    if type(data) is list:
        db.analytics.insert_many(data)
    else:
        db.analytics.insert_one(data)


def remove_analytics():
    db.analytics.delete_many({})


def fetch_analytics(key):
    entry = db.analytics.find_one({'type': key})
    if not entry:
        return ''
    else:
        return entry['data']


def update_timestamp(key):
    timestamp = get_timestamp()
    db.timestamps.insert_one({'type': key, 'data': timestamp})
    return timestamp


def fetch_timestamp(key):
    entry = db.timestamps.find_one({'type': key})
    if not entry:
        return ''
    else:
        return entry['data']


def insert_surveys(data):
    if type(data) is list:
        db.surveys.insert_many(data)
    else:
        db.surveys.insert_one(data)


def fetch_last_survey(site, survey_type):
    return db.surveys.find_one({"$query": {'site': site, 'survey_type': survey_type},
                                "$orderby": {"$natural": -1}})


def fetch_surveys(site_name=None, survey_type=None):
    query = {}
    if site_name:
        query['site'] = site_name
    if survey_type:
        query['survey_type'] = survey_type
    return db.surveys.find(query, {'_id': 0})

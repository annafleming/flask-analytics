from .. import db


def insert_analytics(data):
    db.analytics.insert_one(data)


def remove_analytics():
    db.analytics.delete_many({})
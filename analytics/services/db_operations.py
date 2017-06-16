from .. import db


def insert_analytics(data):
    if type(data) is list:
        db.analytics.insert_many(data)
    else:
        db.analytics.insert_one(data)



def remove_analytics():
    db.analytics.delete_many({})
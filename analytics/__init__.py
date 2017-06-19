import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from pymongo import MongoClient
from .config import config_by_name

client = MongoClient('db', 27017)
db = client.analytics
toolbar = DebugToolbarExtension()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .charts import charts as charts_blueprint
    app.register_blueprint(charts_blueprint, url_prefix='/charts')

    from .refresh import refresh as refresh_blueprint
    app.register_blueprint(refresh_blueprint, url_prefix='/refresh')

    from .responses import responses as responses_blueprint
    app.register_blueprint(responses_blueprint, url_prefix='/responses')

    return app


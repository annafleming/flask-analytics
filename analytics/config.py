import os
from .env_config import ENV
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = ENV['SECRET_KEY']
    QUALTRICS_API_TOKEN = ENV['QUALTRICS_API_TOKEN']
    SURVEY_IDS = ENV['SURVEY_IDS']
    QUALTRICS_DATA_CENTER_ID = ENV['QUALTRICS_DATA_CENTER_ID']
    DEBUG = False
    PETSAFE_APP = 'petsafe'
    SPORTDOG_APP = 'sportdog'
    VOC_SURVEY ='voc'
    COMMENT_CARD_SURVEY = 'cc'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "localhost"


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)
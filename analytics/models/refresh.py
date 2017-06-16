from ..models import dataset_operations
from analytics.config import Config
from .stats import get_summary, get_finished, get_completed, get_feedback_types, get_website_rating, get_product_rating
from ..services import db_operations, qualtrics_api


def refresh_all():
    qualtrics_api.import_surveys()
    dataset_operations.save_survey_entries()
    db_operations.remove_analytics()
    db_operations.insert_analytics([
        {'type': 'summary', 'data': get_summary([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'finished', 'data': get_finished([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'completed', 'data': get_completed([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'feedback_types', 'data': get_feedback_types([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'website_rating', 'data': get_website_rating([Config.PETSAFE_APP, Config.SPORTDOG_APP])},
        {'type': 'product_rating', 'data': get_product_rating([Config.PETSAFE_APP, Config.SPORTDOG_APP])}])
    return str(db_operations.update_timestamp('updated_analytics'))


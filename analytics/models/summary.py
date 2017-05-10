from .csv_loader import load_dataset
from .dataset_operations import merge_datasets_by_fields, get_entries_after
from .datetime_operations import subtract_from_today_days
from ..config import Config


def get_summary(site_name):
    columns = ['EndDate', 'WebsiteRating', 'ProductRating']
    voc_dataset = load_dataset(site_name, Config.VOC_SURVEY, columns)
    cc_dataset = load_dataset(site_name, Config.COMMENT_CARD_SURVEY, columns)

    merged_dataset = merge_datasets_by_fields(voc_dataset, cc_dataset, ['EndDate'])
    merged_dataset = get_entries_after(merged_dataset, subtract_from_today_days(7), 'EndDate')

    return {
        'week': {
            'reviews': len(merged_dataset),
            'promoters': 99,
            'passives': 99,
            'detractors': 99
        },
        'month': {
            'reviews': 99,
            'promoters': 99,
            'passives': 99,
            'detractors': 99
        },
    }


def addition(a, b):
    return a + b
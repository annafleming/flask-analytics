from .dataset_loader import load_dataset, get_combined_dataset
from ..helpers.dataset_helper import merge_datasets_vertically, get_entries_after, merge_columns
from ..helpers.datetime_helper import subtract_from_today_days
from ..config import Config
from ..models.column_format import change_column_scale


def get_summary(site_name):
    summary = {'week': {}, 'month': {}}

    merged_dataset = get_combined_dataset(site_name, ['EndDate', 'WebsiteRating', 'ProductRating'])
    merged_dataset = get_entries_after(merged_dataset, subtract_from_today_days(30), 'EndDate')
    merged_dataset['Rating'] = _get_unified_rating_column(merged_dataset)
    summary['month'] = _fill_summary_values(merged_dataset)
    merged_dataset = get_entries_after(merged_dataset, subtract_from_today_days(7), 'EndDate')
    summary['week'] = _fill_summary_values(merged_dataset)

    return summary


def _fill_summary_values(dataset):
    return {
        'reviews': len(dataset),
        'promoters': len(dataset[dataset['Rating'] == 3]),
        'passives': len(dataset[dataset['Rating'] == 2]),
        'detractors': len(dataset[dataset['Rating'] == 1]),
    }


def _get_unified_rating_column(dataset):
    dataset['WebsiteRating'] = change_column_scale(dataset['WebsiteRating'])
    dataset['ProductRating'] = change_column_scale(dataset['ProductRating'])
    return merge_columns(dataset, ['WebsiteRating', 'ProductRating'])

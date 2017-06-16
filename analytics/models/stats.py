from .dataset_loader import get_combined_dataset
from ..helpers import dataset_helper, datetime_helper


def get_summary(sites):
    result = dict()
    for site in sites:
        dataset = get_combined_dataset(site, ['EndDate', 'WebsiteRating', 'ProductRating'])
        dataset = dataset_helper.get_entries_after(dataset, datetime_helper.subtract_from_today_days(30), 'EndDate')
        dataset['Rating'] = _get_unified_rating_column(dataset)
        summary = dict()
        summary['month'] = _fill_summary_values(dataset)
        dataset = dataset_helper.get_entries_after(dataset, datetime_helper.subtract_from_today_days(7), 'EndDate')
        summary['week'] = _fill_summary_values(dataset)
        result[site] = summary
    return result


def _get_unified_rating_column(dataset):
    dataset['WebsiteRating'] = dataset_helper.change_column_scale(dataset['WebsiteRating'])
    dataset['ProductRating'] = dataset_helper.change_column_scale(dataset['ProductRating'])
    return dataset_helper.merge_columns(dataset, ['WebsiteRating', 'ProductRating'])


def _fill_summary_values(dataset):
    return {
        'reviews': len(dataset),
        'promoters': len(dataset[dataset['Rating'] == 3]),
        'passives': len(dataset[dataset['Rating'] == 2]),
        'detractors': len(dataset[dataset['Rating'] == 1]),
    }
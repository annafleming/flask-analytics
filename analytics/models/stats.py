from .dataset_loader import get_combined_dataset
from ..helpers import dataset_helper, datetime_helper


def get_summary(sites):
    result = {}
    for site in sites:
        dataset = get_combined_dataset(site, ['EndDate', 'WebsiteRating', 'ProductRating'])
        dataset = dataset_helper.get_entries_after(dataset, datetime_helper.subtract_from_today_days(30), 'EndDate')
    return result
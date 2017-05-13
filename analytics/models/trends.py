from .csv_loader import load_dataset, get_combined_dataset
from ..helpers.datetime_helper import get_beginning_of_the_month

def get_finished(site_name):
    merged_dataset = get_combined_dataset(site_name, ['EndDate', 'Finished'])
    merged_dataset['EndDate'] = get_beginning_of_the_month(merged_dataset['EndDate'],
                                                           format_in="%Y-%m-%d %H:%M:%S",
                                                           format_out="%Y-%m-%d")
    result = {
        'totals': [],
        'proportion': []
    }
    return result

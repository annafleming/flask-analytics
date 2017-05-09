import pandas as pd
import numpy as np
import datetime
from .csv_loader import load_dataset


def get_summary(site_name):
    voc_dataset = load_dataset(site_name, 'voc')
    cc_dataset = load_dataset(site_name, 'cc')

    merged_dataset = merge_datasets_by_fields(voc_dataset, cc_dataset, ['EndDate'])
    merged_dataset = get_entries_after(merged_dataset, get_beginning_of_the_week_date())

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


def get_entries_after(dataset, start_date):
    return dataset[dataset['EndDate'] >= start_date]


def merge_datasets_by_fields(ds1, ds2, fields):
    return pd.concat([ds1[fields], ds2[fields]], axis=0)


def get_beginning_of_the_week_date():
    beginning_of_the_week = datetime.datetime.now() - datetime.timedelta(days=7)
    return beginning_of_the_week.strftime("%Y-%m-%d 00:00:00")


def addition(a, b):
    return a + b
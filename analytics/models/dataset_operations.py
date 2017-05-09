import pandas as pd


def get_entries_after(dataset, start_date):
    return dataset[dataset['EndDate'] >= start_date]


def merge_datasets_by_fields(ds1, ds2, fields):
    return pd.concat([ds1[fields], ds2[fields]], axis=0)


import pandas as pd


def get_entries_after(dataset, start_date, field_name):
    return dataset[dataset[field_name] >= start_date]


def merge_datasets_by_fields(ds1, ds2, columns):
    return pd.concat([ds1[columns], ds2[columns]], axis=0)


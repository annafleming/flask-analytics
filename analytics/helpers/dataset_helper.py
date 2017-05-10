import pandas as pd


def get_entries_after(dataset, start_date, field_name):
    return dataset[dataset[field_name] >= start_date]


def merge_datasets_vertically(ds1, ds2):
    return pd.concat([ds1, ds2], axis=0)


def rename_columns(dataset, column_names):
    return dataset.rename(columns=column_names)


def filter_columns(dataset, columns):
    return dataset[columns]


def add_colums_if_not_exist(dataset, columns):
    for name in columns:
        if name not in dataset:
            dataset[name] = ''
    return dataset
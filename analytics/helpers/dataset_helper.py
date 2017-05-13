import pandas as pd


def get_entries_after(dataset, start_date, field_name):
    if field_name not in dataset.columns:
        raise Exception('Column %s is missing in the dataset' % field_name)
    return dataset[dataset[field_name] >= start_date]


def merge_datasets_vertically(ds1, ds2):
    return pd.concat([ds1, ds2], axis=0)


def rename_columns(dataset, column_names):
    return dataset.rename(columns=column_names)


def filter_columns(dataset, columns):
    dataset_columns = set(dataset.columns)
    if not (set(columns)).issubset(dataset_columns):
        raise Exception('Column(s) are missing in the dataset')
    return dataset[columns]


def add_columns_if_not_exist(dataset, columns):
    for name in columns:
        if name not in dataset:
            dataset[name] = None
    return dataset


def lambda_get_first_present_value(row, columns):
    for column in columns:
        if not pd.isnull(row[column]) and row[column]:
            return row[column]
    return row[columns[-1]]


def merge_columns(dataset, columns):
    return dataset.apply(lambda x: lambda_get_first_present_value(x, columns), axis=1)

import pandas as pd
from ..models.dataset_settings import column_types, column_scale


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


def trim_heading_rows(dataset, rows):
    if len(dataset) < rows:
        raise Exception('Dataset length is less then the number of rows to remove')
    return dataset[rows:]


def drop_rows_with_missing_data(dataset):
    return dataset.dropna(axis=0)


def count_values_by_grouping(ds, group_by, value_column):
    grouped_ds = ds.groupby(group_by).size().reset_index()
    grouped_ds.rename(columns={0: value_column}, inplace=True)
    return grouped_ds


def merge_datasets_horizontally(ds1, ds2, column, how, na_values):
    result_ds = pd.merge(ds1, ds2, on=column, how=how)
    return result_ds.fillna(na_values)


def count_values_grouped_by_column(dataset, group_by, value_column, count_values, count_proportion):
    count_ds = count_values_by_grouping(dataset[dataset[value_column] == count_values], group_by, value_column)
    total_ds = count_values_by_grouping(dataset, group_by, 'Total')
    result_ds = merge_datasets_horizontally(count_ds, total_ds, column=group_by, how='outer', na_values=0)
    result_ds['Total'] = result_ds['Total'].astype('int64')
    result_ds[value_column] = result_ds[value_column].astype('int64')
    if count_proportion:
        result_ds['Proportion'] = (result_ds[value_column] / result_ds['Total']) * 100
        result_ds['Proportion'] = result_ds['Proportion'].apply(lambda x: float("{0:.2f}".format(x)))
    return result_ds


def get_dataset_column_types(ds):
    return dict(ds.dtypes)


def set_column_types(ds, columns):
    if not set(columns).issubset(set(column_types.keys())):
        raise Exception('Column(s) are missing from types dictionary')
    for column in columns:
        if column_types[column] == 'bool':
            bool_conversion = {'True': True, 'False': False,
                               True: True, False: False,
                               'Yes': True, 'No': False,
                               1: True, 0: False,
                               '1': True, '0': False}
            ds[column] = convert_column_values(ds[column], bool_conversion)
        else:
            ds[column] = ds[column].astype(column_types[column])
    return ds


def convert_column_values(column, settings):
    return column.map(settings)


def lambda_fill_count_values(row, column):
    row[row[column]] = 1
    return row


def count_column_values_frequency(dataset, key_column, values_column):
    agg_dataset = dataset.pivot_table(index=[key_column],
                                      columns=values_column,
                                      aggfunc=len,
                                      fill_value=0).reset_index()
    agg_dataset.columns.name = None
    return agg_dataset


def count_average_value_in_row(ds, column_weights):
    column_names = list(set(list(column_weights.keys())) & set(ds.columns))
    ds['Average'] = 0
    for column in column_weights:
        if column in ds:
            ds['Average'] = ds['Average'] + column_weights[column] * ds[column]
    ds['Average'] = ds['Average'] / ds[column_names].sum(axis=1)
    ds['Average'] = ds['Average'].apply(lambda x: float("{0:.2f}".format(x)))

    return ds['Average']


def change_column_scale(column):
    if column.name not in column_scale:
        raise Exception('Scale settings are missing for the column %s' % column.name)

    settings = column_scale[column.name]

    if 'Default' not in settings:
        raise Exception('Default value is missing in settings')
    return column.apply(lambda x: settings[x] if x in settings else settings['Default'])
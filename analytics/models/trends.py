from .csv_loader import load_dataset, get_combined_dataset
from ..helpers.datetime_helper import get_beginning_of_the_month, get_range_of_month
from ..helpers.dataset_helper import count_values_grouped_by_column, set_column_types
from .settings import Config


def get_finished(site_name):
    merged_dataset = get_combined_dataset(site_name, ['EndDate', 'Finished'])
    return calculate_proportions_by_month(merged_dataset, 'EndDate', 'Finished')


def get_completed(site_name):
    ds = load_dataset(site_name, Config.VOC_SURVEY, ['EndDate', 'CompletedPurpose'])
    return calculate_proportions_by_month(ds, 'EndDate', 'CompletedPurpose')


def fill_values_if_monthly_data_is_missing(ds, date_column, format, values):
    date_range = get_range_of_month(ds[date_column].min(), ds[date_column].max(), format)
    for date_value in date_range:
        if len(ds[ds[date_column] == date_value]) == 0:
            row_dict = values
            row_dict[date_column] = date_value
            ds = ds.append(row_dict, ignore_index=True)
    return ds


def calculate_proportions_by_month(ds, date_column, value_column):
    ds[date_column] = get_beginning_of_the_month(ds[date_column], format_in="%Y-%m-%d %H:%M:%S",
                                                 format_out="%Y-%m-%d")
    ds = set_column_types(ds, [value_column])
    ds = count_values_grouped_by_column(ds, date_column, value_column, True, True)
    ds = fill_values_if_monthly_data_is_missing(ds,
                                                date_column, "%Y-%m-%d",
                                                {value_column: 0, 'Total': 0, 'Proportion': 0.0})
    ds.sort_values(date_column, inplace=True)
    return {
        'Keys': ds[date_column].tolist(),
        value_column: ds[value_column].tolist(),
        'Total': ds['Total'].tolist(),
        'Proportion': ds['Proportion'].tolist(),
    }

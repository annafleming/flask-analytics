from .csv_loader import load_dataset, get_combined_dataset
from ..helpers.datetime_helper import get_beginning_of_the_month, get_range_of_month
from ..helpers.dataset_helper import count_values_grouped_by_column, set_column_types


def get_finished(site_name):
    merged_dataset = get_combined_dataset(site_name, ['EndDate', 'Finished'])
    merged_dataset['EndDate'] = get_beginning_of_the_month(merged_dataset['EndDate'],
                                                           format_in="%Y-%m-%d %H:%M:%S",
                                                           format_out="%Y-%m-%d")
    merged_dataset = set_column_types(merged_dataset, ['Finished'])
    merged_dataset = count_values_grouped_by_column(merged_dataset, 'EndDate', 'Finished', True, True)
    merged_dataset = fill_values_if_monthly_data_is_missing(merged_dataset, 'EndDate', "%Y-%m-%d", {'Finished': 0, 'Total': 0, 'Proportion': 0.0})
    merged_dataset.sort_values('EndDate', inplace=True)

    result = {
        'keys': merged_dataset['EndDate'].tolist(),
        'finished': merged_dataset['Finished'].tolist(),
        'total': merged_dataset['Total'].tolist(),
        'proportion': merged_dataset['Proportion'].tolist(),
    }
    return result


def fill_values_if_monthly_data_is_missing(ds, date_column, format, values):
    date_range = get_range_of_month(ds[date_column].min(), ds[date_column].max(), format)
    for date_value in date_range:
        if len(ds[ds[date_column] == date_value]) == 0:
            row_dict = values
            row_dict[date_column] = date_value
            ds = ds.append(row_dict, ignore_index=True)
    return ds

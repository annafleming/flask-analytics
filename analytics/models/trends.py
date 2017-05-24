from .csv_loader import load_dataset, get_combined_dataset
from ..helpers.datetime_helper import get_beginning_of_the_month, get_range_of_month, convert_date_column
from ..helpers.dataset_helper import count_values_grouped_by_column, set_column_types, count_column_values_frequency, count_average_value_in_row
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
    ds[date_column] = convert_date_column(ds[date_column], format_in="%Y-%m-%d", format_out="%b %y")

    return {
        'Keys': ds[date_column].tolist(),
        value_column: ds[value_column].tolist(),
        'Total': ds['Total'].tolist(),
        'Proportion': ds['Proportion'].tolist(),
    }


def get_feedback_types(site_name):
    merged_dataset = get_combined_dataset(site_name, ['EndDate', 'FeedbackType'])
    merged_dataset['EndDate'] = get_beginning_of_the_month(merged_dataset['EndDate'],
                                                           format_in="%Y-%m-%d %H:%M:%S",
                                                           format_out="%Y-%m-%d")
    result_ds = count_column_values_frequency(merged_dataset, 'EndDate', 'FeedbackType')
    result_ds['Products'] = result_ds['Products'] + result_ds['Product(s)']
    result_ds.drop(['Product(s)'], axis=1, inplace=True)
    result_ds.sort_values('EndDate', inplace=True)
    return {
        'Keys': result_ds['EndDate'].tolist(),
        'Website Experience': result_ds['Website Experience'].tolist(),
        'Products': result_ds['Products'].tolist(),
    }


def get_website_rating(site_name):
    merged_dataset = get_combined_dataset(site_name, ['EndDate', 'WebsiteRating']).dropna(axis=0)
    unique_rating_values = merged_dataset['WebsiteRating'].unique().tolist()
    column_default_values = {column: 0 for column in unique_rating_values}

    merged_dataset['EndDate'] = get_beginning_of_the_month(merged_dataset['EndDate'],
                                                           format_in="%Y-%m-%d %H:%M:%S",
                                                           format_out="%Y-%m-%d")

    result_ds = count_column_values_frequency(merged_dataset, 'EndDate', 'WebsiteRating')
    result_ds = fill_values_if_monthly_data_is_missing(result_ds,
                                                       'EndDate',
                                                       "%Y-%m-%d",
                                                       column_default_values)
    result_ds = result_ds.sort_values('EndDate')
    result_ds['EndDate'] = convert_date_column(result_ds['EndDate'], format_in="%Y-%m-%d", format_out="%b %y")
    result_ds['Average'] = count_average_value_in_row(result_ds, column_weights={
        'Very Bad': 1,
        'Bad': 2,
        'Fair': 3,
        'Good': 4,
        'Very Good': 5,
    })
    result_ds['Average'].fillna(0, inplace=True)
    result = {
        'Keys': result_ds['EndDate'].tolist(),
        'Average': result_ds['Average'].tolist(),
    }

    for column in unique_rating_values:
        result[column] = result_ds[column].tolist()
    return result


def get_product_rating(site_name):
    merged_dataset = get_combined_dataset(site_name, ['EndDate', 'ProductRating']).dropna(axis=0)
    unique_rating_values = merged_dataset['ProductRating'].unique()
    column_default_values = {column: 0 for column in unique_rating_values}

    merged_dataset['EndDate'] = get_beginning_of_the_month(merged_dataset['EndDate'],
                                                           format_in="%Y-%m-%d %H:%M:%S",
                                                           format_out="%Y-%m-%d")

    result_ds = count_column_values_frequency(merged_dataset, 'EndDate', 'ProductRating')
    result_ds = fill_values_if_monthly_data_is_missing(result_ds,
                                                       'EndDate',
                                                       "%Y-%m-%d",
                                                       column_default_values)
    result_ds = result_ds.sort_values('EndDate')
    result = {
        'Keys': result_ds['EndDate'].tolist(),
    }
    for column in unique_rating_values:
        result[str(column)] = result_ds[column].tolist()
    return result

from .dataset_loader import get_combined_dataset, load_dataset_from_db
from ..helpers import dataset_helper, datetime_helper
from analytics.config import Config


def get_summary(sites):
    result = dict()
    for site in sites:
        dataset = get_combined_dataset(site, ['EndDate', 'WebsiteRating', 'ProductRating'])
        dataset = dataset_helper.get_entries_after(dataset, datetime_helper.subtract_from_today_days(30), 'EndDate')
        dataset['Rating'] = _get_unified_rating_column(dataset)
        summary = dict()
        summary['month'] = _fill_summary_values(dataset)
        dataset = dataset_helper.get_entries_after(dataset, datetime_helper.subtract_from_today_days(7), 'EndDate')
        summary['week'] = _fill_summary_values(dataset)
        result[site] = summary
    return result


def get_finished(sites):
    result = dict()
    for site in sites:
        dataset = get_combined_dataset(site, ['EndDate', 'Finished']).dropna(axis=0)
        result[site] = _calculate_proportions_by_month(dataset, 'EndDate', 'Finished')
    return result


def get_completed(sites):
    result = dict()
    for site in sites:
        dataset = load_dataset_from_db(site, Config.VOC_SURVEY, ['EndDate', 'CompletedPurpose']).dropna(axis=0)
        result[site] = _calculate_proportions_by_month(dataset, 'EndDate', 'CompletedPurpose')
    return result


def _get_unified_rating_column(dataset):
    dataset['WebsiteRating'] = dataset_helper.change_column_scale(dataset['WebsiteRating'])
    dataset['ProductRating'] = dataset_helper.change_column_scale(dataset['ProductRating'])
    return dataset_helper.merge_columns(dataset, ['WebsiteRating', 'ProductRating'])


def _fill_summary_values(dataset):
    return {
        'reviews': len(dataset),
        'promoters': len(dataset[dataset['Rating'] == 3]),
        'passives': len(dataset[dataset['Rating'] == 2]),
        'detractors': len(dataset[dataset['Rating'] == 1]),
    }


def _calculate_proportions_by_month(ds, date_column, value_column):
    ds[date_column] = datetime_helper.get_beginning_of_the_month(ds[date_column],
                                                                 format_in="%Y-%m-%d %H:%M:%S",
                                                                 format_out="%Y-%m-%d")
    ds = dataset_helper.set_column_types(ds, [value_column])
    ds = dataset_helper.count_values_grouped_by_column(ds, date_column, value_column, True, True)
    ds = _fill_values_if_monthly_data_is_missing(ds,
                                                 date_column,
                                                 "%Y-%m-%d",
                                                 {value_column: 0, 'Total': 0, 'Proportion': 0.0})
    ds.sort_values(date_column, inplace=True)
    ds[date_column] = datetime_helper.convert_date_column(ds[date_column], format_in="%Y-%m-%d", format_out="%b %y")
    return {
        'Keys': ds[date_column].tolist(),
        value_column: ds[value_column].tolist(),
        'Other': (ds['Total'] - ds[value_column]).tolist(),
        'Proportion': ds['Proportion'].tolist(),
    }


def _fill_values_if_monthly_data_is_missing(ds, date_column, format, values):
    date_range = datetime_helper.get_range_of_month(ds[date_column].min(), ds[date_column].max(), format)
    for date_value in date_range:
        if len(ds[ds[date_column] == date_value]) == 0:
            row_dict = values
            row_dict[date_column] = date_value
            ds = ds.append(row_dict, ignore_index=True)
    return ds


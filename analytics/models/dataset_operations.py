import pandas as pd
from ..config import Config
from .dataset_settings import file_names, column_rename
from ..helpers import dataset_helper
from ..services import csv_adapter, db_operations
from .. import db


def load_dataset_from_csv(site_name, survey_type, columns):
    dataset = csv_adapter.load_dataset_from_csv(file_names[site_name][survey_type])
    dataset = dataset_helper.trim_heading_rows(dataset=dataset, rows=2)
    dataset = dataset_helper.rename_columns(dataset, fetch_original_column_names(site_name, survey_type, columns))
    dataset = dataset_helper.add_columns_if_not_exist(dataset, columns)
    dataset = dataset_helper.filter_columns(dataset, columns)
    return dataset


def load_dataset_from_db(site_name, survey_type, columns):
    dataset = pd.DataFrame(list(db.surveys.find({'site': site_name, 'survey_type': survey_type}, {'_id': 0, 'survey_type': 0, 'site': 0})))
    dataset = dataset_helper.add_columns_if_not_exist(dataset, columns)
    dataset = dataset_helper.filter_columns(dataset, columns)
    return dataset


def fetch_original_column_names(site_name, survey_type, columns):
    columns_set = column_rename[site_name][survey_type]
    return {key: val for key, val in columns_set.items() if val in columns}


def get_combined_dataset(site_name, columns):
    voc_dataset = load_dataset_from_db(site_name, Config.VOC_SURVEY, columns)
    cc_dataset = load_dataset_from_db(site_name, Config.COMMENT_CARD_SURVEY, columns)
    return dataset_helper.merge_datasets_vertically(voc_dataset, cc_dataset)


def save_survey_entries():
    surveys = [
        {'site': Config.PETSAFE_APP, 'survey_type': Config.VOC_SURVEY},
        {'site': Config.PETSAFE_APP, 'survey_type': Config.COMMENT_CARD_SURVEY},
        {'site': Config.SPORTDOG_APP, 'survey_type': Config.VOC_SURVEY},
        {'site': Config.SPORTDOG_APP, 'survey_type': Config.COMMENT_CARD_SURVEY},
    ]
    survey_list = []
    for survey in surveys:
        ds = load_dataset_from_csv(survey['site'],
                                   survey['survey_type'],
                                   list(column_rename[survey['site']][survey['survey_type']].values()))
        for index, row in ds.iterrows():
            data = {'site': survey['site'],
                    'survey_type': survey['survey_type']}
            for column in ds.columns.values.tolist():
                data[column] = row[column]
            survey_list.append(data)
    db_operations.insert_surveys(survey_list)

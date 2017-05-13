import pandas as pd
from ..config import Config
from .settings import file_names, column_rename
from ..helpers import dataset_helper


def load_dataset(site_name, survey_type, columns):
    dataset = pd.read_csv(file_names[site_name][survey_type])
    dataset = dataset_helper.trim_heading_rows(dataset=dataset, rows=2)
    dataset = dataset_helper.rename_columns(dataset, fetch_original_column_names(site_name, survey_type, columns))
    dataset = dataset_helper.add_columns_if_not_exist(dataset, columns)
    dataset = dataset_helper.filter_columns(dataset, columns)
    return dataset


def fetch_original_column_names(site_name, survey_type, columns):
    columns_set = column_rename[site_name][survey_type]
    return {key: val for key, val in columns_set.items() if val in columns}


def get_combined_dataset(site_name, columns):
    voc_dataset = load_dataset(site_name, Config.VOC_SURVEY, columns)
    cc_dataset = load_dataset(site_name, Config.COMMENT_CARD_SURVEY, columns)
    return dataset_helper.merge_datasets_vertically(voc_dataset, cc_dataset)
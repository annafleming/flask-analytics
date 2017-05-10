import pandas as pd

file_names = {
    'petsafe': {
        'voc': 'data/PetSafeVOCSurvey.csv',
        'cc': 'data/PetSafeFeedbackCommentCard.csv'
    },
    'sportdog': {
        'voc': 'data/SportDOGVOCSurvey.csv',
        'cc': 'data/SportDOGFeedbackCommentCard.csv'
    }
}


def load_dataset(site_name, survey_type, columns):
    dataset = pd.read_csv(file_names[site_name][survey_type])
    dataset = trim_heading_rows(dataset=dataset, rows=2)
    # dataset = get_dataset_columns(dataset=dataset, columns=dataset)
    return dataset


def trim_heading_rows(dataset, rows):
    if len(dataset) < rows:
        raise Exception('Dataset length is less then the number of rows to remove')
    return dataset[rows:]


def get_dataset_columns(dataset, columns):
    return 1
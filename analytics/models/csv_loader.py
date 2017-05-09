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


def load_dataset(site_name, survey_type):
    dataset = pd.read_csv(file_names[site_name][survey_type])
    return trim_heading_rows(dataset)


def trim_heading_rows(dataset):
    return dataset[2:]

import pandas as pd


def load_dataset_from_csv(file_path):
    return pd.read_csv(file_path)
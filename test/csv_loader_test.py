import unittest
from unittest.mock import patch
import analytics
import pandas as pd


class CsvLoaderTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_trim_heading_rows_if_greater_then_dataset_length(self):
        rows_number = 2
        ds = pd.DataFrame([["2017-05-07"], ["2017-05-08"], ["2017-05-09"]], columns=['EndDate'])
        trimmed_ds = analytics.models.csv_loader.trim_heading_rows(ds, rows_number)
        self.assertEqual(len(trimmed_ds), 1)

    def test_should_raise_exception_if_amount_of_rows_to_remove_greater_dataset_lenth(self):
        rows_number = 4
        ds = pd.DataFrame([["2017-05-07"], ["2017-05-08"], ["2017-05-09"]], columns=['EndDate'])
        self.assertRaises(Exception, analytics.models.csv_loader.trim_heading_rows, ds, rows_number)

    def fake_read_csv(self):
        return pd.DataFrame([["2017-05-07"], ["2017-05-08"], ["2017-05-09"]], columns=['EndDate'])

    def fake_trim_heading_rows(dataset, rows):
        return dataset

    @patch('analytics.models.csv_loader.file_names', { 'test': {'voc': 'data/sample.csv'}})
    @patch('analytics.models.csv_loader.pd.read_csv', fake_read_csv)
    @patch('analytics.models.csv_loader.trim_heading_rows', fake_trim_heading_rows)
    def test_should_load_dataset_with_existing_key(self):
        ds = analytics.models.csv_loader.load_dataset('test', 'voc', [])
        self.assertEqual(len(ds), 3)

    @patch('analytics.models.csv_loader.file_names', {'test': {'somekey': 'data/sample.csv'}})
    def test_should_raise_exception_if_config_key_does_not_exist(self):
        self.assertRaises(Exception, analytics.models.csv_loader.load_dataset, 'test', 'voc', [])


    if __name__ == '__main__':
        unittest.main()

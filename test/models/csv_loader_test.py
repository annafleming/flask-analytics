import unittest
from unittest.mock import patch
import analytics
import pandas as pd


class CsvLoaderTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    @patch('analytics.models.csv_loader.file_names', {'test': {'somekey': 'data/sample.csv'}})
    def test_should_raise_exception_if_config_key_does_not_exist(self):
        self.assertRaises(Exception, analytics.models.csv_loader.load_dataset, 'test', 'voc', [])

    @patch('analytics.models.csv_loader.column_rename', {'test': {'voc': {'C1': 'Date', 'C2': 'Type', 'C3': 'Exclude'}}})
    def test_should_fetch_original_column_names_for_dataset(self):
        original_column_names = analytics.models.csv_loader.fetch_original_column_names('test', 'voc', ['Date', 'Type'])
        self.assertEqual(original_column_names, {'C1': 'Date', 'C2': 'Type'})

    if __name__ == '__main__':
        unittest.main()


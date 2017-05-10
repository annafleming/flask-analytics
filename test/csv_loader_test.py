import unittest
import analytics
import pandas as pd


class CsvLoaderTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_trim_heading_rows(self):
        rows_number = 2
        ds = pd.DataFrame([["2017-05-07"], ["2017-05-08"], ["2017-05-09"]], columns=['EndDate'])
        trimmed_ds = analytics.models.csv_loader.trim_heading_rows(ds, rows_number)
        self.assertEqual(len(trimmed_ds), 1)


    if __name__ == '__main__':
        unittest.main()

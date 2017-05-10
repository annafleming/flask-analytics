import unittest
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




    if __name__ == '__main__':
        unittest.main()

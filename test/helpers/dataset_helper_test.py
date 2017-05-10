import unittest
import analytics
import pandas as pd
import datetime


class DatasetHelperTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_should_merge_datasets_vertically(self):
        df1 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']], columns=['letter', 'number', 'animal'])
        df2 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
        merged = analytics.helpers.dataset_helper.merge_datasets_vertically(df1, df2)
        self.assertEquals(len(merged), 4)

    def test_should_get_entries_after_date(self):
        df = pd.DataFrame([["2017-05-07"], ["2017-05-08"], ["2017-05-09"]], columns=['EndDate'])
        filter_date = datetime.datetime(2017, 5, 8).strftime('%Y-%m-%d')
        filtered_ds = analytics.helpers.dataset_helper.get_entries_after(df, filter_date, 'EndDate')
        self.assertEquals(len(filtered_ds), 2)

    if __name__ == '__main__':
        unittest.main()

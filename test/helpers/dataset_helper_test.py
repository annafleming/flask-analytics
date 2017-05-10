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

    def test_should_rename_columns(self):
        df = pd.DataFrame([["2017-05-07"], ["2017-05-08"], ["2017-05-09"]], columns=['EndDate'])
        renamed_dataset = analytics.helpers.dataset_helper.rename_columns(df, {'EndDate': 'NewEndDate'})
        self.assertIn('NewEndDate', renamed_dataset.columns.values)
        self.assertNotIn('EndDate', renamed_dataset.columns.values)

    def test_should_filter_requested_columns(self):
        df = pd.DataFrame([["2017-05-07", 'Type1', 'True'], ["2017-05-08", 'Type2', 'False']], columns=['Date', 'Type', 'Exclude'])
        filtered_dataset = analytics.helpers.dataset_helper.filter_columns(df, ['Date', 'Type'])
        self.assertIn('Date', filtered_dataset.columns.values)
        self.assertIn('Type', filtered_dataset.columns.values)
        self.assertNotIn('Exclude', filtered_dataset.columns.values)

    def test_should_add_columns_if_not_exist(self):
        columns = ['Date', 'Type', 'Exclude']
        df = pd.DataFrame([["2017-05-07", 'Type1'], ["2017-05-08", 'Type2']], columns=['Date', 'Type'])
        analytics.helpers.dataset_helper.add_colums_if_not_exist(df, columns)
        self.assertIn('Date', df.columns.values)
        self.assertIn('Type', df.columns.values)
        self.assertIn('Exclude', df.columns.values)


    if __name__ == '__main__':
        unittest.main()

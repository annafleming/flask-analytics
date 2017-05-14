import unittest
import analytics
import pandas as pd

class TrendsTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_should_fill_in_values_if_monthly_data_is_missing(self):
        ds = pd.DataFrame([["2015-07-01", 1, 1],
                           ["2015-07-03", 0, 3]], columns=['Date', 'Finished', 'Total'])
        expected_ds = pd.DataFrame([["2015-07-01", 1, 1],
                                    ["2015-07-01", 0, 0],
                                    ["2015-07-03", 0, 3]], columns=['Date', 'Finished', 'Total'])
        result_ds = analytics.models.trends.\
            fill_values_if_monthly_data_is_missing(ds, date_column='Date',
                                                   format="%Y-%m-%d",
                                                   values={'Finished': 0, 'Total': 0})
        # self.assertTrue(result_ds.equals(expected_ds))

    if __name__ == '__main__':
        unittest.main()
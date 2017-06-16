import unittest
import analytics
import pandas as pd


class StatsTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_get_summary(self):
        summary = analytics.models.stats.get_summary(['sportdog'])
        self.assertIn('week', summary['sportdog'])
        self.assertIn('month', summary['sportdog'])

    def test_should_fill_in_values_if_monthly_data_is_missing(self):
        ds = pd.DataFrame([["2015-07-01", 1, 1],
                           ["2015-09-01", 0, 3]], columns=['Date', 'Finished', 'Total'])
        expected_ds = pd.DataFrame([["2015-07-01", 1, 1],
                                    ["2015-09-01", 0, 3],
                                    ["2015-08-01", 0, 0]], columns=['Date', 'Finished', 'Total'])
        result_ds = analytics.models.stats. \
            _fill_values_if_monthly_data_is_missing(ds, date_column='Date',
                                                    format="%Y-%m-%d",
                                                    values={'Finished': 0, 'Total': 0})
        self.assertTrue(result_ds.equals(expected_ds))

    if __name__ == '__main__':
        unittest.main()

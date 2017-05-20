import unittest
import analytics
from freezegun import freeze_time
import datetime
import pandas as pd


class DatetimeHelperTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_should_subtract_from_today_days(self):
        with freeze_time("2017-05-09"):
            self.assertEqual(analytics.helpers.datetime_helper.subtract_from_today_days(7),
                             datetime.datetime(2017, 5, 2).strftime('%Y-%m-%d %H:%M:%S'))

    def test_should_set_date_to_the_beginning_of_the_month(self):
        ds = pd.DataFrame([["2017-05-07 10:00:28"], ["2017-05-08 10:00:28"], ["2017-05-09 10:00:28"]], columns=['EndDate'])
        series_normalised = analytics.helpers.datetime_helper.get_beginning_of_the_month(ds['EndDate'])
        self.assertEqual(series_normalised.tolist(), ["2017-05-01", "2017-05-01", "2017-05-01"])

    def test_should_set_date_to_the_beginning_of_the_month_for_any_format(self):
        ds = pd.DataFrame([["2017-05-07"], ["2017-05-08"], ["2017-05-09"]], columns=['EndDate'])
        series_normalised = analytics.helpers\
            .datetime_helper. \
            get_beginning_of_the_month(ds['EndDate'], format_in="%Y-%m-%d", format_out="%Y-%m-%d %H:%M:%S")
        self.assertEqual(series_normalised.tolist(), ["2017-05-01 00:00:00", "2017-05-01 00:00:00",
                                                      "2017-05-01 00:00:00"])

    def test_should_return_of_months(self):
        date_range = analytics.helpers.\
            datetime_helper.get_range_of_month(start_date="2017-01-01",
                                               end_date="2017-07-01",
                                               format="%Y-%m-%d")
        expected_range = ["2017-01-01", "2017-02-01", "2017-03-01",
                          "2017-04-01", "2017-05-01", "2017-06-01", "2017-07-01"]
        self.assertEqual(date_range, expected_range)

    def test_should_convert_date_column_to_passed_format(self):
        ds = pd.DataFrame([["2017-05-01"], ["2017-06-01"], ["2017-07-01"]], columns=['EndDate'])
        expected_ds = pd.DataFrame([["May 17"], ["Jun 17"], ["Jul 17"]], columns=['EndDate'])
        ds['EndDate'] = analytics.helpers.datetime_helper.\
            convert_date_column(ds['EndDate'], format_in="%Y-%m-%d", format_out="%b %y")
        self.assertTrue(ds.equals(expected_ds))

    if __name__ == '__main__':
        unittest.main()
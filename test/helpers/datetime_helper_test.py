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

    if __name__ == '__main__':
        unittest.main()
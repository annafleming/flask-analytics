import unittest
import analytics
from freezegun import freeze_time
import datetime


class DatetimeOperationsTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_should_subtract_from_today_days(self):
        with freeze_time("2017-05-09"):
            self.assertEqual(analytics.models.datetime_operations.subtract_from_today_days(7),
                             datetime.datetime(2017, 5, 2).strftime('%Y-%m-%d %H:%M:%S'))

    if __name__ == '__main__':
        unittest.main()
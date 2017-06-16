import unittest
import analytics


class StatsTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_get_summary(self):
        summary = analytics.models.stats.get_summary(['sportdog'])
        self.assertIn('week', summary['sportdog'])
        self.assertIn('month', summary['sportdog'])

    if __name__ == '__main__':
        unittest.main()
import unittest
import analytics

class SummaryTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_get_summary(self):
        summary = analytics.models.summary.get_summary('sportdog')
        self.assertIn('week', summary)
        self.assertIn('month', summary)


    if __name__ == '__main__':
        unittest.main()
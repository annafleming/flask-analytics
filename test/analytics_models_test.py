import unittest
import analytics


class AnalyticsModelsTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    def test_addition(self):
        result = analytics.models.addition(2, 3)
        self.assertEqual(result, 5)

    if __name__ == '__main__':
        unittest.main()
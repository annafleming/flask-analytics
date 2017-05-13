import unittest
import analytics


class TrendsTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    # def test_get_trends(self):
    #     self.assertEqual(2, 3)

    if __name__ == '__main__':
        unittest.main()
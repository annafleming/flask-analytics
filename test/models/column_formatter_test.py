import unittest
import analytics

class ColumnFormatterTest(unittest.TestCase):
    def setUp(self):
        self.app = analytics.create_app('test')

    if __name__ == '__main__':
        unittest.main()
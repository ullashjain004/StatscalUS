import unittest
from CsvReader.CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('Tests/Data/StatsData.csv')

    def test_csv_file(self):
        test_data = CsvReader('Tests/Data/StatsData.csv').data
        lst = []
        p = 0
        for row in test_data:
            p = p + 1
            y = int(row['PopData'])
            lst.append(y)
        self.assertEqual(p, 200)

if __name__ == '__main__':
    unittest.main()
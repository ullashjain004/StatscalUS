import unittest
from Statistics.Statistics import Statistics
from CsvReader.CsvReader import CsvReader
from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics('Tests/Data/StatsData.csv')

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Pop_Mean_calculator(self):
        test_mean_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data  
        dataset = []
        for row in test_mean_data:
            a = int(row['PopData'])
            dataset.append(a)
        for column in answer:
            result = float((column['Mean']))
        self.assertEqual(self.statistics.mean(dataset), result)



    # def test_Median_calculator(self):
    #     test_data = CsvReader('Tests/Data/StatsData.csv').data
    #     answer = CsvReader('Tests/Data/StataDataAns.csv').data
    #     dataset = []
    #     for row in test_data:
    #         x = int(row['PopData'])
    #         dataset.append(x)
    #     for column in answer:
    #         result = float((column['Median']))
    #     self.assertEqual(self.statistics.median(dataset), result)



if __name__ == '__main__':
    unittest.main()
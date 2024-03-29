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



    def test_Mode_calculator(self):
        test_mode_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_mode_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Mode'])
        self.assertEqual(self.statistics.mode(dataset), result)



    def test_Median_calculator(self):
        test_median_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_median_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Median'])
        self.assertEqual(self.statistics.median(dataset), result)



    def test_popstddev_calculator(self):
        test_popstd_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_popstd_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Pop_Std'])
        self.assertEqual(self.statistics.pop_stddev(dataset), result)


    def test_sample_stddev_calculator(self):
        test_sample_stddev_data = CsvReader('Tests/Data/StatsData.csv').data
        dataset = []
        for row in test_sample_stddev_data:
            a = int(row['PopData'])
            dataset.append(a)
            p, q = self.statistics.samplestddev(dataset)
            p = round(p,3)
            q = round(q,3)
            self.assertEqual(p, q)


    def test_sample_mean_calculator(self):
        test_sample_data = CsvReader('Tests/Data/StatsData.csv').data
        dataset = []
        for row in test_sample_data:
            a = int(row['PopData'])
            dataset.append(a)
            p, q = self.statistics.samplemean(dataset)
            self.assertEqual(p, q)

    def test_popvar_calculator(self):
        test_popvar_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        dataset = []
        for row in test_popvar_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Pop_Var'])
        self.assertEqual(self.statistics.pop_variance(dataset), result)

    def test_confi_int_calculator(self):
        test_confiint_data = CsvReader('Tests/Data/StatCalcData.csv').data
        val = data_add(test_confiint_data)
        confidence = 95
        self.assertEqual(self.statistics.pop_confi_int(val, confidence), (131.0783, 156.631))
        self.assertNotEqual(self.statistics.pop_confi_int(val, confidence), (132.578, 163.0283), "Incorrect Confidence Interval")


    def test_popZScore_calculator(self):
        test_popzscore_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/Zscore.csv').data
        dataset = []
        for row in test_popzscore_data:
            x = int(row['PopData'])
            dataset.append(x)
            dataset1 = []
        for row in answer:
            result = float(row['Zscore'])
            dataset1.append(result)
        self.assertEqual(self.statistics.pop_z_score(dataset), dataset1)


    def test_Var_Pop_prop_calculator(self):
        test_pop_prop_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        for row in test_pop_prop_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Var_Prop'])
            self.assertEqual(self.statistics.proportion(dataset), result)



    def test_popcorrcoeff_calculator(self):
        test_popcorrcoeff_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/data.csv').data
        dataset = []
        for row in test_popcorrcoeff_data:
            x = int(row['PopData'])
            dataset.append(x)
            dataset1 = []
        for row in answer:
            result = float(row['Result'])
            dataset1.append(result)
        self.assertEqual(self.statistics.popcorrcoeff(dataset), dataset1)

    def test_prop_calculator(self):
        test_prop_data = CsvReader('Tests/Data/StatsData.csv').data
        answer = CsvReader('Tests/Data/StataDataAns.csv').data
        for row in test_prop_data:
            x = int(row['PopData'])
            dataset.append(x)
        for column in answer:
            result = float(column['Proportion'])
            self.assertEqual(self.statistics.proportion(dataset), result)



if __name__ == '__main__':
    unittest.main()
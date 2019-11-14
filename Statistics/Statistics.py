from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from CsvReader.CsvReader import CsvReader
from Statistics.Mode import mode
from Statistics.StandardDeviation import stddev
class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/StatsData.csv')
        super().__init__()

    def mode(self, a):
        self.result = mode(a)
        return self.result

    def pop_stddev(self, a):
        self.result = stddev(a)
        return self.result

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result


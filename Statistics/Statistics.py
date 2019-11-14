from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
#from Statistics.Proportion import proportion
from CsvReader.CsvReader import CsvReader
from Statistics.Mode import mode
from Statistics.StandardDeviation import stddev
from Statistics.variance import variance
from Statistics.Zscore import Zscore




class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/StatsData.csv')
        super().__init__()

    def mode(self, a):
        self.result = mode(a)
        return self.result

    # def pop_proportion(self, a):
    #     self.result = proportion(a)
    #     return self.result



    def pop_stddev(self, a):
        self.result = stddev(a)
        return self.result

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def pop_variance(self, a):
        self.result = variance(a)
        return self.result

    def pop_z_score(self, a):
        self.result = Zscore(a)
        return self.result
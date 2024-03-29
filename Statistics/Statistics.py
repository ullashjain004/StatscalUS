from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Proportion import prop
from CsvReader.CsvReader import CsvReader
from Statistics.Mode import mode
from Statistics.StandardDeviation import stddev
from Statistics.variance import variance
from Statistics.Zscore import Zscore
from Statistics.PopCorrCoeff import pop_corr
from Statistics.Confidence_Interval import confi_int
from Statistics.Var_of_Pop_Prop import var_of_pop_prop
from Statistics.Sample_mean import sample_mean
from Statistics.Sample_Stddev import sample_std_dev

class Statistics(Calculator):
    data = []

    def __init__(self, filepath):
        self.data = CsvReader('Tests/Data/StatsData.csv')
        super().__init__()

    def mode(self, a):
        self.result = mode(a)
        return self.result

    def proportion(self, a):
        self.result = prop(a)
        return self.result

    def pop_stddev(self, a):
        self.result = stddev(a)
        return self.result

    def mean(self, a):
        self.result = mean(a)
        return self.result

    def pop_prop(self, a):
        self.result = var_of_pop_prop(a)
        return self.result

    def median(self, a):
        self.result = median(a)
        return self.result

    def pop_variance(self, a):
        self.result = variance(a)
        return self.result

    def pop_confi_int(self, a):
        self.result = confi_int(a)
        return self.result

    def samplestddev(self, a):
        self.result = sample_std_dev(a)
        return self.result

    def pop_z_score(self, a):
        self.result = Zscore(a)
        return self.result

    def samplemean(self, a):
        self.result = sample_mean(a)
        return self.result

    def popcorrcoeff(self, a, b):
        self.result = pop_corr(a, b)
        return self.result
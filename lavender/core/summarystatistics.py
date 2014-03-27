__author__ = 'lewis'

from math import sqrt


class SummaryStatistics:
    def __init__(self):
        self._values = []

    def add_value(self, value):
        self._values.append(value)

    def clear(self):
        self._values = []

    def count(self):
        return len(self._values)

    def sum(self):
        return float(sum(self._values))

    def mean(self):
        return self.sum() / self.count()

    def variance(self):
        mean = self.mean()
        sumSqDev = 0.0

        for value in self._values:
            dev = value - mean
            sumSqDev += dev * dev

        count = self.count()
        result = 0 if count == 0 else sumSqDev / count
        return result

    def stdev(self):
        variance = self.variance()
        result = sqrt(variance)
        return result



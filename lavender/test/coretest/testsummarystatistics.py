__author__ = 'lewis'

from math import sqrt
import unittest

from lavender.core.summarystatistics import SummaryStatistics


class MyTestCase(unittest.TestCase):

    @classmethod
    def stats(cls):
        stats = SummaryStatistics()
        for i in [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]:
            stats.add_value(i)

        return stats

    def test_count(self):
        stats = MyTestCase.stats()
        self.assertEqual(stats.count(), 10)

    def test_sum(self):
        stats = MyTestCase.stats()
        self.assertEqual(stats.sum(), 50)

    def test_mean(self):
        stats = MyTestCase.stats()
        self.assertEqual(stats.mean(), 5)

    def test_variance(self):
        stats = MyTestCase.stats()
        self.assertEqual(stats.variance(), 6)

    def test_stdev(self):
        stats = MyTestCase.stats()
        self.assertAlmostEqual(stats.stdev(), sqrt(6), 6)


if __name__ == '__main__':
    unittest.main()

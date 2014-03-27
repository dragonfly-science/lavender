__author__ = 'lewis'

import unittest
import time

from lavender.core.interactionrecord import InteractionRecordSet


class MyTestCase(unittest.TestCase):
    def test_empty_record_names(self):
        record_set = InteractionRecordSet()
        interaction_names = record_set.interaction_names
        self.assertEquals(len(interaction_names), 0)

    def test_record_names(self):
        record_set = InteractionRecordSet()

        record_set.new_timer("Timer 1")
        interaction_names = record_set.interaction_names
        self.assertEquals(1, len(interaction_names))
        self.names_are_equal(interaction_names, ["Timer 1"])

        record_set.new_timer("Timer 1")
        interaction_names = record_set.interaction_names
        self.names_are_equal(interaction_names, ["Timer 1"])

        record_set.new_timer("Timer 2")
        interaction_names = record_set.interaction_names
        self.names_are_equal(interaction_names, ["Timer 1", "Timer 2"])

    def test_empty_stats(self):
        record_set = InteractionRecordSet()
        stats = record_set.calculate_stats("Timer 1")
        self.assertEquals(stats.count(), 0)

    def test_stats_are_calculated(self):
        record_set = InteractionRecordSet()

        record_set.new_timer("Timer 1").stop()
        stats = record_set.calculate_stats("Timer 1")
        self.assertEquals(1, stats.count())

        record_set.new_timer("Timer 1").stop()
        stats = record_set.calculate_stats("Timer 1")
        self.assertEquals(2, stats.count())

        timer = record_set.new_timer("Timer 1")
        time.sleep(1)
        timer.stop()
        stats = record_set.calculate_stats("Timer 1")
        self.assertEquals(3, stats.count())
        self.assertAlmostEqual(1, stats.sum(), 2)

    def names_are_equal(self, names1, names2):
        names1.sort()
        names2.sort()
        return names1 == names2

if __name__ == '__main__':
    unittest.main()

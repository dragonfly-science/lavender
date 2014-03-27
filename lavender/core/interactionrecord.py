__author__ = 'lewis'

import copy

from interactiontimer import InteractionTimer
from summarystatistics import SummaryStatistics


class InteractionRecord:

    def __init__(self, name):
        self.name = name
        self._timer_list = []

    def new_timer(self):
        new_timer = InteractionTimer.start()
        self._timer_list.append(new_timer)
        return new_timer

    def calculate_statistics(self):
        stats = SummaryStatistics()

        for timer in self._timer_list:
            if timer.is_finished:
                stats.add_value(timer.duration)

        return stats


class InteractionRecordSet:
    def __init__(self):
        self._interaction_record_map = {}

    def new_timer(self, name):
        record = self._interaction_record_map.setdefault(name, InteractionRecord(name))
        return record.new_timer()

    @property
    def interaction_names(self):
        return copy.deepcopy(self._interaction_record_map.keys())

    def calculate_stats(self, interaction_name):
        if interaction_name in self._interaction_record_map:
            record = self._interaction_record_map.get(interaction_name)
            return record.calculate_statistics()
        else:
            return SummaryStatistics()
__author__ = 'lewis'

import copy
from summarystatistics import SummaryStatistics
from interactionrecord import InteractionRecordSet


class AppProxy:

    def __init__(self):
        self._driver = None
        self._interaction_record_set = InteractionRecordSet()

    def connect_to(self, driver):
        self._driver = driver
        self.init()

    def init(self):
        pass

    def disconnect(self):
        if self._driver is not None: self._driver.quit()

    def start_new_timer(self, name):
        return self._interaction_record_set.new_timer(name)

    @property
    def driver(self):
        return self._driver

    @property
    def interaction_names(self):
        return self._interaction_record_set.interaction_names

    def calculate_stats(self, interaction_name):
        return self._interaction_record_set.calculate_stats(interaction_name)
__author__ = 'lewis'

import platform_config
import selenium_wrapper
import testing_session

from interaction_record import InteractionRecordSet
from driver_manager import driver_for_config


class AppProxy:

    def __init__(self):
        self._interaction_record_set = InteractionRecordSet()
        test_session = testing_session.current_session()

        if not test_session.platform_config_name is None:
            config_name = test_session.platform_config_name
            if not config_name is None:
                config = platform_config.get_config(config_name)
                self._driver = driver_for_config(config)

    def connect_to(self, driver):
        self._driver = driver
        self.init()

    def init(self):
        pass

    def disconnect(self):
        if self._driver is not None:
            self._driver.quit()

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

    def wait_for_element_by_xpath_to_have_text(self, xpath, text):
        test_session = testing_session.current_session()
        max_wait = test_session.max_wait
        selenium_wrapper.wait_for_element_by_xpath_to_have_text(self.driver, xpath, text, max_wait)

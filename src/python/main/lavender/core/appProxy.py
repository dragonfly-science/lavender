__author__ = 'lewis'

from interactionrecord import InteractionRecordSet
import platformconfig
import testingsession
import seleniumwrapper
from drivermanager import driver_for_config
from selenium.common.exceptions import TimeoutException
from errors import LavenderError, LavenderTimeoutError


class AppProxy:

    def __init__(self):
        self._interaction_record_set = InteractionRecordSet()

        if not testingsession.platform_config_name() is None:
            config_name = testingsession.platform_config_name()
            if not config_name is None:
                config = platformconfig.get_config(config_name)
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
        max_wait = testingsession.max_wait()

        try:
            seleniumwrapper.wait_for_element_by_xpath_to_have_text(self.driver, xpath, text, max_wait)
        except TimeoutException:
            element = seleniumwrapper.find_element_by_xpath(self.driver, xpath)
            if element is None:
                raise LavenderTimeoutError("Unable to find element specified by xpath '{}'".format(xpath))
            else:
                raise LavenderError(
                    "Expected element specified by xpath '{}' to contain '{}' but instead found '{}'"
                    .format(xpath, text, element.text))

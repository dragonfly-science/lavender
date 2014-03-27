__author__ = 'lewis'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from core.errors import LavenderError, LavenderTimeoutError


def wait_for_element_by_xpath_to_have_text(driver, xpath, text, timeout):
        try:
            WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))
        except TimeoutException:
            element = find_element_by_xpath(driver, xpath)
            if element is None:
                raise LavenderTimeoutError("Unable to find element specified by xpath '{}'".format(xpath))
            else:
                raise LavenderError(
                    "Expected element specified by xpath '{}' to contain '{}' but instead found '{}'"
                    .format(xpath, text, element.text))


def find_element_by_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)
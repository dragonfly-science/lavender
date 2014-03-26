__author__ = 'lewis'

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def wait_for_element_by_xpath_to_have_text(driver, xpath, text, timeout):
    WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element((By.XPATH, xpath), text))


def find_element_by_xpath(driver, xpath):
    return driver.find_element_by_xpath(xpath)
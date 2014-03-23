__author__ = 'lewis'

import testingsession

from utils import new_dict_if_none
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver


def local_chrome_driver(caps=None):
    caps = new_dict_if_none(caps)
    full_caps = DesiredCapabilities.CHROME.copy().update(caps)
    driver = webdriver.Chrome(executable_path="/usr/bin/ChromeDriver", desired_capabilities=full_caps)

    return driver


def browser_stack_driver(browser_stack_account_properties, operating_system, browser, desired_caps=None):
    platform_caps = operating_system.set_capabilities()
    browser.set_capabilities(platform_caps)
    return _web_driver_for(browser_stack_account_properties, platform_caps, desired_caps)


def _web_driver_for(browser_stack_account_properties, platform_caps, desired_caps):
    full_caps = platform_caps.copy()

    if not desired_caps is None:
        full_caps.update(desired_caps)

    testingsession.update_capabilities(full_caps)

    url = browser_stack_account_properties.to_url()
    driver = webdriver.Remote(command_executor=url, desired_capabilities=full_caps)
    return driver

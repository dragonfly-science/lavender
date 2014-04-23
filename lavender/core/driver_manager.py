__author__ = 'lewis'

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

import testing_session
from browser_stack import BrowserStackAccountProperties
from platform_config import LocalChromeConfig, LocalPhantomConfig


def local_chrome_driver(platform_config):
    caps = platform_config.set_capabilities()
    full_caps = DesiredCapabilities.CHROME.copy()
    full_caps.update(caps)
    driver = webdriver.Chrome(executable_path="/usr/bin/ChromeDriver", desired_capabilities=full_caps)

    return driver


def local_phantom_driver(platform_config):
    caps = platform_config.set_capabilities()
    full_caps = DesiredCapabilities.PHANTOMJS.copy()
    full_caps.update(caps)
    return webdriver.PhantomJS(desired_capabilities=full_caps)


def browser_stack_driver(platform_config):
    browser_stack_account_properties = BrowserStackAccountProperties.get()
    platform_caps = platform_config.set_capabilities()
    return _web_driver_for(browser_stack_account_properties, platform_caps)


def driver_for_config(platform_config):
    generator_fn = None

    if isinstance(platform_config, LocalChromeConfig):
        generator_fn = local_chrome_driver
    elif isinstance(platform_config, LocalPhantomConfig):
        generator_fn = local_phantom_driver
    else:
        generator_fn = browser_stack_driver

    return generator_fn(platform_config)


def _web_driver_for(browser_stack_account_properties, platform_caps):
    full_caps = platform_caps.copy()
    test_session = testing_session.current_session()
    test_session.update_capabilities(full_caps)

    url = browser_stack_account_properties.to_url()
    driver = webdriver.Remote(command_executor=url, desired_capabilities=full_caps)
    return driver

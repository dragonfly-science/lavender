__author__ = 'lewis'

import unittest
from unittest.case import SkipTest

from lavender.core.driver_manager import local_chrome_driver, local_phantom_driver
from lavender.core.driver_manager import browser_stack_driver, driver_for_config
from lavender.core.operating_system import Windows7
from lavender.core.browser import IE8
from lavender.core import testing_session
from lavender.core.platform_config import (
    BrowserPlatformConfig, LocalChromeConfig, LocalPhantomConfig)
import os


class MyTestCase(unittest.TestCase):
    def test_local_chrome_driver(self):
        if not os.path.exists('/usr/bin/ChromeDriver'):
            raise SkipTest
        driver = local_chrome_driver(LocalChromeConfig())
        driver.quit()

    def test_local_phantom_driver(self):
        driver = local_phantom_driver(LocalPhantomConfig())
        driver.quit()

    def test_browser_stack_driver(self):
        testing_session.new_session(
            "python_api",
            "0.1",
            {}
        )

        test_session = testing_session.current_session()
        test_session.set_test_name("Testing Session Update Capabilities")
        driver = browser_stack_driver(BrowserPlatformConfig(Windows7, IE8))
        driver.quit()

if __name__ == '__main__':
    unittest.main()

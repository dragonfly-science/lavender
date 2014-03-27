__author__ = 'lewis'

import unittest

from lavender.core.drivermanager import local_chrome_driver
from lavender.core.drivermanager import browser_stack_driver, driver_for_config
from lavender.core.operatingSystem import Windows7
from lavender.core.browser import IE8
from lavender.core import testingsession
from lavender.core.platformconfig import BrowserPlatformConfig, LocalChromeConfig


class MyTestCase(unittest.TestCase):
    def test_local_chrome_driver(self):
        driver = local_chrome_driver(LocalChromeConfig())
        driver.quit()

    def test_browser_stack_driver(self):
        testingsession.new_session(
            "python_api",
            "0.1",
            {}
        )

        test_session = testingsession.current_session()
        test_session.set_test_name("Testing Session Update Capabilities")
        driver = browser_stack_driver(BrowserPlatformConfig(Windows7, IE8))
        driver.quit()

if __name__ == '__main__':
    unittest.main()

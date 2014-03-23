__author__ = 'lewis'

import unittest
import lavender.core.testingsession

from lavender.core.drivermanager import local_chrome_driver
from lavender.core.drivermanager import browser_stack_driver
from lavender.core.browserstack import BrowserStackAccountProperties
from lavender.core.operatingSystem import Windows7
from lavender.core.browser import IE8
from lavender.core import testingsession


class MyTestCase(unittest.TestCase):
    def test_local_chrome_driver(self):
        driver = local_chrome_driver();
        driver.quit()

    def test_browser_stack_driver(self):

        testingsession.set_session_details(
            project_name="python_api",
            build_name="0.1",
            test_name="Testing Session Update Capabilities"
        )

        testingsession.set_is_debug(True)
        testingsession.set_max_wait(10)
        caps = testingsession.update_capabilities()

        props = BrowserStackAccountProperties("lewiswalker", "py3FYbBbkr2pdF3dD3wL")
        driver = browser_stack_driver(props, Windows7, IE8)
        driver.quit()

if __name__ == '__main__':
    unittest.main()

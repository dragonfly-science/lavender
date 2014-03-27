__author__ = 'lewis'

import unittest

from lavender.core.capabilities import add_args
from lavender.core.capabilities import browser_stack_resolution
from lavender.core.capabilities import chrome_start_maximised
from lavender.core.capabilities import chrome_window_size


class MyTestCase(unittest.TestCase):

    def test_add_args_no_existing(self):
        caps = {"key": "value"}
        add_args(caps, ["arg1", "arg2"])

        self.assertEquals(len(caps.keys()), 2)
        self.assertEquals(caps["key"], "value")
        self.assertEquals(caps["args"], ["arg1", "arg2"])

    def test_add_args_to_existing(self):
        caps = {"key": "value", "args": ["arg1", "arg2"]}
        add_args(caps, ["arg3", "arg4"])

        self.assertEquals(len(caps.keys()), 2)
        self.assertEquals(caps["key"], "value")
        self.assertEquals(caps["args"], ["arg1", "arg2", "arg3", "arg4"])

    def test_browser_stack_resolution(self):
        caps = browser_stack_resolution(1280, 1024)
        self.assertEquals(caps["resolution"], "1280x1024")

    def test_chrome_start_maximised(self):
        caps = chrome_start_maximised()
        self.assertEquals(caps["args"], ["--start-maximized"])

    def test_chrome_window_size(self):
        caps = chrome_window_size(1280, 1024)
        self.assertEquals(caps["args"], ["--window-size=1280,1024"])


if __name__ == '__main__':
    unittest.main()

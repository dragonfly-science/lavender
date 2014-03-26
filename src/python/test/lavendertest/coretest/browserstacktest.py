__author__ = 'lewis'

import unittest
from lavender.core.browserstack import BrowserStackAccountProperties


class MyTestCase(unittest.TestCase):
    def test_url(self):
        props = BrowserStackAccountProperties("fredbloggs", "publickeystring")
        url = props.to_url()

        self.assertEquals(url, "http://fredbloggs:publickeystring@hub.browserstack.com/wd/hub")
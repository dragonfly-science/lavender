__author__ = 'lewis'

import unittest
import logging

from lavender.core import testingsession


class MyTestCase(unittest.TestCase):
    def test_update_capabilities(self):

        testingsession.set_session_details(
            project_name="python_api",
            build_name="0.1",
            test_name="Testing Session Update Capabilities"
        )

        testingsession.set_is_debug(True)
        testingsession.set_max_wait(10)
        caps = testingsession.update_capabilities()


if __name__ == '__main__':
    unittest.main()

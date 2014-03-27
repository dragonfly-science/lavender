__author__ = 'lewis'

import unittest

from lavender.core import testing_session


class MyTestCase(unittest.TestCase):
    def test_update_capabilities(self):
        testing_session.new_session(
            "python_api",
            "0.1",
            {}
        )

        test_session = testing_session.current_session()
        test_session.set_test_name("Testing Session Update Capabilities")

        test_session.set_is_debug(True)
        test_session.set_max_wait(30)
        caps = test_session.update_capabilities()

        self.assertIn("browserstack.debug", caps)
        self.assertIn("max_wait", caps)
        self.assertIn("project", caps)
        self.assertIn("build", caps)
        self.assertIn("name", caps)

        self.assertEquals(caps["browserstack.debug"], True)
        self.assertEquals(caps["project"], "python_api")
        self.assertEquals(caps["build"], "0.1")
        self.assertEquals(caps["name"], "Testing Session Update Capabilities")


if __name__ == '__main__':
    unittest.main()

__author__ = 'lewis'

import os

from errors import LavenderError
import call_arguments


class BrowserStackAccountProperties:

    def __init__(self, name, automate_key):
        self.name = name
        self.automate_key = automate_key

    def to_url(self):
        return "http://{0.name}:{0.automate_key}@hub.browserstack.com/wd/hub".format(self)

    @classmethod
    def get(cls):
        browser_stack_key = call_arguments.get("bs_key")
        if browser_stack_key is None:
            browser_stack_key = os.environ.get('BROWSER_STACK_KEY')

        browser_stack_name = call_arguments.get("bs_name")
        if browser_stack_name is None:
            browser_stack_name = os.environ.get('BROWSER_STACK_NAME')

        if browser_stack_key is None:
            raise LavenderError(
                "Browser Stack key must be set through either the Environment variable "
                "'BROWSER_STACK_KEY' or via the command line option --bs-key")

        if browser_stack_name is None:
            raise LavenderError(
                "Browser Stack name must be set through either the Environment variable "
                "'BROWSER_STACK_NAME' or via the command line option --bs-name")

        return BrowserStackAccountProperties(browser_stack_name, browser_stack_key)

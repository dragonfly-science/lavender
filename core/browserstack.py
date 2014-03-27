__author__ = 'lewis'

import os

from core.errors import LavenderError
import callarguments


class BrowserStackAccountProperties:

    def __init__(self, username, automate_key):
        self.username = username
        self.automate_key = automate_key

    def to_url(self):
        return "http://{0.username}:{0.automate_key}@hub.browserstack.com/wd/hub".format(self)

    @classmethod
    def get(cls):
        browser_stack_username = callarguments.get("bs_username")
        if browser_stack_username is None:
            browser_stack_username = os.environ.get('BROWSER_STACK_USERNAME')

        browser_stack_password = callarguments.get("bs_password")
        if browser_stack_password is None:
            browser_stack_password = os.environ.get('BROWSER_STACK_PASSWORD')

        if browser_stack_username is None:
            raise LavenderError(
                "Browser Stack username must be set through either the Environment variable "
                "'BROWSER_STACK_USERNAME' or via the command line option --bs_username")

        if browser_stack_password is None:
            raise LavenderError(
                "Browser Stack password must be set through either the Environment variable "
                "'BROWSER_STACK_PASSWORD' or via the command line option --bs_password")

        return BrowserStackAccountProperties(browser_stack_username, browser_stack_password)
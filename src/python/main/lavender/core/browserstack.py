__author__ = 'lewis'

import os
from lavender.core.errors import LavenderError


class BrowserStackAccountProperties:

    def __init__(self, username, automate_key):
        self.username = username
        self.automate_key = automate_key

    def to_url(self):
        return "http://{0.username}:{0.automate_key}@hub.browserstack.com/wd/hub".format(self)

    @classmethod
    def get(cls):
        browser_stack_username = os.environ.get('BROWSER_STACK_USERNAME')
        browser_stack_password = os.environ.get('BROWSER_STACK_PASSWORD')

        if browser_stack_username is None:
            raise LavenderError("Environment variable 'BROWSER_STACK_USERNAME' must be set")

        if browser_stack_password is None:
            raise LavenderError("Environment variable 'BROWSER_STACK_PASSWORD' must be set")

        return BrowserStackAccountProperties(browser_stack_username, browser_stack_password)

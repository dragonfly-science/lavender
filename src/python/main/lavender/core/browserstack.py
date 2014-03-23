__author__ = 'lewis'


class BrowserStackAccountProperties:

    def __init__(self, username, automate_key):
        self.username = username
        self.automate_key = automate_key

    def to_url(self):
        return "http://{0.username}:{0.automate_key}@hub.browserstack.com/wd/hub".format(self)
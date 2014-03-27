__author__ = 'lewis'


class LavenderError(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)


class LavenderTimeoutError(LavenderError):
    def __init__(self, msg):
        LavenderError.__init__(self, msg)
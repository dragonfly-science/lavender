__author__ = 'lewis'

from core.utils import new_dict_if_none


class MobilePlatform:

    def __init__(self, name):
        self._caps = {"platform": name}

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        caps.update(self._caps)
        return caps

iOS = MobilePlatform("MAC"),
Android = MobilePlatform("ANDROID");
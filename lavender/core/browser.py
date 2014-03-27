__author__ = 'lewis'

from utils import new_dict_if_none


class Browser:

    def __init__(self, name, version):
        self._caps = {"browser": name, "browser_version": version}

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        caps.update(self._caps)
        return caps

IE7 = Browser("IE", "7.0")
IE8 = Browser("IE", "8.0")
IE9 = Browser("IE", "9.0")
IE10 = Browser("IE", "10.0")
IE11 = Browser("IE", "11.0")
Chrome32 = Browser("Chrome", "32.0")
Firefox27 = Browser("Firefox", "27.0")
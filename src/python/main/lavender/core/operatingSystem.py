__author__ = 'lewis'

from utils import new_dict_if_none


class OperatingSystem:

    def __init__(self, name, version):
        self._caps = {"os": name, "os_version": version}

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        caps.update(self._caps)
        return caps

Windows7 = OperatingSystem("Windows", "7")
Windows8 = OperatingSystem("Windows", "8")
Windows8_1 = OperatingSystem("Windows", "8.1")
WindowsXP = OperatingSystem("Windows", "XP")
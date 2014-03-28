__author__ = 'lewis'

from utils import new_dict_if_none


_advertised_configs = {}


class PlatformConfig(object):

    def __init__(self, caps=None):
        self._caps = new_dict_if_none(caps)

    @property
    def caps(self):
        return self._caps


class LocalChromeConfig(PlatformConfig):

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        self.caps.update(caps)
        return caps


class LocalPhantomConfig(PlatformConfig):

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        self.caps.update(caps)
        return caps


class BrowserPlatformConfig(PlatformConfig):
    def __init__(self, operating_system, browser, caps=None):
        super(BrowserPlatformConfig, self).__init__(caps)
        self._operating_system = operating_system
        self._browser = browser

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        self.caps.update(caps)
        self._operating_system.set_capabilities(caps)
        self._browser.set_capabilities(caps)
        return caps


class MobilePlatformConfig(PlatformConfig):
    def __init__(self, mobile_platform, mobile_device, caps=None):
        super(MobilePlatformConfig, self).__init__(caps)
        self._mobile_platform = mobile_platform
        self._mobile_device = mobile_device

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        self.caps.update(caps)
        self._mobile_platform.set_capabilities(caps)
        self._mobile_device.set_capabilities(caps)
        return caps


# noinspection PyProtectedMember
def advertise_config(name, config):
    _advertised_configs[name] = config


# noinspection PyProtectedMember
def advertised_configs():
    return _advertised_configs


# noinspection PyProtectedMember
def get_config(name):
    return _advertised_configs[name]

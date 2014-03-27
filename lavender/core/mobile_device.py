__author__ = 'lewis'

from utils import new_dict_if_none


class MobileDevice:

    def __init__(self, name, version):
        self._caps = {"browserName": name, "device": version}

    def set_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)
        caps.update(self._caps)
        return caps

SamsungGalaxyNote_10_1 = MobileDevice("android", "Samsung Galaxy Note 10.1")
GoogleNexus_7 = MobileDevice("android", "Google Nexus 7")
AmazonKindleFire_2 = MobileDevice("android", "Amazon Kindle Fire 2")
AmazonKindleFireHD_8_9 = MobileDevice("android", "Amazon Kindle Fire HD 8.9")
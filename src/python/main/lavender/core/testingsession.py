__author__ = 'lewis'

from utils import new_dict_if_none


_props = {
    "project": "",
    "build": "",
    "name": "",
    "browserstack.debug": False,
    "max_wait": 15,
}


def set_session_details(project_name="", build_name="", test_name=""):
    _props["project"] = project_name
    _props["build"] = build_name
    _props["name"] = test_name


def set_is_debug(is_debug):
    _props["browserstack.debug"] = is_debug


def set_max_wait(max_wait):
    _props["max_wait"] = max_wait


def update_capabilities(caps=None):
    caps = new_dict_if_none(caps)
    caps.update(_props)
    return caps

def max_wait():
    return _props["max_wait"]
__author__ = 'lewis'

import nose

from platform_config import advertise_config
from utils import new_dict_if_none
import call_arguments
import sys


class TestingSession:

    _the_instance = None

    def __init__(self, project_name, build_name):
        self._project_name = project_name
        self._build_name = build_name
        self._test_name = ""
        self._is_debug = False
        self._max_wait = 15
        self._platform_config_name = None

        call_arguments.init(project_name)

    def set_test_name(self, test_name):
        self._test_name = test_name

    def set_is_debug(self, is_debug):
        self._is_debug = is_debug

    def set_max_wait(self, wait):
        self._max_wait = wait

    def set_platform_config_name(self, name):
        self._platform_config_name = name

    def update_capabilities(self, caps=None):
        caps = new_dict_if_none(caps)

        _props = {
            "project": self._project_name,
            "build": self._build_name,
            "name": self._test_name,
            "browserstack.debug": self._is_debug,
            "max_wait": self._max_wait,
        }

        caps.update(_props)
        return caps

    @property
    def max_wait(self):
        return self._max_wait

    @property
    def platform_config_name(self):
        if not self._platform_config_name is None:
            config_name = self._platform_config_name
        else:
            config_name = call_arguments.get("config")

        return config_name

    def run(self, *args):
        call_arguments.parse_args()
        for a in args:
            sys.argv.append(a)
        nose.run()


def new_session(project_name, build_name, configs):
    for name in configs:
        advertise_config(name, configs[name])

    TestingSession._the_instance = TestingSession(project_name, build_name)
    return TestingSession._the_instance


def current_session():
    return TestingSession._the_instance
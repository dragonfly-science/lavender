__author__ = 'lewis'

from sys import argv
import argparse

from platform_config import advertised_configs


_arguments = None
_parser = None


def get(name):
    global _arguments
    return None if not hasattr(_arguments, name) else getattr(_arguments, name)


def arguments():
    global _arguments
    return _arguments

def add_argument(*args, **kwargs):
    parser().add_argument(*args, **kwargs)


def parse_args():
    global _arguments
    if _arguments is None:
        _arguments = _parser.parse_args()
        app_args = ['--bs-username', '--bs-password', '--app-username', '--app-password', '--config']

        for name in _arguments.__dict__:
            if name != 'tests' and name != 'xunit_file':
                value = getattr(_arguments, name)
                if value in argv:
                    argv.remove(value)

        for name in app_args:
            if name in argv:
                argv.remove(name)


def init(name):
    global _parser
    _parser = argparse.ArgumentParser(description=name)
    _parser.add_argument(
        '--bs-username',
        metavar='Username',
        help='The username of the Browser Stack account under which tests should be run')

    _parser.add_argument(
        '--bs-password',
        metavar='Password',
        help='The password corresponding to the Browser Stack username')

    configs = advertised_configs()

    if len(configs) > 0:
        _parser.add_argument(
            '--config',
            metavar='name',
            help='An advertised platform configuration name',
            choices=advertised_configs().keys())

    # Passed through to nose
    _parser.add_argument("--with-xunit", help="Generate xunit output", action="store_true")
    _parser.add_argument("--nologcapture", help="Disable log capturing", action="store_true")
    _parser.add_argument(
        "tests",
        help=(
            "which tests to run (file names, module names and or modules "
            "suffixed with the TestClass derivative - "
            "passed through to nose"),
        nargs="*")

    _parser.add_argument("--xunit-file", metavar="FILE", help=(
        "Path to xml file to store the xunit report in. "
        "Default is nosetests.xml in the working directory"))


def parser():
    global _parser
    if _parser is None:
        init('Lavender Test Suite')

    return _parser
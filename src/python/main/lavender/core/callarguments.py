__author__ = 'lewis'

from platformconfig import advertised_configs

_arguments = {}


def get(name):
    return None if not name in _arguments else getattr(_arguments, name)


def add_to_parser(parser):
    parser.add_argument(
        '--bs-username',
        metavar='Username',
        help='The username of the Browser Stack account under which tests should be run')

    parser.add_argument(
        '--bs-password',
        metavar='Password',
        help='The password corresponding to the Browser Stack username')

    configs = advertised_configs()

    if len(configs) > 0:
        parser.add_argument(
            '--config',
            metavar='name',
            help='An advertised platform configuration name',
            choices=advertised_configs().keys())

    # Passed through to nose
    parser.add_argument("--with-xunit", help="Generate xunit output", action="store_true")
    parser.add_argument("--nologcapture", help="Disable log capturing", action="store_true")
    parser.add_argument(
        "tests",
        help=(
            "which tests to run (file names, module names and or modules "
            "suffixed with the TestClass derivative - "
            "passed through to nose"),
        nargs="*")

    parser.add_argument("--xunit-file", metavar="FILE", help=(
        "Path to xml file to store the xunit report in. "
        "Default is nosetests.xml in the working directory"))

    global _arguments
    _arguments = parser.parse_args()
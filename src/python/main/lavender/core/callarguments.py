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

    global _arguments
    _arguments = parser.parse_args()
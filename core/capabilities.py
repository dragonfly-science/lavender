__author__ = 'lewis'

from core.utils import new_dict_if_none


def browser_stack_resolution(width, height, caps=None):
    caps = new_dict_if_none(caps)
    caps["resolution"] = "{0}x{1}".format(width, height)
    return caps


def chrome_start_maximised(caps=None):
    caps = new_dict_if_none(caps)
    return add_args(caps, ["--start-maximized"])


def chrome_window_size(width, height, caps=None):
    caps = new_dict_if_none(caps)
    return add_args(caps, ["--window-size={0},{1}".format(width, height)])


def add_args(caps, new_args):
    args = caps.setdefault("args", [])
    args.extend(new_args)
    return caps


"""
Module contains functions to printing render time in the console.
Functions returning the date and time.
"""


from datetime import datetime


rt_info = "[MDSANIMA RT]"


def rt_init(scene):
    time_init = datetime.now()
    print(rt_info, "->", str(time_init).ljust(26), "=> Render Init")
    return time_init


def rt_start(scene):
    time_start = datetime.now()
    print(rt_info, "->", str(time_start).ljust(26), "=> Render Start")
    return time_start


def rt_complete(scene):
    time_complete = datetime.now()
    print(rt_info, "->", str(time_complete).ljust(26), "=> Render Complete")
    return time_complete


def rt_cancel(scene):
    time_cancel = datetime.now()
    print(rt_info, "->", str(time_cancel).ljust(26), "=> Render Cancel")
    return time_cancel

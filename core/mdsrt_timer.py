"""
Module contains functions to printing render time in the console.
"""


from datetime import datetime


def rt_init(scene):
    print("[MDSANIMA RT] ->", datetime.now(), "Render Init")


def rt_start(scene):
    print("[MDSANIMA RT] ->", datetime.now(), "Render Start")


def rt_complete(scene):
    print("[MDSANIMA RT] ->", datetime.now(), "Render Complete")


def rt_cancel(scene):
    print("[MDSANIMA RT] ->", datetime.now(), "Render Cancel")


"""
Module contains functions to printing render time in the console.
Functions returning the date and time for actual renderig.
"""


from bpy.app import handlers
from datetime import datetime


def rt_stats():
    rt_info = "[MDSANIMA RT]"


    @handlers.persistent
    def rt_init(dummy):
        ti_init = datetime.now()
        print(rt_info, "->", str(ti_init).ljust(26), "=> Render Init")
        return ti_init


    @handlers.persistent
    def rt_start(dummy):
        ti_start = datetime.now()
        print(rt_info, "->", str(ti_start).ljust(26), "=> Render Start")
        return ti_start


    @handlers.persistent
    def rt_complete(dummy):
        ti_complete = datetime.now()
        print(rt_info, "->", str(ti_complete).ljust(26), "=> Render Complete")
        return ti_complete


    @handlers.persistent
    def rt_cancel(dummy):
        ti_cancel = datetime.now()
        print(rt_info, "->", str(ti_cancel).ljust(26), "=> Render Cancel")
        return ti_cancel


    handlers.render_init.append(rt_init)
    handlers.render_pre.append(rt_start)
    handlers.render_complete.append(rt_complete)
    handlers.render_cancel.append(rt_cancel)

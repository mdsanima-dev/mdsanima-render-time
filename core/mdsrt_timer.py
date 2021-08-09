"""
Module contains functions to printing render time in the console.
Functions store the date and time for actual renderig in global variable.
"""


from bpy.app import handlers
from datetime import datetime


# initail global variable timer
ti_init = None
ti_start = None
ti_complete = None
ti_cancel = None


def rt_stats():
    """Function contains all handlers for printing stats in the console"""
    rt_info = "[MDSANIMA RT]"

    @handlers.persistent
    def rt_init(dummy):
        global ti_init
        ti_init = datetime.now()
        print(rt_info, "->", str(ti_init).ljust(26), "=> Render Init")

    @handlers.persistent
    def rt_start(dummy):
        global ti_start
        ti_start = datetime.now()
        print(rt_info, "->", str(ti_start).ljust(26), "=> Render Start")

    @handlers.persistent
    def rt_complete(dummy):
        global ti_complete
        ti_complete = datetime.now()
        print(rt_info, "->", str(ti_complete).ljust(26), "=> Render Complete")

    @handlers.persistent
    def rt_cancel(dummy):
        global ti_cancel
        ti_cancel = datetime.now()
        print(rt_info, "->", str(ti_cancel).ljust(26), "=> Render Cancel")

    # append printing message render time stats timer
    handlers.render_init.append(rt_init)
    handlers.render_pre.append(rt_start)
    handlers.render_complete.append(rt_complete)
    handlers.render_cancel.append(rt_cancel)

"""
Blender Addon for estimated total rendering time for all frames in your
animation.

Creates a Panel in the UI 3D View to show rendering statistic.
"""


import os
import bpy
from datetime import datetime


# addon information dictionary
bl_info = {
    "name": "MDSANIMA RenderTime",
    "description": "Estimated total rendering time for all frames",
    "author": "Marcin Różewski (mdsanima)",
    "license": "GPL",
    "deps": "",
    "version": (0, 1, 0),
    "blender": (2, 93, 2),
    "location": "View3D > UI",
    "warning": "",
    "doc_url": "https://github.com/mdsanima-dev/mdsanima-render-time/",
    "tracker_url": "https://github.com/mdsanima-dev/mdsanima-render-time/issues",
    "link": "https://mdsanima.com",
    "support": "COMMUNITY",
    "category": "Render"
}


from bpy.app import handlers
from datetime import datetime, timedelta


# initail global variable timer
ti_init = None
ti_start = None
ti_complete = None
ti_cancel = None
rt_init_render = None
rt_one_frame = None
rt_info = "[MDSANIMA RT]"


@handlers.persistent
def rt_init(dummy):
    global ti_init
    ti_init = datetime.now()
    print(rt_info, "->", str(ti_init).ljust(26), "=> Render Init")


@handlers.persistent
def rt_start(dummy):
    global ti_start
    global rt_init_render
    ti_start = datetime.now()
    rt_init_render = (ti_start - ti_init)
    print(rt_info, "->", str(ti_start).ljust(26), "=> Render Start")
    print(rt_info, "->", "RT Initialization =>", rt_init_render)


@handlers.persistent
def rt_complete(dummy):
    global ti_complete
    global rt_one_frame
    ti_complete = datetime.now()
    rt_one_frame = (ti_complete - ti_start)
    print(rt_info, "->", str(ti_complete).ljust(26), "=> Render Complete")
    print(rt_info, "->", "RT One Frame =>", rt_one_frame)


@handlers.persistent
def rt_cancel(dummy):
    global ti_cancel
    global rt_one_frame
    ti_cancel = datetime.now()
    rt_one_frame = (ti_cancel - ti_start)
    print(rt_info, "->", str(ti_cancel).ljust(26), "=> Render Cancel")
    print(rt_info, "->", "RT One Frame =>", rt_one_frame)


class MDSRT_PT_render_time(bpy.types.Panel):
    """Creates a Panel in the UI 3D View"""
    MDSRT_version = str(bl_info["version"])\
        .replace("(", "")\
        .replace(")", "")\
        .replace(", ", ".")
    bl_idname = "MDSRT_PT_render_time"
    bl_label = "MDSANIMA RenderTime v" + MDSRT_version
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MDSANIMA RenderTime"

    def draw(self, context):
        # initial variable layout
        layout = self.layout
        scene = bpy.context.scene

        # initial variable get icons from dictionary
        pcoll = preview_collections["main"]
        ico_w = pcoll["ic_mds_whit"]
        ico_b = pcoll["ic_mds_blue"]

        # initial variable calculation resolution
        perc_res_v = 100 / scene.render.resolution_percentage
        res_x = scene.render.resolution_x / perc_res_v
        res_y = scene.render.resolution_y / perc_res_v
        res_val = str(int(res_x)) + " x " + str(int(res_y))

        # initial variable calculation all frames
        sta_frames = scene.frame_start
        end_frames = scene.frame_end
        check_frame = 1 if sta_frames == 1 or sta_frames == 0 else 0
        all_frames = (end_frames - sta_frames) + check_frame
        time_code = bpy.utils.smpte_from_frame(all_frames)


        # render properties stats info
        row = layout.row()
        row.label(text="Render Engine", icon="DESKTOP")
        row.label(text=scene.render.engine)

        row = layout.row()
        row.label(text="Device", icon="MEMORY")
        row.label(text=scene.cycles.device)

        row = layout.row()
        row.label(text="Samples", icon="SHADING_BBOX")
        row.label(text=str(scene.cycles.samples))


        layout.separator()


        # output properties stats info
        row = layout.row()
        row.label(text="Resolution", icon="RESTRICT_VIEW_ON")
        row.label(text=res_val)

        row = layout.row()
        row.label(text="All Frames", icon="RENDER_ANIMATION")
        row.label(text=str(all_frames))

        row = layout.row()
        row.label(text="Frame Rate", icon="OUTLINER_DATA_CAMERA")
        row.label(text=str(scene.render.fps) + " fps")

        row = layout.row()
        row.label(text="Duration TC", icon="PREVIEW_RANGE")
        row.label(text=time_code)


        layout.separator()


        # render button operator
        row = layout.row()
        row.scale_y = 2.0
        row.operator("render.render", text="Render", icon_value=ico_b.icon_id)


        # checking draw layout
        if rt_init_render == None:
            pass
        else:
            # initial variable calculation render time
            ini_frame_rt = rt_init_render
            one_frame_rt = rt_one_frame
            all_frame_rt = (one_frame_rt * all_frames)
            date_now = datetime.now()
            sec_complete = timedelta(seconds=all_frame_rt.total_seconds())
            calc_complete = date_now + sec_complete
            start_render = date_now.strftime("%Y-%m-%d %H:%M:%S")
            complete_render = calc_complete.strftime("%Y-%m-%d %H:%M:%S")


            layout.separator()


            # render time stats info
            row = layout.row()
            row.label(text="RT Initialization", icon="IMAGE_PLANE")
            row.label(text=str(ini_frame_rt))

            row = layout.row()
            row.label(text="RT One Frame", icon="OUTPUT")
            row.label(text=str(one_frame_rt)[:-4])

            row = layout.row()
            row.label(text="RT All Frames", icon="FILE_MOVIE")
            row.label(text=str(all_frame_rt)[:-4])

            row = layout.row()
            row.label(text="Render Start", icon="PLUGIN")
            row.label(text=str(start_render))

            row = layout.row()
            row.label(text="Render Complete", icon="EXTERNAL_DRIVE")
            row.label(text=str(complete_render))


            layout.separator()


            # button website
            row = layout.row(align=True)
            row.operator(
                "mdsrt.web_issues", text="GITHUB", icon="SCRIPTPLUGINS"
                )
            row.operator(
                "mdsrt.web_mdsanima", text="MDSANIMA", icon_value=ico_b.icon_id
                )
            row.operator(
                "mdsrt.web_blog", text="BLOG", icon_value=ico_w.icon_id
                )


class MDSRT_OT_web_issues(bpy.types.Operator):
    bl_idname = "mdsrt.web_issues"
    bl_label = "GITHUB ISSUES"
    bl_description = "Opening the GITHUB ISSUES website in your browswer"

    def execute(self, context):
        git_iss = "https://github.com/mdsanima-dev/mdsanima-render-time/issues"
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url=git_iss)
        return {"FINISHED"}


class MDSRT_OT_web_mdsanima(bpy.types.Operator):
    bl_idname = "mdsrt.web_mdsanima"
    bl_label = "MDSANIMA"
    bl_description = "Opening the MDSANIMA website in your browswer"

    def execute(self, context):
        mds_web = "https://mdsanima.com/"
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url=mds_web)
        return {"FINISHED"}


class MDSRT_OT_web_blog(bpy.types.Operator):
    bl_idname = "mdsrt.web_blog"
    bl_label = "BLOG"
    bl_description = "Opening the MDSANIMA BLOG website in your browswer"

    def execute(self, context):
        blog_web = "https://blendervisual.blogspot.com/"
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url=blog_web)
        return {"FINISHED"}


# initial dictionary for custom icons data
preview_collections = {}


def register():
    # initial variable icons name
    ic_mds_whit = "ic_mdsanima_12_drp_sdw_w.png"
    ic_mds_blue = "ic_mdsanima_20_drp_sdw_b.png"

    # store custom icons data
    import bpy.utils.previews
    pcoll = bpy.utils.previews.new()

    # path to the folder where the icon is
    mds_ic_dir = os.path.join(os.path.dirname(__file__), "icons")

    # load a preview thumbnail of a file and store in the previews collection
    pcoll.load("ic_mds_whit", os.path.join(mds_ic_dir, ic_mds_whit), 'IMAGE')
    pcoll.load("ic_mds_blue", os.path.join(mds_ic_dir, ic_mds_blue), 'IMAGE')
    preview_collections["main"] = pcoll

    # append printing message render time stats timer
    handlers.render_init.append(rt_init)
    handlers.render_pre.append(rt_start)
    handlers.render_complete.append(rt_complete)
    handlers.render_cancel.append(rt_cancel)

    # register class panel render time
    bpy.utils.register_class(MDSRT_PT_render_time)
    bpy.utils.register_class(MDSRT_OT_web_issues)
    bpy.utils.register_class(MDSRT_OT_web_mdsanima)
    bpy.utils.register_class(MDSRT_OT_web_blog)


def unregister():
    # clear all icons preview data
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

    # unregister class panel render time
    bpy.utils.unregister_class(MDSRT_PT_render_time)
    bpy.utils.unregister_class(MDSRT_OT_web_issues)
    bpy.utils.unregister_class(MDSRT_OT_web_mdsanima)
    bpy.utils.unregister_class(MDSRT_OT_web_blog)


if __name__ == "__main__":
    register()

"""
Blender Addon for estimated total rendering time for all frames in your
animation.

Creates a Panel in the UI 3D View to show rendering statistic.
"""


import os
import bpy


# initial links variable
github_url = "https://github.com/mdsanima-dev/mdsanima-render-time/"
issues_url = github_url + "issues"
mdsanima_url = "https://mdsanima.com"

# addon information dictionary
bl_info = {
    "name": "MDSANIMA RenderTime",
    "description": "Estimated total rendering time for all frames",
    "author": "Marcin Różewski (mdsanima)",
    "license": "GPL",
    "deps": "",
    "version": (0, 1, 0),
    "blender": (2, 93, 1),
    "location": "View3D > UI",
    "warning": "",
    "doc_url": github_url,
    "tracker_url": issues_url,
    "link": mdsanima_url,
    "support": "TESTING",
    "category": "Render"
    }


from .core.mdsrt_timer import rt_stats
from .core.mdsrt_timer import ti_init, ti_start, ti_complete, ti_cancel


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
        # initial variable get icons from dictionary
        pcoll = preview_collections["main"]
        ico_w = pcoll["ic_mds_whit"]
        ico_b = pcoll["ic_mds_blue"]

        # initial variable layout
        layout = self.layout

        layout.separator()

        row = layout.row()
        row.operator("render.render", text="Render", icon_value=ico_w.icon_id)

        layout.separator()


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

    # register class panel render time
    bpy.utils.register_class(MDSRT_PT_render_time)

    # print render stats in the console
    rt_stats()


def unregister():
    # clear all icons preview data
    for pcoll in preview_collections.values():
        bpy.utils.previews.remove(pcoll)
    preview_collections.clear()

    # unregister class panel render time
    bpy.utils.unregister_class(MDSRT_PT_render_time)


if __name__ == "__main__":
    register()

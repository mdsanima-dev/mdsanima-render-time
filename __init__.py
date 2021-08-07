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
    "doc_url": "https://github.com/mdsanima-dev/mdsanima-render-time/",
    "wiki_url": "https://github.com/mdsanima-dev/mdsanima-render-time/wiki",
    "tracker_url": "https://github.com/mdsanima-dev/mdsanima-render-time/issues",
    "link": "https://mdsanima.com",
    "support": "TESTING",
    "category": "Render"
    }


import bpy

from .core.mdsrt_timer import rt_stats
from .core.mdsrt_timer import ti_init, ti_start, ti_complete, ti_cancel


class MDSRT_PT_render_time(bpy.types.Panel):
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
        layout = self.layout

        layout.separator()

        row = layout.row(align=True)
        row.operator("render.render", text="Render", icon='RENDER_STILL')

        layout.separator()


def register():
    bpy.utils.register_class(MDSRT_PT_render_time)
    rt_stats()


def unregister():
    bpy.utils.unregister_class(MDSRT_PT_render_time)


if __name__ == "__main__":
    register()

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

from .core.mdsrt_timer import rt_init, rt_start, rt_complete, rt_cancel


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
    bpy.app.handlers.render_init.append(rt_init)
    bpy.app.handlers.render_pre.append(rt_start)
    bpy.app.handlers.render_complete.append(rt_complete)
    bpy.app.handlers.render_cancel.append(rt_cancel)


def unregister():
    bpy.utils.unregister_class(MDSRT_PT_render_time)


if __name__ == "__main__":
    register()

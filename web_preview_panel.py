import bpy

class WebPreviewPanel(bpy.types.Panel):
    bl_label = "Web Preview Panel"
    bl_idname = "WEBPREVIEWPANEL_PT_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "Web Preview"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("object.webpreview", text="Preview in browser", icon="WORLD_DATA")

def register():
    bpy.utils.register_class(WebPreviewPanel)

def unregister():
    bpy.utils.unregister_class(WebPreviewPanel)

import bpy
import os
import subprocess
import webbrowser
import socket

def servertest(argv):
    host = argv[0]
    port = int(argv[1])

    args = socket.getaddrinfo(host, port, socket.AF_INET, socket.SOCK_STREAM)
    for family, socktype, proto, canonname, sockaddr in args:
        s = socket.socket(family, socktype, proto)
        try:
            s.connect(sockaddr)
        except socket.error:
            return False
        else:
            s.close()
            return True

class WebPreviewButton(bpy.types.Operator):
    bl_idname = "object.webpreview"
    bl_label = "Preview in browser"
    bl_description ="Run preview in browser"

    def execute(self, context):
        addon_path = bpy.utils.user_resource('SCRIPTS', "addons") + "\\web_preview"
        os.chdir(addon_path)
        
        bpy.ops.export_scene.gltf(export_format='GLTF_EMBEDDED', export_cameras=True, export_lights=True, filepath=os.path.join(addon_path, "Preview.gltf"))
        
        if not servertest(["localhost", "8000"]):
            subprocess.Popen("python -m http.server")
        
        webbrowser.open("http://localhost:8000/Preview.html")

        return {'FINISHED'}

def register():
    bpy.utils.register_class(WebPreviewButton)

def unregister():
    bpy.utils.unregister_class(WebPreviewButton)
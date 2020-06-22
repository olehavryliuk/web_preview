import bpy
import sys
import importlib

bl_info = {
    "name": "Web Preview",
    "author": "Oleh Havryliuk",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > N",
    "description": "Runs web preview on python http.server",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}

moduleNames = ['web_preview_button', 'web_preview_panel']

moduleFullNames = {}
for currentModuleName in moduleNames:
    moduleFullNames[currentModuleName] = ('{}.{}'.format(__name__, currentModuleName))

for currentModuleFullName in moduleFullNames.values():
    if currentModuleFullName in sys.modules:
        importlib.reload(sys.modules[currentModuleFullName])
    else:
        globals()[currentModuleFullName] = importlib.import_module(currentModuleFullName)
        setattr(globals()[currentModuleFullName], 'moduleNames', moduleFullNames)

def register():
    for currentModuleName in moduleFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'register'):
                sys.modules[currentModuleName].register()

def unregister():
    for currentModuleName in moduleFullNames.values():
        if currentModuleName in sys.modules:
            if hasattr(sys.modules[currentModuleName], 'unregister'):
                sys.modules[currentModuleName].unregister()

if __name__ == "__main__":
    register()
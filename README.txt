import sys
import maya.cmds as cmds

path_to_scripts_folder = r'C:\Users\Natalia\Documents\maya\scripts\playblast-project'
if path_to_scripts_folder not in sys.path:
    sys.path.append(path_to_scripts_folder)



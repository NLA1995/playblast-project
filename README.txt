#IF IT DOESN'T WORK RUN THIS CODE FIRST REMPLACING 'YOUREQUIPMENTNAME' THEN RUN THE PREVIOUS CODE.

import sys
import maya.cmds as cmds

path_to_scripts_folder = r'C:\Users\YOUREQUIPMENTNAME\Documents\maya\scripts\playblast-project'
if path_to_scripts_folder not in sys.path:
    sys.path.append(path_to_scripts_folder)



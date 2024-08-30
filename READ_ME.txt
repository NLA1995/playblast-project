This tool enables you to create highly personalized playblasts, allowing you to display 
important information about the shot. You can include details such as the artist's name, 
company name, timestamp, and department.

#COPY THIS SCRIP INTO YOUR MAYA SCRIPT'S FOLDER
#PASTE THE NEXT COMAND INTO A PYTHON TAB INSIDE SCRIPT EDITOR 
#THEN WITH THE MIDDLE MOUSE DRAG IT TO YOUR CUSTOM SHELF 


import sys
import os
import subprocess
import importlib
from utils import playblast_utils, ffmpeg_utils
from core import capture
from ui import playblast_ui
importlib.reload(playblast_utils)
importlib.reload(ffmpeg_utils)
importlib.reload(capture)
importlib.reload(playblast_ui)

window_1 = playblast_ui.PlayblastManagerUI()
window_1.show()



#IF IT DOESN'T WORK RUN THIS CODE FIRST REMPLACING 'YOUREQUIPMENTNAME' THEN RUN THE PREVIOUS CODE.

import sys
import maya.cmds as cmds

path_to_scripts_folder = r'C:\Users\YOUREQUIPMENTNAME\Documents\maya\scripts\playblast-project'
if path_to_scripts_folder not in sys.path:
    sys.path.append(path_to_scripts_folder)
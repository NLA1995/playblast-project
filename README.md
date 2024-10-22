This tool enables you to create highly personalized playblasts, allowing you to display 
important information about the shot. You can include details such as the artist's name, 
company name, frame count, and department.

#COPY THIS ENTIRE TOOL FOLDER INTO YOUR MAYA SCRIPT'S FOLDER
#PASTE THE FOLLOWING COMMAND INTO A PYTHON TAB INSIDE SCRIPT EDITOR
#CHANGE "YOUREQUIPMENTNAME" FOR YOUR EQUPMENT'S NAME
#THEN WITH THE MIDDLE MOUSE DRAG IT TO YOUR CUSTOM SHELF


import sys
path_to_scripts_folder = r'C:\Users\YOUREQUIPMENTNAME\Documents\maya\scripts\playblast-project\src'
if path_to_scripts_folder not in sys.path:
    sys.path.append(path_to_scripts_folder)


from ui import playblast_ui

playblast_window = playblast_ui.PlayblastManagerUI()
playblast_window.show()

import maya.cmds as cmds
import os
def create_png_sequence(dir_path, file_name, width, height, start_time=None, end_time=None):

    """ This function creates a sequences of png images based on the input of the user
    Args:
<<<<<<< HEAD
        dir_path (str): The path to the folder you want to store your pngs in
        file_name (str): The name of the file for each png
        width (int): The horizontal size of the image
        height (int): The vertical size of the image
        start_time(int): The start point  from timeline where export begins
        end_time (int): The end point in time line where export ends

    Returns: the value of cmds.playblast
    """
    # get the last frame of the timeline
    if end_time is None:
        end_time = cmds.playbackOptions(query=True, maxTime=True)

    # get the first frame of the timeline
    if start_time is None:
        start_time = cmds.playbackOptions(query=True, minTime=True)

    full_file_name = os.path.join(dir_path, file_name)
=======
        path (str): The path to the folder you want to store your pngs in
        file_name (str): The name of the file for each png
        width (int): The horizontal size of the image
        height (int): The vertical size of the image
    """
>>>>>>> 0097ac1b461f46fb5f1b405193f6bba5810d1d48

    cmds.playblast(
        format='image',          # Output format: 'avi', 'qt', 'movie', etc.
        filename=full_file_name, # Output file path
        compression='png',       # Compression type: 'none', 'avi', 'h264', etc.
        percent= 100,            # Percentage of current view size to use during blasting.
        quality= 100,            # Specify the compression quality factor to use for the movie file
        clearCache=True,         # Clear the cache before the playblast
        viewer=False,            # Do not show the playblast in the viewer
        showOrnaments=False,     # Hide UI elements
        forceOverwrite=True,     # Overwrite existing file
        framePadding=4,          # Number of digits in the frame number
        startTime=start_time,    # Start frame
        endTime=end_time,        # End frame
        widthHeight=(width, height)  # Resolution of the playblast
    )

    return cmds.playblast



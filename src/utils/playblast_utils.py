import maya.cmds as cmds
import os


def create_png_sequence(dir_path, file_name, width, height, start_time=None, end_time=None):

    """ This function creates a sequences of png images based on the input of the user
    Args:

        dir_path (str): The path to the folder you want to store your pngs in
        file_name (str): The name of the file for each png
        width (int): The horizontal size of the image
        height (int): The vertical size of the image
        start_time (int): The start point from timeline where export begins
        end_time (int): The end point in timeline where export ends

    Returns:
         str: The path to the image sequence
    """

    # get the last frame of the timeline
    if end_time is None:
        end_time = cmds.playbackOptions(query=True, maxTime=True)

    # get the first frame of the timeline
    if start_time is None:
        start_time = cmds.playbackOptions(query=True, minTime=True)

    full_file_name = os.path.join(dir_path, file_name.replace(" ", ""))

    playblast_path = cmds.playblast(
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

    return playblast_path

def format_sequence_path(playblast_path):

    """This is a function that exchanges the #### given by maya into a format ffmpeg can manage

    Args:
        playblast_path (str): The path where the image sequence lives

    Returns:
        str: A new string with a .%04d. in the middle of the name instead of the ####
    """

    # Use a regular expression to split the path
    split_path = playblast_path.split('.')

    # The parts before, the #### part, and the parts after
    before_part = split_path[0].replace(" ", "")  # C:\Users\Natalia\Desktop\prueba\prueba
    number_of_padding = split_path[1].count("#")
    middle_part = f'.%0{str(number_of_padding)}d.'
    after_part = split_path[2]  # png

    formatted_path = f"{before_part}{middle_part}{after_part}"

    return formatted_path
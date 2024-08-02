import maya.cmds as cmds

# get the last frame of the timeline
end_time = cmds.playbackOptions(query=True, maxTime=True)

# get the first frame of the timeline
start_time = cmds.playbackOptions(query=True, minTime=True)

def create_sequence_of_pngs(path, file_name, width1, height1):
    """
    Args:
        path(str): stores the name of the folder you want to store your pngs in
        file_name(str): stores the name of the file for each png
        width(int): the horizontal size of the image
        height(int): the vertical size of the image
    """

    full_file_name = f"{path}\\{file_name}"
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
        widthHeight=(width1, height1)  # Resolution of the playblast
    )

# Example usage
create_sequence_of_pngs(r"C:\Users\Natalia\Desktop\prueba", "prueba", 1280, 720)

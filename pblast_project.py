import maya.cmds as cmds

# get the last frame of the timeline
end_time = cmds.playbackOptions(query=True, maxTime=True)

# get the first frame of the timeline
start_time = cmds.playbackOptions(query=True, minTime=True)

#name the file
path = r"C:\Users\Natalia\Desktop\prueba"
file_name = f"{path}\\prueba"

def create_secuence_of_pngs(): #width, height)
    cmds.playblast(
        format='image',          # Output format: 'avi', 'qt', 'movie', etc.
        filename=file_name,      # Output file path
        compression='png',       # Compression type: 'none', 'avi', 'h264', etc.
        clearCache=True,         # Clear the cache before the playblast
        viewer=False,            # Do not show the playblast in the viewer
        showOrnaments=False,     # Hide UI elements
        forceOverwrite=True,     # Overwrite existing file
        framePadding=4,          # Number of digits in the frame number
        startTime=start_time,    # Start frame
        endTime=end_time,        # End frame
        widthHeight=(1280, 720)  # Resolution of the playblast
    )

# Example usage
create_secuence_of_pngs()
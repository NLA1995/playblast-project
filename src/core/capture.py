import maya.cmds as cmds
import os


class PlayblastManager:

    def __init__(self):
        # List to store the paths of exported videos
        self.exported = []

    def do_playblast(self, dir_path, file_name, width, height, start_frame, end_frame):
        """ this function creates a playblast in Maya's viewport and outputs a video

        Args:
            dir_path (str): The folder where the video will be stored
            file_name (str): The name of the file
            width (int): The horizontal size of the video
            height (int): The vertical size of the video
            start_frame (int): The frame from where the video will start
            end_frame (int): The frame where the video ends

        """
        # Ensure the export directory exists
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Construct the full path for the exported file
        file_path = os.path.join(dir_path, f"{file_name}.mov")

        # Set up playblast options in Maya
        cmds.playblast(
            startTime=start_frame,
            endTime=end_frame,
            format="qt",
            filename=file_path,
            sequenceTime=False,
            clearCache=True,
            viewer=False,
            showOrnaments=False,
            fp=4,
            percent=100,
            widthHeight=(width, height),
            compression="H.264"
        )

        # Check if the file was successfully created and add it to the list
        if os.path.exists(file_path):
            self.exported.append(file_path)
            print(f"Exported playblast: {file_path}")
        else:
            print("Error while making playblast: the file was not created.")
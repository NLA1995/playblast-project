import os
import maya.cmds as cmds
from utils.playblast_utils import create_png_sequence
from utils.playblast_utils import format_sequence_path
from utils.ffmpeg_utils import video_from_sequence
from utils.ffmpeg_utils import create_black_bar
from utils.ffmpeg_utils import create_water_mark



class PlayblastManager:
    def __init__(self):
        # List to store the paths of exported videos
        self.exported = []

    def do_playblast(self, dir_path, file_name, water_mark, width, height, start_frame, end_frame):

        """This function creates a playblast in Maya's viewport and outputs a video.

        Args:
            dir_path (str): The folder where the video will be stored.
            file_name (str): The name of the file.
            width (int): The horizontal size of the video.
            height (int): The vertical size of the video.
            start_frame (int): The frame from where the video will start.
            end_frame (int): The frame where the video ends.

        """

        # Ensure the export directory exists
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Construct the full path for the exported file
        file_path = os.path.join(dir_path, f"{file_name}.mov")
        file_path_2 = os.path.join(dir_path, "black_bar.png")
        file_path_3 = os.path.join(dir_path, f"{water_mark}.mov")

        png_sequence = create_png_sequence(dir_path, file_name, width, height, start_frame, end_frame)

        format_path = format_sequence_path(png_sequence)

        video_from_sequence(format_path, file_path, start_frame)

        create_black_bar(file_path_2)

        create_water_mark(file_path, file_path_2, file_path_3)


        # Check if the file was successfully created and add it to the list
        if os.path.exists(file_path_3):
            self.exported.append(file_path_3)
            print(f"Exported playblast: {file_path_3}")
        else:
            print("Error while making playblast: the file was not created.")
import os
import maya.cmds as cmds
from utils.playblast_utils import create_png_sequence
from utils.playblast_utils import format_sequence_path
from utils.ffmpeg_utils import video_from_sequence
from utils.ffmpeg_utils import create_black_bar
from utils.ffmpeg_utils import create_water_mark
import tempfile



class PlayblastManager:
    def __init__(self):
        # List to store the paths of exported videos
        self.exported = []
        # Create temporary folder
        self.temp_dir = tempfile.mkdtemp(prefix='playblast_')

    def do_playblast(self, dir_name, file_name, width, height, start_frame, end_frame):

        """This function creates a playblast in Maya's viewport and outputs a video

        Args:
            dir_name (str) : The folder where the video with watermarks will be stored
            file_name (str): The name of the file
            width (int): The horizontal size of the video
            height (int): The vertical size of the video
            start_frame (int): The frame from where the video will start
            end_frame (int): The frame where the video ends

        """

        # Construct the full path for the exported file
        file_path = os.path.join(self.temp_dir, "no_watermark.mov")
        path_to_black_bar = os.path.join(self.temp_dir, "black_bar.png")
        path_to_watermark = os.path.join(dir_name, f"{file_name}.mov")

        png_sequence = create_png_sequence(self.temp_dir, file_name, width, height, start_frame, end_frame)

        format_path = format_sequence_path(png_sequence)

        video_from_sequence(format_path, file_path, start_frame)

        create_black_bar(path_to_black_bar, width)

        create_water_mark(file_path, path_to_black_bar, path_to_watermark)


        # Check if the file was successfully created and add it to the list
        if os.path.exists(path_to_watermark):
            self.exported.append(path_to_watermark)
            print(f"Exported playblast: {path_to_watermark}")
        else:
            print("Error while making playblast: the file was not created.")
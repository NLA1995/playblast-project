import os
import maya.cmds as cmds
from utils.playblast_utils import create_png_sequence
from utils.playblast_utils import format_sequence_path
from utils.ffmpeg_utils import video_from_sequence
from utils.ffmpeg_utils import create_black_bar
from utils.ffmpeg_utils import create_water_mark
from utils.ffmpeg_utils import add_text_to_watermark
from utils.ffmpeg_utils import add_fcount_overlay
import tempfile



class PlayblastManager:
    def __init__(self, debug=False):
        # List to store the paths of exported videos
        self.exported = []
        # Create temporary folder
        self.temp_dir = tempfile.TemporaryDirectory(prefix='playblast_')

        self.debug = debug

    def do_playblast(self, dir_name, file_name, width, height, frame_rate, start_frame, end_frame, artist_name, department_name, company_name):

        """This function creates a playblast in Maya's viewport and outputs a video

        Args:
            dir_name (str) : The folder where the video with watermarks will be stored
            file_name (str): The name of the file
            width (int): The horizontal size of the video
            height (int): The vertical size of the video
            start_frame (int): The frame from where the video will start
            end_frame (int): The frame where the video ends

        """
        file_name = file_name.replace(" ", "_")
        temp_dir_name = self.temp_dir.name
        if not os.path.exists(temp_dir_name):
            os.mkdir(temp_dir_name)

        # Construct the full path for the exported file
        file_path = os.path.join(temp_dir_name, "no_watermark.mov")
        path_to_black_bar = os.path.join(temp_dir_name, "black_bar.png")
        path_to_watermark = os.path.join(temp_dir_name, f"watermark.mov")
        path_to_video_with_text = os.path.join(temp_dir_name, f"video_with_text.mov")
        path_to_frame_count = os.path.join(dir_name, f"{file_name}.mov")
        artist_name = artist_name
        department_name = department_name
        company_name = company_name

        png_sequence = create_png_sequence(temp_dir_name, file_name, width, height, start_frame, end_frame)

        format_path = format_sequence_path(png_sequence)

        video_from_sequence(frame_rate, format_path, file_path, start_frame)

        create_black_bar(path_to_black_bar, width)

        create_water_mark(file_path, path_to_black_bar, path_to_watermark)

        add_text_to_watermark(path_to_watermark, artist_name, department_name, company_name, path_to_video_with_text)

        add_fcount_overlay(path_to_video_with_text, path_to_frame_count, start_frame)

        #clean temporary directory
        if not self.debug:
            self.temp_dir.cleanup()

        # Check if the file was successfully created and add it to the list
        if os.path.exists(path_to_frame_count):
            self.exported.append(path_to_frame_count)
            print(f"Exported playblast: {path_to_frame_count}")
        else:
            print("Error while making playblast: the file was not created.")

    def do_clean(self, dir_name, file_name, width, height, start_frame, end_frame, artist_name, department_name, company_name):
        file_name = ""
        dir_name = ""
        width = ""
        height = ""
        start_frame = ""
        end_frame = ""
        artist_name = ""
        department_name = ""
        company_name = ""
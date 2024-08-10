import os
from os.path import join

# Define repository path via environment variable
repo_path = os.getenv("REPO_PATH", r"C:\Users\Natalia\Desktop\repositorios\playblast-project")
EXECUTABLE = join(repo_path, 'bin', 'ffmpeg', 'bin', 'ffmpeg.exe')


def format_sequence_path(playblast_path):

    """This is a function that exchanges the #### given by maya into a format ffmpeg can manage

    Args:
        playblast_path (str): The string given by the function in playblast_utils, create_png_sequence

    Returns:
        str: A new string with a .%04d. in the middle of the name instead of the ####
    """

    # Use a regular expression to split the path
    split_path = playblast_path.split('.')

    # The parts before, the #### part, and the parts after
    before_part = split_path[0]  # C:\Users\Natalia\Desktop\prueba\prueba
    middle_part = '.%04d.'
    after_part = split_path[2]  # png

    formatted_path = f"{before_part}{middle_part}{after_part}"
    return formatted_path


def video_from_sequence(formatted_path, output_video, start_frame=None):

    """This function creates a video based on a sequence of images

    Args:
        formatted_path (str): The return value of the function format_sequence_path
        output_video (str): The location where we want the video stored
        start_frame (int): The point from when we want the video to start

    """

    if start_frame is None:
        start_frame = 1
    run = f"{EXECUTABLE} -framerate 24 -start_number {start_frame} -i {formatted_path} -c:v libx264 -pix_fmt yuv420p -y {output_video}"
    os.system(run)

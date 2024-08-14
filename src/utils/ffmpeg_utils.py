import os
from os.path import join, dirname


# Define repository path via environment variable
repo_path = dirname(dirname(dirname(__file__)))
EXECUTABLE = join(repo_path, 'bin', 'ffmpeg', 'bin', 'ffmpeg.exe')

def video_from_sequence(formatted_path, output_video, start_frame=None):

    """This function creates a video based on a sequence of images

    Args:
        formatted_path (str): The necessary path to output the video
        output_video (str): The location where we want the video stored
        start_frame (int): The point from when we want the video to start

    """

    if start_frame is None:
        start_frame = 1
    run = f"{EXECUTABLE} -framerate 24 -start_number {start_frame} -i {formatted_path} -c:v libx264 -pix_fmt yuv420p -y {output_video}"
    os.system(run)

    if not os.path.exists(output_video):
        raise RuntimeError(f"Failed to create video from sequence path: {formatted_path}")
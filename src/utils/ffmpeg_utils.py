import os
import subprocess
from os.path import join, dirname

# Define repository path via environment variable
repo_path = dirname(dirname(dirname(__file__)))
EXECUTABLE = join(repo_path, 'bin', 'ffmpeg', 'bin', 'ffmpeg.exe')


def video_from_sequence(frame_rate, formatted_path, output_video, start_frame=None):

    """
    This function creates a video based on a sequence of images.

    Args:
        formatted_path (str): The necessary path to output the video.
        output_video (str): The location where we want the video stored.
        start_frame (int): The point from when we want the video to start.

    """

    if start_frame is None:
        start_frame = 1
    command = f"{EXECUTABLE} -framerate {frame_rate} -start_number {start_frame} -i {formatted_path} -c:v libx264 -pix_fmt yuv420p -y {output_video}"
    run_subprocess(command)

    if not os.path.exists(output_video):
        raise RuntimeError(f"Failed to create video from sequence path: {formatted_path}")

    return(output_video)


def create_black_bar(output_file_path, width):
    """
    This function creates a file with a black bar.

    Args:
        output_file_path(str): The name of the path where the black bar will be stored.
        width(int): The horizontal size of the black bar.

    """
    command = f"{EXECUTABLE} -f lavfi -i color=black:{width}x80:d=3,format=rgb24 -frames:v 1 -y {output_file_path}"
    run_subprocess(command)


def create_water_mark(input_video_path, black_bar_path, output_video_path):
    """
    This function creates 2 watermarks on the top and bottom of the video.

    Args:
        input_video_path(str): The path of the initial video without the watermark.
        black_bar_path(str): The path of the black bar.
        output_video_path(str): The path where the video with the watermark will be stored.

    """
    command = (f"{EXECUTABLE} -i {input_video_path} -i {black_bar_path} -i {black_bar_path} "
            f"-y -filter_complex [1]lut=a=val*0.1[bar1];[2]lut=a=val*0.1[bar2];[0][bar1]overlay=x=(W-w)/2:y=0[video_with_top];[video_with_top][bar2]overlay=x=(W-w)/2:y=H-h {output_video_path}")
    run_subprocess(command)


def add_text_to_watermark(input_video_path, artist_name, department_name, company_name, output_video_path):
    """
    This function adds the text on top of the black bars
    Args:
        input_video_path(str): The path of the initial video with the black bars
        artist_name(str): The name of the artist inputted by the user
        department_name(str): The name of the department inputted by the user
        company_name(str): The name of the company inputted by the user
        output_video_path(str): The path where the video with the info will be stored.

    """
    command = (
        f"{EXECUTABLE} -i {input_video_path} -vf "
        f"\"drawtext=text='{artist_name}':fontfile='Arial':fontsize=50:fontcolor=white:x=10:y=25\","
        f"drawtext=text='{department_name}':fontfile='Arial':fontsize=50:fontcolor=white:x=w-text_w-10:y=25\","
        f"drawtext=text='{company_name}':fontfile='Arial':fontsize=50:fontcolor=white:x=10:y=h-text_h-10\" "
        f"-codec:a copy -y {output_video_path}"
    )

    run_subprocess(command)


def add_current_frame_overlay(input_video_path, output_video_path, start_frame):
    """
    This function adds the current frame count on the right bottom corner of the video
    Args:
        input_video_path(str): The path of the initial video with the other info
        output_video_path(str): The path where the video with the info will be stored
        start_frame(str): The number of frame where the video starts

    Returns:

    """
    # Create the command to overlay FPS on the video
    command = (
        f"{EXECUTABLE} -i {input_video_path} -vf "
        f"drawtext=fontfile='Arial':"
        "x=w-tw-10:y=h-th-10:"
        "fontcolor=white:fontsize=40:box=1:boxcolor=black@0.5:"
        f"text='%{{frame_num}}':"
        f"start_number={start_frame} "
        f"-codec:a copy -y {output_video_path}"
    )

    process, stderr = run_subprocess(command)

    if process.returncode != 0:
        print(f"Error: {stderr.decode()}")
    else:
        print(f"Frame count overlay added successfully to {output_video_path}")


def run_subprocess(command):
    """
    This function takes care of running the command in the background
    Args:
        command (str): a ffmpeg line of code
    """
    # Run the command using subprocess
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process, stderr

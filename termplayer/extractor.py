import imageio
import imageio_ffmpeg as ffmpeg
from PIL import Image
import subprocess
import os

def extract_frames(path, width, height):
    reader = imageio.get_reader(path)
    for i, frame in enumerate(reader):
        image = Image.fromarray(frame)
        image = image.resize((width, height))
        image.save(f"../resources/frames/frame_{i}.bmp", format="BMP")

def extract_audio(path, output):
    ffmpeg_cmd = ffmpeg.get_ffmpeg_exe()

    command = [
        ffmpeg_cmd,
        "-i", path,
        "-vn",
        "-acodec", "mp3",
        output
    ]

    with open(os.devnull, 'w') as devnull:
        subprocess.run(command, check=True, stdout=devnull, stderr=devnull)

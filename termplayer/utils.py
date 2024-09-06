import imageio
import logging
import os
import shutil
import re

def setup_logging(log_level):
    logging.basicConfig(level=getattr(logging, log_level.upper()))

def cleanup_resources():
    resources = "../resources"
    if os.path.exists(resources):
        shutil.rmtree(resources)
    os.mkdir(resources)
    os.mkdir(resources + "/frames")

def natural_sort(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split("([0-9]+)", s)]

def get_video_fps(path):
    reader = imageio.get_reader(path)
    fps = reader.get_meta_data()["fps"]
    return fps

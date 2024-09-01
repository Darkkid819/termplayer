from extractor import extract_frames
from utils import cleanup_resources
from convertor import frame_to_ascii
from PIL import Image
import os
import curses

class Player:
    def __init__(self, stdscr, path, width, height, fps, audio=True):
        self.stdscr = stdscr
        self.path = path
        self.width = width
        self.height = height
        self.fps = fps
        self.audio = audio

        cleanup_resources()

        extract_frames(self.path, self.width, self.height)

    def play(self):
        frame_dir = "../resources/frames"
        frame_files = sorted(os.listdir(frame_dir))

        for frame_file in frame_files:
            frame_path = os.path.join(frame_dir, frame_file)
            ascii_frame = frame_to_ascii(frame_path, self.stdscr)
            # print(ascii_frame)
            # self.stdscr.clear()
            # self.stdscr.refresh()

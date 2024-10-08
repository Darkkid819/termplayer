from extractor import extract_audio, extract_frames
from utils import cleanup_resources, natural_sort
from convertor import frame_to_ascii
from renderer import render_frame
from PIL import Image
import os
import curses
import pygame

class Player:
    def __init__(self, stdscr, path, width, height, fps, audio=True):
        self.stdscr = stdscr
        self.path = path
        self.width = width
        self.height = height
        self.fps = fps
        self.audio = audio

        # Display the progress of each step in the terminal
        self.display_message("Cleaning up resources...")
        cleanup_resources()

        self.display_message("Extracting frames...")
        extract_frames(self.path, self.width, self.height)

        if self.audio:
            self.display_message("Extracting audio...")
            extract_audio(self.path, "../resources/audio.mp3")

        self.display_message("Setup complete. Playing video...")

    def play(self):
        frame_dir = "../resources/frames"
        frame_files = sorted(os.listdir(frame_dir), key=natural_sort)
        frame_delay = int(1000 / self.fps)

        if self.audio:
            pygame.mixer.init()
            pygame.mixer.music.load("../resources/audio.mp3")
            pygame.mixer.music.play()

        for frame_file in frame_files:
            frame_path = os.path.join(frame_dir, frame_file)
            ascii_frame = frame_to_ascii(frame_path, self.stdscr)
            render_frame(self.stdscr, ascii_frame)
            curses.napms(frame_delay)

            if self.audio and not pygame.mixer.music.get_busy():
                break

        if self.audio:
            pygame.mixer.music.stop()

    def display_message(self, message):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, message)
        self.stdscr.refresh()
        curses.napms(1000)  

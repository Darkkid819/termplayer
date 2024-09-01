from extractor import extract_frames
from utils import cleanup_resources

class Player:
    def __init__(self, path, width, height, fps, audio=True):
        self.path = path
        self.width = width
        self.height = height
        self.fps = fps
        self.audio = audio

        cleanup_resources()

        extract_frames(self.path, self.width, self.height)

    def play(self):
        pass

import argparse
from player import Player
from utils import get_video_fps, setup_logging
import curses
import sys

def parse_arguments():
    parser = argparse.ArgumentParser("TermPlayer: Play videos as ASCII art in the terminal")
    parser.add_argument("--path", type=str, help="Path to the video file")
    parser.add_argument("--width", type=int, default=80, help="Width of the ASCII output")
    parser.add_argument("--height", type=int, default=60, help="Height of the ASCII output")
    parser.add_argument("--fps", type=int, default=24, help="Playback frames per second")
    parser.add_argument("--no-audio", action="store_true", help="Disable audio playback")
    parser.add_argument("--log-level", type=str, default="INFO", help="Set the logging level (DEBUG, INFO, WARNING, ERROR)")
    return parser.parse_args()

def main(stdscr):
    curses.curs_set(0)
    args = parse_arguments()
    setup_logging(args.log_level)

    if not args.path or not args.path.strip():
        print("Error: you must provide a valid video file path.")
        sys.exit(1)

    player = Player(
        stdscr=stdscr,
        path=args.path,
        width=args.width,
        height=args.height,
        fps=args.fps,
        audio=not args.no_audio
    )
    player.fps=get_video_fps(player.path)

    player.play()

if __name__ == "__main__":
    curses.wrapper(main)

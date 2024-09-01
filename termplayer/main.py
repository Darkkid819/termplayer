import argparse
from player import Player
from utils import setup_logging

def parse_arguments():
    parser = argparse.ArgumentParser("TermPlayer: Play videos as ASCII art in the terminal")
    parser.add_argument("--path", type=str, help="Path to the video file")
    parser.add_argument("--width", type=int, default=80, help="Width of the ASCII output")
    parser.add_argument("--height", type=int, default=60, help="Height of the ASCII output")
    parser.add_argument("--fps", type=int, default=24, help="Playback frames per second")
    parser.add_argument("--no-audio", action="store_true", help="Disable audio playback")
    parser.add_argument("--log-level", type=str, default="INFO", help="Set the logging level (DEBUG, INFO, WARNING, ERROR)")
    return parser.parse_args()

def main():
    args = parse_arguments()
    setup_logging(args.log_level)

    player = Player(
        path=args.path,
        width=args.width,
        height=args.height,
        fps=args.fps,
        audio=not args.no_audio
    )

    player.play()

if __name__ == "__main__":
    main()

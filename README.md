# ASCII Video Player

An ASCII video player that takes a video file, extracts its frames, converts them to ASCII art, and plays the video in the terminal, synchronized with audio playback.

## Features

- Converts video frames to ASCII art and displays them in the terminal.
- Synchronizes audio playback with the video frames.
- Supports frame rate detection and automatic synchronization with the terminal’s width and height.
- Extracts audio and plays it alongside the ASCII video using `pygame`.
- Uses `ffmpeg` to extract frames and audio from the input video.

## Requirements

To run the ASCII video player, you need the following dependencies:

### Python Packages
- `imageio`
- `imageio-ffmpeg`
- `Pillow`
- `pygame`
- `curses` (built-in on Unix systems, `windows-curses` on Windows)
  
### Install Dependencies

You can install the required dependencies using `pip`:

```bash
pip install imageio imageio-ffmpeg pygame Pillow
```

For Windows users, install `windows-curses`:

```bash
pip install windows-curses
```

### FFmpeg

Make sure you have `ffmpeg` installed on your system for frame and audio extraction.

- On Ubuntu:
  ```bash
  sudo apt install ffmpeg
  ```
  
- On macOS:
  ```bash
  brew install ffmpeg
  ```

- On Windows, download from [ffmpeg.org](https://ffmpeg.org/download.html) and ensure it is added to your `PATH`.

## Usage

### Running the Program

To run the program, you need to provide the path to a video file. The program will extract frames, convert them to ASCII, and synchronize with audio playback.

Example usage:

```bash
python main.py <path_to_video.mp4>
```

### Command-Line Arguments

- `video_path`: The path to the input video file.
- `width`: The desired width of the terminal (default: terminal width).
- `height`: The desired height of the terminal (default: terminal height).
- `fps`: The frames per second (FPS) to synchronize the video with.
- `audio`: A boolean flag to enable or disable audio playback (default: `True`).

### Example

```bash
python main.py your_video.mp4

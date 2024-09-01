from PIL import Image
import curses

def frame_to_ascii(frame, stdscr):
    height, width = stdscr.getmaxyx()

    image = Image.open(frame)
    image = image.convert("L")
    image = image.resize((width, height))

    charset = "@%#*+=-:. "

    pixels = image.getdata()
    ascii_str = "".join([charset[pixel // 32] for pixel in pixels])
    
    ascii_img = "\n".join([ascii_str[i:i + (width - 1)] for i in range(0, len(ascii_str), width)])
    return ascii_img

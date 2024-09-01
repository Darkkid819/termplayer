import imageio
from PIL import Image

def extract_frames(path, width, height):
    reader = imageio.get_reader(path)
    for i, frame in enumerate(reader):
        image = Image.fromarray(frame)
        image = image.resize((width, height))
        image.save(f"../resources/frames/frame_{i}.bmp", format="BMP")

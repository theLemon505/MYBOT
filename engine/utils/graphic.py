import sys
from PIL import Image
from termcolor import colored
import colorama

class Graphic:
    def __init__(self, image):
        self.image = Image.open(image)
        colorama.init()

    def draw(self):
        width, height = self.image.size
        aspect_ratio = height/width
        new_width = 120
        new_height = aspect_ratio * new_width * 0.55
        img = self.image.resize((new_width, int(new_height)))
        img = img.convert('L')
        pixels = img.getdata()
        chars = ["B", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
        new_pixels = [chars[pixel//25] for pixel in pixels]
        new_pixels = ''.join(new_pixels)
        new_pixels_count = len(new_pixels)
        ascii_image = [new_pixels[index:index + new_width]
            for index in range(0, new_pixels_count, new_width)]
        ascii_image = "\n".join(ascii_image)
        print(ascii_image)
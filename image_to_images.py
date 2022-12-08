# Image Converter to Images Module
# Requirements: ImageMagick (for windows) https://imagemagick.org/script/download.php#windows
# How to: using command line
# Project starter: Martin Alvarez

# from wand.image import Image
import subprocess


class Converter:  # Parent class
    def __int__(self, input_file, output_file):  # args, kwargs?
        self.input_file = input_file
        self.output_file = output_file
        # self.convert() # ?

    def convert(self):
        pass


class ImageConverter(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):  # Convert image to any type
        picture = self.input_file
        output_file = self.output_file
        command_line = ['magick', f'{picture}', f'{output_file}']
        return subprocess.Popen(command_line)


image_converted = ImageConverter('RickandMorty.jpg', 'RickandMorty.png').convert()


class ImageFlip(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):   # Flip image horizontally
        picture = self.input_file
        output_file = self.output_file
        command_line = ['magick', f'{picture}', '-flip', f'{output_file}']
        return subprocess.Popen(command_line)


image_flip = ImageFlip('RickandMorty.jpg', 'RickandMorty_flip.jpg').convert()


class ImageRotate(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):  # Rotate image clockwise   #Add parameters (grades)
        picture = self.input_file
        output_file = self.output_file
        command_line = ['magick', f'{picture}', '-rotate', f'90', f'{output_file}']
        return subprocess.Popen(command_line)


image_rotate = ImageRotate('RickandMorty.jpg', 'RickandMorty_rotate.jpg').convert()


class ImageBN(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):  # Convert image to black and white
        picture = self.input_file
        output_file = self.output_file
        command_line = ['magick', f'{picture}', '-monochrome', f'{output_file}']
        return subprocess.Popen(command_line)


image_bn = ImageBN('RickandMorty.jpg', 'RickandMorty_BN.jpg').convert()


class ImageResize(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):  # Resize image to a given % or values
        picture = self.input_file
        output_file = self.output_file
        command_line = ['magick', f'{picture}', '-resize', f'50%', f'{output_file}']
        return subprocess.Popen(command_line)


image_resize = ImageResize('RickandMorty.jpg', 'RickandMorty_resize.jpg').convert()

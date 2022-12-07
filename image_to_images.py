# Image Converter to Images Module
# Requirements: ImageMagick (for windows) https://imagemagick.org/script/download.php#windows
# wand.image info: https://www.pythonpool.com/imagemagick-python/
# How to: using command line (In progress)
# Project starter: Martin Alvarez

from wand.image import Image
# import subprocess, os


class Converter:  # Parent class
    def __int__(self, input_file, output_file):  # **k?
        self.input_file = input_file
        self.output_file = output_file
        # self.convert() # ?

    def convert(self):
        pass


class ImageConverter(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file  # ask Paolo, is it necessary to repeat this?

    def convert(self):  # Convert image to any type
        picture = self.input_file
        output_file = self.output_file
        name = picture.split('.')
        convert_picture = Image(filename=picture)
        convert_picture = convert_picture.convert('png')
        convert_picture.save(filename=output_file)
        # convert_picture.save(filename=f'/images/{name[0]}.png')
        return print(f"Convert image from {name[1]} to {'png'} successfully")

image_converted = ImageConverter('RickandMorty.jpg', 'RickandMorty.png').convert()

# conv_command = f'ffmpeg -i {source} -r 1 {destination}'
# b = subprocess.Popen(['ffmpeg',param_input,'file_example_MP4_1920_18MG.mp4','-r','1','image%06d.jpg'])
# print("The exit code was: %d"%b)


class ImageFlip(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):   # Flip image horizontally
        picture = self.input_file
        output_file = self.output_file
        name = picture.split('.')
        flip_picture = Image(filename=picture)
        flip_picture.flip()
        flip_picture.save(filename=output_file)
        # flip_picture.save(filename=f'{name[0]}_flip.{name[1]}')
        return print(f"Flip image {name[0]} successfully")

image_flip = ImageFlip('RickandMorty.jpg', 'RickandMorty_flip.jpg').convert()


class ImageRotate(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):  # Rotate image clockwise
        picture = self.input_file
        output_file = self.output_file
        name = picture.split('.')
        rotate_picture = Image(filename=picture)
        rotate_picture.rotate(45)  # grades
        rotate_picture.save(filename=output_file)
        #rotate_picture.save(filename=f'{name[0]}_rotate_{grades}.{name[1]}')
        return print(f"Rotate image {name[0]} 45° grades successfully")

image_rotate = ImageRotate('RickandMorty.jpg', 'RickandMorty_rotate.jpg').convert()


class ImageBN(Converter):  # Child class
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):  # Convert image to black and white
        picture = self.input_file
        output_file = self.output_file
        name = picture.split('.')
        bn_picture = Image(filename=picture)
        bn_picture.transform_colorspace('gray')
        bn_picture.sketch(0.5, 0.0, 98.0)
        bn_picture.save(filename=output_file)
        # bn_picture.save(filename=f'{name[0]}_bn.{name[1]}')
        return print(f"Convert image {name[0]} to black and white successfully")

image_bn = ImageBN('RickandMorty.jpg', 'RickandMorty_BN.jpg').convert()




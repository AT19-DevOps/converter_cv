#
# @image_to_images.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from CONVERTER.src.com.jalasoft.converter.model.converter import Converter
from CONVERTER.src.com.jalasoft.converter.model.command_line import Command


class ImageConverter(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self) -> list:
        """Converts image to any type, returns the command line"""
        command_line = ['magick', f'{self.input_file}', f'{self.output_file}']
        return command_line


class ImageFlip(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self) -> list:
        """Flips image horizontally, returns the command line"""
        command_line = ['magick', f'{self.input_file}', '-flip', f'{self.output_file}']
        return command_line


class ImageRotate(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file, grades):
        super().__init__(input_file, output_file)
        self.grades = grades

    def convert(self) -> list:
        """Rotates image clockwise for a given value, returns the command line"""
        command_line = ['magick', f'{self.input_file}', '-rotate', f'{self.grades}', f'{self.output_file}']
        return command_line


class ImageBW(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self) -> list:
        """Converts image to black and white, returns the command line"""
        command_line = ['magick', f'{self.input_file}', '-monochrome', f'{self.output_file}']
        return command_line


class ImageResize(Converter):
    """ Inherits Converter criteria"""
    def __init__(self, input_file, output_file, new_size):
        super().__init__(input_file, output_file)
        self.new_size = new_size

    def convert(self) -> list:
        """ Resizes image to a given % or values, returns the command line"""
        command_line = ['magick', f'{self.input_file}', '-resize', f'{self.new_size}', f'{self.output_file}']
        return command_line


image_converted = Command(ImageConverter('RickandMorty.jpg', 'RickandMorty.png').convert()).run_cmd()
image_flip = Command(ImageFlip('RickandMorty.jpg', 'RickandMorty_flip.jpg').convert()).run_cmd()
image_rotate = Command(ImageRotate('RickandMorty.jpg', 'RickandMorty_rotate.jpg', 90).convert()).run_cmd()
image_bn = Command(ImageBW('RickandMorty.jpg', 'RickandMorty_BW.jpg').convert()).run_cmd()
image_resize = Command(ImageResize('RickandMorty.jpg', 'RickandMorty_resize.jpg', '50%').convert()).run_cmd()
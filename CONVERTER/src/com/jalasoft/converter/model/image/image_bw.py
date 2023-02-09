#
# @image_bw.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from CONVERTER.src.com.jalasoft.converter.common.exception.converter_exception import ConverterException
from CONVERTER.src.com.jalasoft.converter.common.valid_data import Validations
from CONVERTER.src.com.jalasoft.converter.model.converter import Converter


class ImageBW(Converter):
    """ Inherits Converter criteria"""

    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self) -> str:
        """Converts image to black and white, returns the command line"""
        Validations().validate_directory(self.input_file, 'imaBWima-')
        Validations().validate_input(self.input_file, 'imaBWima-')
        Validations().validate_output(self.output_file, 'imaBWima-')
        Validations().validate_directory(self.output_file, 'imaBWima-')
        try:
            command_line = ['magick', f'{self.input_file}', '-monochrome', f'{self.output_file}']
            return " ".join(command_line)
        except Exception as error:
            raise ConverterException('Create Image to Black and Withe command error')

# @audio_converter.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.

from CONVERTER.src.com.jalasoft.converter.model.converter import Converter


# Inherits Converter criteria
class AudioConvert(Converter):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    # Creates a command to converts audio format
    def convert(self):
        cmd = f'ffmpeg -i {self.input_file} {self.output_file}'
        return cmd

# Inherits Converter criteria
class IncreaseVolume(Converter):
    def __init__(self, input_file, output_file, multiplier):
        super().__init__(input_file, output_file)
        self.multiplier = multiplier

    # Creates a command to increases the volume of an audio
    def convert(self):
        cmd = f'ffmpeg -i {self.input_file} -af "volume={self.multiplier}" {self.output_file}'
        return cmd

# Inherits Converter criteria
class ExtractAudio(Converter):
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    # Creates a command to extracts the audio from a video
    def convert(self):
        cmd = f'ffmpeg -i {self.input_file} -vn {self.output_file}'
        return cmd

# Inherits Converter criteria
class MixAudio(Converter):
    def __init__(self, input_file, output_file, second_input):
        super().__init__(input_file, output_file)
        self.second_input = second_input
    # Creates a command to mixes two audios
    def convert(self):
        cmd = f'ffmpeg -i {self.input_file} -i {self.second_input} -filter_complex amerge {self.output_file}'
        return cmd






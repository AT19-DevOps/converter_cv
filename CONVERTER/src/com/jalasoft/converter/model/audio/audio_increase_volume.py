# @audio_increase_volume.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.

from model.converter import Converter


class IncreaseVolume(Converter):
    """Inherits Converter criteria"""
    def __init__(self, input_file, output_file, multiplier):
        super().__init__(input_file, output_file)
        self.multiplier = multiplier

    def convert(self):
        """Creates a command to increases the volume of an audio"""
        cmd = f'ffmpeg -i {self.input_file} -af "volume={self.multiplier}" {self.output_file}'
        return cmd

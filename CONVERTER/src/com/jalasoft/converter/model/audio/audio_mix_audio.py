#
# @audio_mix_audio.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from CONVERTER.src.com.jalasoft.converter.model.converter import Converter


class MixAudio(Converter):
    """Inherits Converter criteria"""
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)

    def convert(self):
        list = ['ffmpeg']
        for element in self.input_file:
            list.append(' -i ' + element)
        list.append(' -filter_complex amerge '+self.output_file)
        cmd = ''.join(list)
        return cmd

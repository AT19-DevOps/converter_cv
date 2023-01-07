#
# @vconverter.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
#
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from model.converter import Converter
from model.video.paths import Path


class VideoToImages(Converter):
    """Converts any video format to a set of any format images""" 
    def __init__(self, input_file, output_file, fps): 
        super().__init__(input_file, output_file) 
        self.fps = fps        
        
    def convert(self):
        """Converts video to a set of images"""
        paths = Path(self.input_file, self.output_file).paths()
        return " ".join(['ffmpeg', '-i', paths[0], '-r', self.fps, paths[1]])

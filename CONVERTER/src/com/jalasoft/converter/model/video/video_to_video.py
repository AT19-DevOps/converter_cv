#
# @video_to_video.py Copyright (c) 2022 Jalasoft.
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


class VideoToVideo(Converter):
    """Converts any video format to another video format""" 
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)
    
    def convert(self):
        """Converts video formats"""
        return " ".join(['ffmpeg', '-i',  self.input_file, '-c:v copy -c:a copy -y', self.output_file])

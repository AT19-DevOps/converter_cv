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

from command_line import Command
from paths import Path
from converter import Converter


# Converts any video format to a set of any format images 
class VideoToImages(Converter):
    def __init__(self, input_file, output_file, fps): 
        super().__init__(input_file, output_file) 
        self.fps = fps        
    
    # Converts video to a set of images    
    def convert(self):
        paths = Path(self.input_file, self.output_file).paths()
        return  Command(['ffmpeg', '-i', paths[0], '-r', self.fps, paths[1]]).run_cmd()
    

# Converts any video format to another video format 
class VideoToVideo(Converter): 
    def __init__(self, input_file, output_file):
        super().__init__(input_file, output_file)
    
    # Converts video format
    def convert(self):
        paths = Path(self.input_file, self.output_file).paths()
        return  Command(['ffmpeg', '-i', paths[0], '-c:v copy -c:a copy -y', paths[1]]).run_cmd()



#
# @paths.py Copyright (c) 2022 Jalasoft.
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

import subprocess
import os


class Path:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        
    def paths(self):
        BASE_DIR = os.getcwd()
        destination_dir = os.path.join(BASE_DIR, self.input_file.split(".")[0])
        source = os.path.join(BASE_DIR, self.input_file)
        if not os.path.exists(destination_dir): os.mkdir(destination_dir)
        destination = os.path.join(destination_dir, self.output_file)
        print(source, "\n", destination)
        return [source, destination] 
#
# @metadata.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
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
import json


class ExifTool(object):
    """Obtiene metadatos"""
    sentinel = "{ready}\r\n"

    def __init__(self, executable="exiftool(-k).exe"):
        """Configures the exiftool(-k).exe"""    
        self.executable = executable
        self.process = subprocess.Popen(
            [self.executable, "-stay_open", "True",  "-@", "-"],
            universal_newlines=True,
            stdin=subprocess.PIPE, stdout=subprocess.PIPE)

    def __exit__(self, exc_type, exc_value, traceback):
        """Completes the metadata process"""  
        self.process.stdin.write("-stay_open\nFalse\n")
        self.process.stdin.flush()

    def execute(self, *args):
        """Calls our tool, it loads files and reads them metadata"""  
        args = args + ("-execute\n",)
        self.process.stdin.write(str.join("\n", args))
        self.process.stdin.flush()
        output = ""
        fd = self.process.stdout.fileno()
        while not output.endswith(self.sentinel):
            output += os.read(fd, 4096).decode('utf-8')
        return output[:-len(self.sentinel)]

    def get_metadata(self, *filenames):
        """Loads metadata in a jeyson and that prints"""  
        return json.loads(self.execute("-G", "-j", "-n", *filenames))
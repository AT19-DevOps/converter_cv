#
# @command_line.py Copyright (c) 2022 Jalasoft.
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
import platform


class Command:
    """Defines Command class criteria"""
    def __init__(self, cmd):
        self.cmd = cmd

    def run_cmd(self):
        """Executes the command given"""
        cmd_line = self.cmd
        if platform.system() == 'Linux':
            cmd_line = str(cmd_line).replace('magick', 'convert')
        try:
            run = subprocess.check_output(cmd_line, shell=True)
            return run
        except subprocess.CalledProcessError:
            raise Exception('Command line error: Please verify syntax: ', cmd_line)
        except:
            raise Exception('Command line error: Invalid parameters', cmd_line)

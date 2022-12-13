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


class Command:
    """Defines Command class criteria"""
    def __init__(self, cmd):
        self.cmd = cmd

    def run_cmd(self):
        """Executes the command given"""
        return subprocess.Popen(self.cmd)

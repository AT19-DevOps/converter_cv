#
# @ep_audio_to_audio.py Copyright (c) 2023 Jalasoft.
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

from flask_restful import Resource
from CONVERTER.src.com.jalasoft.converter.common.command_line import Command
from CONVERTER.src.com.jalasoft.converter.controler.mange_request import ManageData
from CONVERTER.src.com.jalasoft.converter.model.audio.audio_converter import AudioConvert


class AudioToAudio(Resource):
    """Defines audio to audio class"""
    def post(self):
        """Convert audio to another type of audio"""
        files = ManageData().generate_path('audToaud-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(AudioConvert(file_in, file_out).convert()).run_cmd()
            return url

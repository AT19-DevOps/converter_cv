#
# @ep_audio_mix_audio.py Copyright (c) 2023 Jalasoft.
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

import os
from flask import request
from flask_restful import Resource
from werkzeug.utils import secure_filename
from CONVERTER.src.com.jalasoft.converter.common.command_line import Command
from CONVERTER.src.com.jalasoft.converter.controler.config import UPLOAD_FOLDER
from CONVERTER.src.com.jalasoft.converter.controler.config import RESPONSE_FOLDER
from CONVERTER.src.com.jalasoft.converter.model.audio.audio_mix_audio import MixAudio


class AudioMixAudio(Resource):
    """Defines audio mix audio class"""

    def post(self):
        """Mixes two audios"""
        input_file_1 = request.files["input_file_1"]
        input_file_2 = request.files["input_file_2"]
        output_file = request.form["output_file"]
        if input_file_2 and input_file_2 and output_file:
            filename_1 = secure_filename(input_file_1.filename)
            filename_2 = secure_filename(input_file_2.filename)
            audio_name = filename_1[0:-4] + '-Mix-' + filename_2[0:-4] + output_file
            input_file_1.save(os.path.join(UPLOAD_FOLDER, filename_1))
            input_file_2.save(os.path.join(UPLOAD_FOLDER, filename_2))
            input_audio_1 = os.path.join(UPLOAD_FOLDER, filename_1)
            input_audio_2 = os.path.join(UPLOAD_FOLDER, filename_2)
            input_list = [input_audio_1, input_audio_2]
            cmd = MixAudio(input_list, RESPONSE_FOLDER + "\\" + audio_name).convert()
            Command(cmd).run_cmd()
            url = 'http://localhost:5000/download?file_name=' + audio_name
            return url

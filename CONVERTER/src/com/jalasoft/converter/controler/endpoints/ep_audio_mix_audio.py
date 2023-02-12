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
from common.command_line import Command
from common.exception.convert_exception import ConvertException
from config import UPLOAD_FOLDER
from config import RESPONSE_FOLDER
from config import DOWNLOAD_DIR
from model.audio.audio_mix_audio import MixAudio


class AudioMixAudio(Resource):
    """Defines audio mix audio class"""

    def post(self):
        """Mixes two audios"""
        input_file_1 = request.files["input_file_1"]
        input_file_2 = request.files["input_file_2"]
        output_file = request.form["output_file"]
        try:
            if input_file_1 and input_file_2 and output_file:
                filename_1 = secure_filename(input_file_1.filename)
                filename_2 = secure_filename(input_file_2.filename)
                audio_name = os.path.basename(filename_1).split('.')[0] + '-Mix-' + \
                             os.path.basename(filename_2).split('.')[0] + output_file
                input_file_1.save(os.path.join(UPLOAD_FOLDER, filename_1))
                input_file_2.save(os.path.join(UPLOAD_FOLDER, filename_2))
                input_audio_1 = os.path.join(UPLOAD_FOLDER, filename_1)
                input_audio_2 = os.path.join(UPLOAD_FOLDER, filename_2)
                input_list = [input_audio_1, input_audio_2]
                cmd = MixAudio(input_list, os.path.join(RESPONSE_FOLDER, audio_name)).convert()
                Command(cmd).run_cmd()
                url = DOWNLOAD_DIR + audio_name
                return {'download_URL': url}
            else:
                response = {'error message': 'File is corrupted'}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400

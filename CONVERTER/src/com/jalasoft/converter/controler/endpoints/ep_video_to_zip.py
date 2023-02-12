#
# @ep_video_to_zip.py Copyright (c) 2023 Jalasoft.
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
from common.command_line import Command
from common.exception.convert_exception import ConvertException
from common.zip_file import ZipFiles
from config import RESPONSE_FOLDER
from config import DOWNLOAD_DIR
from controler.routes import validate_inputs
from model.video.vconverter import VideoToImages


class VideoToZip(Resource):
    """Defines video to zip class"""
    def post(self):
        """Create zip file containing image from video. This class is for PyQTs Team :)"""
        files = validate_inputs('')
        try:
            if files:
                output_format = str(request.args["output_file"])
                fps = str(request.args["fps"])
                file_in = files[0]
                file_name = '/' + os.path.basename(file_in).split('.')[0] + '/'
                os.makedirs(file_in.split('.')[0] + file_name, exist_ok=True)
                file_out = file_in.split('.')[0] + file_name + '%06d.' + output_format
                Command(VideoToImages(file_in, file_out, fps).convert()).run_cmd()
                tmp_zip = ZipFiles(file_in.split('.')[0], file_in.split('.')[0] + '/', RESPONSE_FOLDER).compress()
                url = DOWNLOAD_DIR + os.path.basename(tmp_zip)
                return {'download_URL': url}
            else:
                response = {'error message': 'File is corrupted'}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400

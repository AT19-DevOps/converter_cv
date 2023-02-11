#
# @ep_video_to_zip_image.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.common.command_line import Command
from CONVERTER.src.com.jalasoft.converter.common.exception.convert_exception import ConvertException
from CONVERTER.src.com.jalasoft.converter.common.zip_file import ZipFiles
from CONVERTER.src.com.jalasoft.converter.config import RESPONSE_FOLDER
from CONVERTER.src.com.jalasoft.converter.config import DOWNLOAD_DIR
from CONVERTER.src.com.jalasoft.converter.controler.routes import validate_inputs
from CONVERTER.src.com.jalasoft.converter.model.video.vconverter import VideoToImages


class VideoToZipImage(Resource):
    """Defines video to zip class"""

    def post(self):
        """Create zip file containing image from video"""
        files = validate_inputs('')
        try:
            if files:
                output_format = str(request.form["output_file"])
                fps = str(request.form["fps"])
                file_in = files[0]
                file_name = os.sep + os.path.basename(file_in).split('.')[0] + os.sep
                os.makedirs(file_in.split('.')[0] + file_name, exist_ok=True)
                file_out = file_in.split('.')[0] + file_name + '%06d.' + output_format
                Command(VideoToImages(file_in, file_out, fps).convert()).run_cmd()
                tmp_zip = ZipFiles(file_in.split('.')[0], file_in.split('.')[0] + os.sep, RESPONSE_FOLDER).compress()
                url = DOWNLOAD_DIR + os.path.basename(tmp_zip)
                return {'download_URL': url}
            else:
                response = {'error message': 'File is corrupted'}
                return response, 400
        except ConvertException as error:
            response = {'error_message': error.get_message()}
            return response, 400

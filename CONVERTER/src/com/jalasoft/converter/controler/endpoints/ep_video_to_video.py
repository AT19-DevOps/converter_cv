#
# @ep_video_to_video.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.controler.routes import validate_inputs
from CONVERTER.src.com.jalasoft.converter.model.video.video_to_video import VideoToVideo


class VideoToVid(Resource):
    """Defines video to another type of video class"""
    def post(self):
        """Convert video to another type of video"""
        files = validate_inputs('')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(VideoToVideo(file_in, file_out).convert()).run_cmd()
            return url
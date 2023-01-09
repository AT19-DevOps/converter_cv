#
# @routes.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import request
from werkzeug.utils import secure_filename
from flask import send_from_directory
from model.command_line import Command
from model.video.vconverter import VideoToImages
from model.video.vconverter import VideoToVideo
from common.zip_file import ZipFiles
from model.image.image_to_images import ImageConverter
from model.image.image_to_images import ImageFlip
from common.allowed_files import AllowedExtensions
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import Resource
import os
# from src.com.jalasoft.converter.model.command_line import Command
# from src.com.jalasoft.converter.model.video.vconverter import VideoToImages
# from src.com.jalasoft.converter.model.video.vconverter import VideoToVideo
# from src.com.jalasoft.converter.common.zip_file import ZipFiles
# from src.com.jalasoft.converter.model.image.image_to_images import ImageConverter
# from src.com.jalasoft.converter.model.image.image_to_images import ImageFlip
# from src.com.jalasoft.converter.common.allowed_files import AllowedExtensions

# PATH = r'C:\Users\GamerStoreCbba\PycharmProjects\AT19_CONVERTER5\CONVERTER\src\com\jalasoft\converter'
PATH = 'src/com/jalasoft/converter'
UPLOAD_FOLDER = os.path.join(PATH, 'uploads')
RESPONSE_FOLDER = os.path.join(PATH, 'responses')
os.makedirs(UPLOAD_FOLDER,  exist_ok=True)
os.makedirs(RESPONSE_FOLDER, exist_ok=True)
print(os.getcwd())
SWAGGER_URL = '/static'
# API_URL = 'src/com/jalasoft/converter/static/swagger.json'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Converter"
    }
)


class Download(Resource):
    """Defines download file method --> url"""
    def get(self):
        """Download file"""
        file_name = request.args["file_name"]
        return send_from_directory(directory=RESPONSE_FOLDER, path=file_name, as_attachment=True)


class VideoToZipImage(Resource):
    """Defines video to zip class"""
    def post(self):
        """Create zip file containing image from video"""
        input_file = request.files["input_file"]
        output_file = request.args["output_file"]
        fps = request.args["fps"]
        if input_file and AllowedExtensions().allowed_extension(input_file.filename):
            filename = secure_filename(input_file.filename)
            zip_name = filename.split(".")[0]
            input_file.save(os.path.join(UPLOAD_FOLDER, filename))
            input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)
            Command(VideoToImages(input_video, output_file, fps).convert()).run_cmd()
            tmp_zip = ZipFiles(UPLOAD_FOLDER, input_video.split(".")[0], zip_name, RESPONSE_FOLDER).compress()
            url = 'http://localhost:5000/download?file_name=' + tmp_zip 
            return url


class VideoToZip(Resource):
    """Defines video to zip class"""
    def post(self):
        """Create zip file containing image from video. This class is for PyQTs Team :)"""
        input_file = request.files["input_file"]
        output_file = request.form.get("output_file")
        fps = request.form.get("fps")
        if input_file and AllowedExtensions().allowed_extension(input_file.filename):
            filename = secure_filename(input_file.filename)
            zip_name = filename.split(".")[0]
            input_file.save(os.path.join(UPLOAD_FOLDER, filename))
            input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)
            Command(VideoToImages(input_video, output_file, fps).convert()).run_cmd()
            tmp_zip = ZipFiles(UPLOAD_FOLDER, input_video.split(".")[0], zip_name, RESPONSE_FOLDER).compress()
            url = 'http://localhost:5000/download?file_name=' + tmp_zip  # Ver lo del localhost al venv
            return url


class VideoToVid(Resource):
    """Defines video to another type of video class"""
    def post(self):
        """Convert video to another type of video"""
        input_file = request.files["input_file"]
        output_file = request.args["output_file"]
        if input_file and AllowedExtensions().allowed_extension(input_file.filename):
            filename = secure_filename(input_file.filename)
            video_name = filename.split(".")[0]
            input_file.save(os.path.join(UPLOAD_FOLDER, filename))
            input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)
            Command(VideoToVideo(input_video, RESPONSE_FOLDER + "/" + video_name + output_file).convert()).run_cmd()
            url = 'http://localhost:5000/download?file_name=' + video_name + output_file
            return url


class ImageToImage(Resource):
    """Defines image to image class"""
    def post(self):
        """Convert image to another type of image"""
        input_file = request.files["input_file"]
        output_file = request.args["output_file"]
        if input_file and AllowedExtensions().allowed_extension(input_file.filename):
            filename = secure_filename(input_file.filename)
            image_name = filename.split(".")[0]
            input_file.save(os.path.join(UPLOAD_FOLDER, filename))
            input_image = os.path.join(UPLOAD_FOLDER, input_file.filename)
            Command(ImageConverter(input_image, RESPONSE_FOLDER + "/" + image_name + output_file).convert()).run_cmd()
            url = 'http://localhost:5000/download?file_name=' + image_name + output_file
            return url


class ImageFlipper(Resource):
    """Defines image flipper class"""
    def post(self):
        """Convert image to flipped image"""
        input_file = request.files["input_file"]
        output_file = request.args["output_file"]
        if input_file and AllowedExtensions().allowed_extension(input_file.filename):
            filename = secure_filename(input_file.filename)
            image_name = filename.split(".")[0]
            input_file.save(os.path.join(UPLOAD_FOLDER, filename))
            input_image = os.path.join(UPLOAD_FOLDER, input_file.filename)
            Command(ImageFlip(input_image, RESPONSE_FOLDER + "/" + image_name + output_file).convert()).run_cmd()
            url = 'http://localhost:5000/download?file_name=' + image_name + output_file
            return url

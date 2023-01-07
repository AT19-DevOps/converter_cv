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
from flask import send_from_directory
from flask_restful import Resource
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import secure_filename
import os

from model.audio import AudioConvert, MixAudio, IncreaseVolume
from model.image import ImageBW, ImageConverter, ImageFlip, ImageResize, ImageRotate, ImageToPDFConvert, ImageToTextConvert, PdfImage
from model.video import VideoToImages, VideoToVideo
from common import Command, ZipFiles, AllowedExtensions


PATH = os.path.join(os.getcwd(), 'workdir')
UPLOAD_FOLDER = os.path.join(PATH, 'uploads')
RESPONSE_FOLDER = os.path.join(PATH, 'responses')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESPONSE_FOLDER, exist_ok=True)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Prueba"
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
        files = validate_inputs('')
        if files:
            output_format = str(request.args["output_file"])
            fps = str(request.args["fps"])
            file_in = files[0]
            os.makedirs(file_in.split('.')[0], exist_ok=True)
            file_out = file_in.split('.')[0] + '/%06d.' + output_format
            Command(VideoToImages(file_in, file_out, fps).convert()).run_cmd()
            tmp_zip = ZipFiles(UPLOAD_FOLDER, file_in.split('.')[0], file_in.split('.')[0], RESPONSE_FOLDER).compress()
            url = 'http://localhost:5000/download?file_name=' + tmp_zip 
            return url
            # filename = secure_filename(input_file.filename)
            # zip_name = filename.split(".")[0]
            # input_file.save(os.path.join(UPLOAD_FOLDER, filename))
            # input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)
            # Command(VideoToImages(input_video, output_file, fps).convert()).run_cmd()
            # tmp_zip = ZipFiles(UPLOAD_FOLDER, input_video.split(".")[0], zip_name, RESPONSE_FOLDER).compress()
            # return url


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
        files = validate_inputs('')
        if files:
            output_format = str(request.args["output_file"])
            file_in, file_out, url = files[0], files[1], files[2]
            file_out = file_out.split('.')[0] + '.' + output_format
            Command(VideoToVideo(file_in, file_out).convert()).run_cmd()
            return url



class ImageToImage(Resource):
    """Defines image to image class"""
    def post(self):
        """Convert image to another type of image"""
        files = validate_inputs('imToim-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(ImageConverter(file_in, file_out).convert()).run_cmd()
            return url


class ImageFlipper(Resource):
    """Defines image flipper class"""
    def post(self):
        """Convert image to flipped image"""
        files = validate_inputs('imFlip-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(ImageFlip(file_in, file_out).convert()).run_cmd()
            return url


class ImageBlackWhite(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        files = validate_inputs('imBW-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(ImageBW(file_in, file_out).convert()).run_cmd()
            return url

class ImageResizer(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        files = validate_inputs('imSize-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            new_size = request.args["new_size"]
            Command(ImageResize(file_in, file_out, new_size).convert()).run_cmd()
            return url


class ImageRotater(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        files = validate_inputs('imRot-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            grades = int(request.args["grades"])
            Command(ImageRotate(file_in, file_out, grades).convert()).run_cmd()
            return url


class ImageToPdf(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        files = validate_inputs('imPDF-')
        if files:
            file_in, file_out, url = files[0], files[1].split('.')[0], files[2]
            lang = request.args["lang"]
            Command(ImageToPDFConvert(file_in, file_out, lang).convert()).run_cmd()
            return url


class ImageToText(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        files = validate_inputs('imTXT-')
        if files:
            file_in, file_out, url = files[0], files[1].split('.')[0], files[2]
            lang = request.args["lang"]
            Command(ImageToTextConvert(file_in, file_out, lang).convert()).run_cmd()
            return url


class PdfToImage(Resource):
    """Defines image to black and white class"""
    def post(self):
        """Convert image to black and white image"""
        files = validate_inputs('imJpg-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            quality = request.args["quality"]
            Command(PdfImage(file_in, file_out, quality).convert()).run_cmd()
            return url


def validate_inputs(file_prefix):
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    fileOut = '.' + str(output_file) if str(output_file)[0] != '.' else str(output_file)
    if input_file and AllowedExtensions().allowed_extension(input_file.filename):
        filename = secure_filename(input_file.filename)
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        fileIn = os.path.join(UPLOAD_FOLDER, input_file.filename)
        if file_prefix == 'imJpg-':
            fileOut = file_prefix + filename.split('.')[0] + '-%4d' + str(fileOut)
        else:
            fileOut = file_prefix + filename.split('.')[0] + str(fileOut)
        url = 'http://localhost:5000/download?file_name=' + fileOut
        fileOut = os.path.join(RESPONSE_FOLDER, fileOut)
        
        return [fileIn, fileOut, url]

    else: raise FileNotFoundError('ConverterError: Invalid input file')
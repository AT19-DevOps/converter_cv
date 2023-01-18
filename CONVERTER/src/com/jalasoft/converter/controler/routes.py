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
from model import AudioConvert
from model import MixAudio
from model import IncreaseVolume
from model import ExtractAudio
from model import ImageBW
from model import ImageConverter
from model import ImageFlip
from model import ImageResize
from model import ImageRotate
from model import ImageToPDFConvert
from model import ImageToTextConvert
from model import PdfImage
from model import VideoToImages
from model import VideoToVideo
from common import Command
from common import ZipFiles
from common import AllowedExtensions
from database.db_commands import CRUD

PATH = "E:/Users/Leo/AT/Programming/AT19_CONVERTER/AT19_CONVERTER/AT19_CONVERTER/CONVERTER/src/com/jalasoft/converter"
PATH = os.path.join(PATH, 'workdir')
UPLOAD_FOLDER = os.path.join(PATH, 'uploads')
RESPONSE_FOLDER = os.path.join(PATH, 'responses')
os.makedirs(UPLOAD_FOLDER,  exist_ok=True)
os.makedirs(RESPONSE_FOLDER, exist_ok=True)
print(os.getcwd())
SWAGGER_URL = '/swagger'
# API_URL = 'src/com/jalasoft/converter/static/swagger.json'
API_URL = '/static/swagger.json'
# SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={
#         'app_name': "Converter"
#     }
# )

def validate_inputs(file_prefix):
    """Validates input files and generates a realiable paths"""
    input_file = request.files["input_file"]
    if request.form:
        output_file = request.form["output_file"]
    else:
        output_file = request.args["output_file"]

    fileOut = '.' + str(output_file) if str(output_file)[0] != '.' else str(output_file)
    if input_file and AllowedExtensions().allowed_extension(input_file.filename):
        filename = secure_filename(input_file.filename)
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        fileIn = os.path.join(UPLOAD_FOLDER, filename)
        checksum = 1
        CRUD.insert_data(filename, checksum, os.path.join(UPLOAD_FOLDER, filename))
        if file_prefix == 'imJpg-':
            fileOut = file_prefix + filename.split('.')[0] + '-%4d' + str(fileOut)
        else:
            fileOut = file_prefix + filename.split('.')[0] + str(fileOut)
        url = 'http://localhost:5000/download?file_name=' + os.path.basename(fileOut)
        fileOut = os.path.join(RESPONSE_FOLDER, fileOut)
        return [fileIn, fileOut, url]
    else: raise FileNotFoundError('ConverterError: Invalid input file')


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
            output_format = str(request.form["output_file"])
            fps = str(request.form["fps"])
            file_in = files[0]
            file_name = '/' + os.path.basename(file_in).split('.')[0] + '/'
            os.makedirs(file_in.split('.')[0] + file_name , exist_ok=True)
            file_out = file_in.split('.')[0] + file_name + '%06d.' + output_format
            Command(VideoToImages(file_in, file_out, fps).convert()).run_cmd()
            tmp_zip = ZipFiles(file_in.split('.')[0], file_in.split('.')[0] + '/', RESPONSE_FOLDER).compress()
            url = 'http://localhost:5000/download?file_name=' + os.path.basename(tmp_zip) 
            return url


class VideoToZip(Resource):
    """Defines video to zip class"""
    def post(self):
        """Create zip file containing image from video. This class is for PyQTs Team :)"""
        files = validate_inputs('')
        if files:
            output_format = str(request.args["output_file"])
            fps = str(request.args["fps"])
            file_in = files[0]
            file_name = '/' + os.path.basename(file_in).split('.')[0] + '/'
            os.makedirs(file_in.split('.')[0] + file_name , exist_ok=True)
            file_out = file_in.split('.')[0] + file_name + '%06d.' + output_format
            Command(VideoToImages(file_in, file_out, fps).convert()).run_cmd()
            tmp_zip = ZipFiles(file_in.split('.')[0], file_in.split('.')[0] + '/', RESPONSE_FOLDER).compress()
            url = 'http://localhost:5000/download?file_name=' + os.path.basename(tmp_zip) 
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


class AudioToAudio(Resource):
    """Defines audio to audio class"""
    def post(self):
        """Convert audio to another type of audio"""
        files = validate_inputs('')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(AudioConvert(file_in, file_out).convert()).run_cmd()
            return url


class IncreaseAudioVolume(Resource):
    """Defines increse audio volume class"""
    def post(self):
        """Increases the audio volume"""
        files = validate_inputs('incVol-')
        multiplier = request.args["multiplier"]
        if files and multiplier != None:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(IncreaseVolume(file_in, file_out, multiplier).convert()).run_cmd()
            return url


class VideoToAudio(Resource):
    """Defines video to audio class"""
    def post(self):
        """Extracts the audio from the video"""
        files = validate_inputs('vidToAud-')
        if files:
            file_in, file_out, url = files[0], files[1], files[2]
            Command(ExtractAudio(file_in, file_out).convert()).run_cmd()
            return url


class AudioMixAudio(Resource):
    """Defines audio mix audio class"""
    def post(self):
        """Mixes two audios"""
        input_file_1 = request.files["input_file_1"]
        input_file_2 = request.files["input_file_2"]
        output_file = request.args["output_file"]
        if (input_file_1 and input_file_2 and AllowedExtensions().allowed_extension(input_file_1.filename)
            and AllowedExtensions().allowed_extension(input_file_2.filename)):
            filename_1 = secure_filename(input_file_1.filename)
            filename_2 = secure_filename(input_file_2.filename)
            audio_name = output_file
            input_file_1.save(os.path.join(UPLOAD_FOLDER, filename_1))
            input_file_2.save(os.path.join(UPLOAD_FOLDER, filename_2))
            input_audio_1 = os.path.join(UPLOAD_FOLDER, filename_1)
            input_audio_2 = os.path.join(UPLOAD_FOLDER, filename_2)
            input_list = [input_audio_1, input_audio_2]
            Command(MixAudio(input_list, RESPONSE_FOLDER + "/" + audio_name).convert()).run_cmd()
            url = 'http://localhost:5000/download?file_name=' + audio_name + output_file
            return url

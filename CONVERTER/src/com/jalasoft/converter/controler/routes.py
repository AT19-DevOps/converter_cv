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
from flask import blueprints
from model.command_line import Command
from model.video.vconverter import VideoToImages
from model.video.vconverter import VideoToVideo
from common.zip_file import ZipFiles
from model.image.image_to_images import ImageConverter
from model.image.image_to_images import ImageFlip
import os
from flask_swagger_ui import get_swaggerui_blueprint


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}
# PATH = r'D:\machine_learning\AT19_CONVERTER\CONVERTER\src\com\jalasoft\converter'
# PATH = r'C:\Users\hp\Documents\projects_prog_101\AT19_CONVERTER\CONVERTER\src\com\jalasoft\converter'
PATH = r'C:\Users\GamerStoreCbba\PycharmProjects\AT19_CONVERTER5\CONVERTER\src\com\jalasoft\converter'
UPLOAD_FOLDER = os.path.join(PATH, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Prueba"
    }
)

routes_files = blueprints.Blueprint('routes_files', __name__)


def allowed_file(file):
    """Check if the file is allowed"""
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False


@routes_files.get("/download")
def download_zip():
    """Download file"""
    file_name = request.args["file_name"]
    return send_from_directory(directory=UPLOAD_FOLDER, path=file_name, as_attachment=True)
    # Poner en carpeta download o public


@routes_files.post("/videotoimage/zip")
def video_to_image():
    """Convert from video to image --> .zip"""
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    fps = request.args["fps"]
    if input_file and allowed_file(input_file.filename):
        filename = secure_filename(input_file.filename)
        zip_name = filename.split(".")[0]
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)
        Command(VideoToImages(input_video, output_file, fps).convert()).run_cmd()
        tmp_zip = ZipFiles(UPLOAD_FOLDER, input_video.split(".")[0], zip_name).compress()
        url = 'http://localhost:5000/download?file_name=' + tmp_zip  # Ver lo del localhost al venv
        return url


@routes_files.post("/videotovideo")
def video_to_video():
    """Convert from video to another type of video --> hay q revisar"""
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    if input_file and allowed_file(input_file.filename):
        filename = secure_filename(input_file.filename)
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)
        Command(VideoToVideo(input_video, output_file).convert()).run_cmd()
        url = 'http://localhost:5000/download?file_name='
        return url


@routes_files.post("/imagetoimage")
def image_to_image():
    """Convert image to another type of image"""
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    if input_file and allowed_file(input_file.filename):
        filename = secure_filename(input_file.filename)
        image_name = filename.split(".")[0]
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        input_image = os.path.join(UPLOAD_FOLDER, input_file.filename)
        output_image = os.path.join(UPLOAD_FOLDER,(image_name+ output_file))
        Command(ImageConverter(input_image, output_image).convert()).run_cmd()
        url = 'http://localhost:5000/download?file_name=' + image_name + output_file
        return url


@routes_files.post("/imageflip")
def imageflip():
    """Convert image to flipped image"""
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    if input_file and allowed_file(input_file.filename):
        filename = secure_filename(input_file.filename)
        image_name = filename.split(".")[0]
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        input_image = os.path.join(UPLOAD_FOLDER, input_file.filename)
        output_image = os.path.join(UPLOAD_FOLDER,(image_name+ output_file))
        Command(ImageFlip(input_image, output_image).convert()).run_cmd()
        url = 'http://localhost:5000/download?file_name=' + image_name + output_file
        return url

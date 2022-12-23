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
from model.video.vconverter import *
from common.zip_video import Zipfiles
from model.audio.audio_converter import *
from model.image.image_to_images import *
from model.audio.save_outputs import *
import os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi'}
# PATH = r'D:\machine_learning\AT19_CONVERTER\CONVERTER\src\com\jalasoft\converter'
PATH = r'C:\Users\hp\Documents\projects_prog_101\AT19_CONVERTER\CONVERTER\src\com\jalasoft\converter'
UPLOAD_FOLDER = os.path.join(PATH,'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

routes_files = blueprints.Blueprint('routes_files', __name__)

def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False

@routes_files.get("/download")
def download_zip():
    file_name=request.args["file_name"]
    return send_from_directory(directory=UPLOAD_FOLDER, path=file_name, as_attachment=True)

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
        tmp = Command(VideoToImages(input_video, output_file, fps).convert()).run_cmd()
        tmp_zip = Zipfiles(UPLOAD_FOLDER, input_video.split(".")[0], zip_name).compress()
        url ='http://localhost:5000/download?file_name=' + tmp_zip
        return url
@routes_files.post("/videotovideo")
def video_to_video():
    """Convert from video to image --> hay q revisar"""
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    if input_file and allowed_file(input_file.filename):
        filename = secure_filename(input_file.filename)
        #zip_name = filename.split(".")[0]
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)
        tmp = Command(VideoToVideo(input_video, output_file).convert()).run_cmd()
        #tmp_zip = Zipfiles(UPLOAD_FOLDER, input_video.split(".")[0], zip_name).compress()
        url ='http://localhost:5000/download?file_name=' 
        return url
@routes_files.post("/imagetoimage")
def image_to_image():
    """Convert from image to image"""
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    if input_file and allowed_file(input_file.filename):
        filename = secure_filename(input_file.filename)
        image_name = filename.split(".")[0]
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        input_image = os.path.join(UPLOAD_FOLDER, input_file.filename)
        output_image = os.path.join(UPLOAD_FOLDER,(image_name+ output_file))
        tmp = Command(ImageConverter(input_image, output_image).convert()).run_cmd()
        url ='http://localhost:5000/download?file_name=' + image_name + output_file
        return url
@routes_files.post("/imageflip")
def imageflip():
    """Convert from image to flip image"""
    input_file = request.files["input_file"]
    output_file = request.args["output_file"]
    if input_file and allowed_file(input_file.filename):
        filename = secure_filename(input_file.filename)
        image_name = filename.split(".")[0]
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        input_image = os.path.join(UPLOAD_FOLDER, input_file.filename)
        output_image = os.path.join(UPLOAD_FOLDER,(image_name+ output_file))
        tmp = Command(ImageFlip(input_image, output_image).convert()).run_cmd()
        url ='http://localhost:5000/download?file_name=' + image_name + output_file
        return url

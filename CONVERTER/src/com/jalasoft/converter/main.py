#
# @main.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.


from model.command_line import Command
from model.converter import Converter
from model.video.vconverter import *
from model.audio.audio_converter import *
from model.image.image_to_images import *
from model.audio.save_outputs import *
from common.zip_video import Zipfiles

from flask import Flask
from flask import request
from flask_restful import Resource
from flask_restful import Api
from werkzeug.utils import secure_filename
import os


PATH = r'D:\machine_learning\AT19_CONVERTER\CONVERTER\src\com\jalasoft\converter'
UPLOAD_FOLDER = os.path.join(PATH,'uploads')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4'}

print(UPLOAD_FOLDER)
def allowed_file(file):
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    return False


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)

@app.route("/fabian", methods=['POST'])
class RestAPI(Resource):
    """Convert Video to Image"""

    def post(self):
        """POST method"""
        input_file = request.files["input_file"]
        output_file = request.form.get("output_file")
        fps = request.form.get("fps")
        
        if input_file and allowed_file(input_file.filename):

            filename = secure_filename(input_file.filename)
            zip_name = filename.split(".")[0]
            input_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            input_video = os.path.join(UPLOAD_FOLDER, input_file.filename)

            tmp = Command(VideoToImages(input_video, output_file, fps).convert()).run_cmd()
            tmp_zip = Zipfiles(UPLOAD_FOLDER , input_video.split(".")[0], zip_name).compress()

            url='http://localhost:5000/download/zip/' + tmp_zip
       
            return {'url_link': url} #en vez de data url_data, devolver la url


            #crear el api del downloader debe ser con un get

#api.add_resource(RestAPI, '/fabian')


if __name__ == '__main__':
    app.run(debug=True)
#
# @main.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#
from dotenv import  load_dotenv
load_dotenv()

from os import getenv
from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Api
from config import SWAGGERUI_BLUEPRINT
from config import SWAGGER_URL
from config import SERVER
from config import PORT
from common.token import Token
from database.db_commands import CRUD
from controler.endpoints.ep_download import Download
from controler.endpoints.ep_video_to_zip_image import VideoToZipImage
from controler.endpoints.ep_video_to_zip import VideoToZip
from controler.endpoints.ep_video_to_video import VideoToVid
from controler.endpoints.ep_image_to_image import ImageToImage
from controler.endpoints.ep_image_flipper import ImageFlipper
from controler.endpoints.ep_image_bw import ImageBlackWhite
from controler.endpoints.ep_image_resizer import ImageResizer
from controler.endpoints.ep_image_rotater import ImageRotater
from controler.endpoints.ep_image_to_text import ImageToText
from controler.endpoints.ep_pdf_to_image import PdfToImage
from controler.endpoints.ep_video_to_audio import VideoToAudio
from controler.endpoints.ep_audio_to_audio import AudioToAudio
from controler.endpoints.ep_incrase_audio_volume import IncreaseAudioVolume
from controler.endpoints.ep_audio_mix_audio import AudioMixAudio
from controler.endpoints.ep_text_translate import TextTranslate
from controler.endpoints.ep_get_metadata import GetMetadata
from controler.endpoints.ep_login import Login
from database.login_crud import UserCRUD

app = Flask(__name__)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
api = Api(app)

CRUD.create_table("media")
UserCRUD().create()
api.add_resource(VideoToZipImage, '/videotoimage/zip')
api.add_resource(VideoToZip, '/videotoimagee/zip')
api.add_resource(VideoToVid, '/videotovideo')
api.add_resource(ImageToImage, '/imagetoimage')
api.add_resource(ImageFlipper, '/imageflip')
api.add_resource(ImageBlackWhite, '/imagebw')
api.add_resource(ImageResizer, '/imageresize')
api.add_resource(ImageRotater, '/imagerotate')
api.add_resource(ImageToText, '/imagetopdf')
api.add_resource(PdfToImage, '/pdftoimage')
api.add_resource(Download, '/download')
api.add_resource(VideoToAudio, '/audioextractaudio')
api.add_resource(AudioToAudio, '/audiotoaudio')
api.add_resource(IncreaseAudioVolume, '/audioincreasevolume')
api.add_resource(AudioMixAudio, "/audiomixaudio")
api.add_resource(TextTranslate, "/texttranslator")
api.add_resource(GetMetadata, "/metadatageter")
api.add_resource(Login, "/login")

@app.before_request
def middleware():
    """Verifies users before process request"""
    if request.method == 'POST':
        try:
            autentification = request.headers.get("Authorization")
            token = autentification.split(" ")[1]
            valid = Token().validate_token(token)
            if valid == False:
                response = jsonify({"message": "You aren't authorizate"})
                response.status_code = 401
                return response
        except:
            response = jsonify({"message": "Bad request"})
            response.status_code = 400
            return response

if __name__ == '__main__':
    app.run(debug=True, host = getenv("CONVERTER_HOST_ALL"), port = getenv("CONVERTER_PORT"))


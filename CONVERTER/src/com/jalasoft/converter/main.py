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


from flask import Flask
from flask import request
from flask import jsonify
from flask_restful import Api
from CONVERTER.src.com.jalasoft.converter.common.token import Token
from CONVERTER.src.com.jalasoft.converter.database.db_commands import CRUD
from CONVERTER.src.com.jalasoft.converter.controler.routes import SWAGGER_URL
from CONVERTER.src.com.jalasoft.converter.controler.routes import SWAGGERUI_BLUEPRINT
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_download import Download
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_video_to_zip_image import VideoToZipImage
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_video_to_zip import VideoToZip
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_video_to_video import VideoToVid
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_image_to_image import ImageToImage
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_image_flipper import ImageFlipper
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_image_bw import ImageBlackWhite
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_image_resizer import ImageResizer
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_image_rotater import ImageRotater
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_image_to_text import ImageToText
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_pdf_to_image import PdfToImage
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_video_to_audio import VideoToAudio
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_audio_to_audio import AudioToAudio
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_incrase_audio_volume import IncreaseAudioVolume
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_audio_mix_audio import AudioMixAudio
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_text_translate import TextTranslate
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_get_metadata import GetMetadata
from CONVERTER.src.com.jalasoft.converter.controler.endpoints.ep_login import Login


app = Flask(__name__)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix = SWAGGER_URL)
api = Api(app)

CRUD.create_table("media")

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
    if request.url_rule.rule != "/login":
        autentification = request.headers.get("Authorization")
        token = autentification.split(" ")[1]
        valid = Token().validate_token(token)
        if valid == False:
            response = jsonify({"message": "You aren't authorizate"})
            response.status_code = 401
            return response


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)


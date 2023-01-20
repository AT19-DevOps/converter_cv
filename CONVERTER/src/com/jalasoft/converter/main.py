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

import os
from flask import Flask
from controler.routes import SWAGGER_URL
from flask_restful import Api
from controler.routes import SWAGGERUI_BLUEPRINT
from controler.routes import Download
from controler.routes import VideoToZipImage
from controler.routes import VideoToZip
from controler.routes import VideoToVid
from controler.routes import ImageToImage
from controler.routes import ImageFlipper
from controler.routes import ImageBlackWhite
from controler.routes import ImageResizer
from controler.routes import ImageRotater
from controler.routes import ImageToPdf
from controler.routes import ImageToText
from controler.routes import PdfToImage
from controler.routes import VideoToAudio
from controler.routes import AudioToAudio
from controler.routes import IncreaseAudioVolume
from controler.routes import AudioMixAudio
from controler.routes import TextTranslate
from controler.routes import GetMetadata

app = Flask(__name__)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix = SWAGGER_URL)
api = Api(app)
api.add_resource(VideoToZipImage, '/videotoimage/zip')
api.add_resource(VideoToZip, '/videotoimagee/zip')
api.add_resource(VideoToVid, '/videotovideo')
api.add_resource(ImageToImage, '/imagetoimage')
api.add_resource(ImageFlipper, '/imageflip')
api.add_resource(ImageBlackWhite, '/imagebw')
api.add_resource(ImageResizer, '/imageresize')
api.add_resource(ImageRotater, '/imagerotate')
api.add_resource(ImageToPdf, '/imagetopdf')
api.add_resource(ImageToText, '/imagetotext')
api.add_resource(PdfToImage, '/pdftoimage')
api.add_resource(Download, '/download')
api.add_resource(VideoToAudio, '/audioextractaudio')
api.add_resource(AudioToAudio, '/audiotoaudio')
api.add_resource(IncreaseAudioVolume, '/audioincreasevolume')
api.add_resource(AudioMixAudio, "/audiomixaudio")
api.add_resource(TextTranslate, "/texttranslator")
api.add_resource(GetMetadata, "/metadatageter")

print(os.getcwd())
if __name__ == '__main__':
    app.run(debug = True, port = 5000, host = '127.0.0.1')

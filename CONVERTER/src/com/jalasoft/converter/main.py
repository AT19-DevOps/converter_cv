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
from CONVERTER.src.com.jalasoft.converter.database.db_commands import CRUD
from controler.routes import SWAGGER_URL
from flask_restful import Api
from controler.routes import SWAGGERUI_BLUEPRINT
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


if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0', port = 5000)

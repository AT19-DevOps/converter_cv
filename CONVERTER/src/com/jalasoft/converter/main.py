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
#

from flask import Flask
from controler.routes import SWAGGER_URL
from flask_restful import Api
from controler.routes import SWAGGERUI_BLUEPRINT
from controler.routes import Download, VideoToZipImage, VideoToZip, VideoToVid, ImageToImage, ImageFlipper, ImageBlackWhite, ImageResizer, ImageRotater, ImageToPdf, ImageToText, PdfToImage


app = Flask(__name__)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
api = Api(app)
api.add_resource(VideoToZipImage, '/videotoimagee/zip')
api.add_resource(VideoToZip, '/videotoimage/zip')
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

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='127.0.0.1')

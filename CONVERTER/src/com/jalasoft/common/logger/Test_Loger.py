#
# @image_to_images.py Copyright (c) 2021 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# # All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from flask import Flask
import json
from flask_cors import CORS
from flask import request
from Logger_ import LoggerManager

app = Flask(__name__)
CORS(app)

logger = LoggerManager()

@app.route("/")
def hello_world():
    """It is a test of how it is being used"""
    logger.debug("Starting method")
    try:
        logger.info("Starting the operation ")
        number = 5 / 0
        # force an error to go to the exception
        logger.debug("End Method")
        return str(number)
    except:
        logger.error("We have an exception")
        return "test"
    
#
# @mange_request.py Copyright (c) 2023 Jalasoft.
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
from flask_swagger_ui import get_swaggerui_blueprint
from werkzeug.utils import secure_filename
import os
from CONVERTER.src.com.jalasoft.converter.common.exception.input_exception import InvalidInputException
from CONVERTER.src.com.jalasoft.converter.controler.config import UPLOAD_FOLDER
from CONVERTER.src.com.jalasoft.converter.controler.config import RESPONSE_FOLDER
from CONVERTER.src.com.jalasoft.converter.common.valid_data import Validations
from CONVERTER.src.com.jalasoft.converter.database.db_commands import CRUD

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Converter"
    }
)


class ManageData:
    """Manages the data received in the endpoint"""
    def __init__(self):
        self.filename = None
        self.output_file_extension = None
        self.in_file = None
        self.input_file = None
        self.output_extension = None

    def get_data(self, file_prefix):
        """Gets data from the form"""
        try:
            self.input_file = request.files["input_file"]
            self.output_extension = request.form["output_file"]
        except Exception as error:
            raise InvalidInputException("Invalid input: the input should not be None type -" + file_prefix)
        Validations().validate_file(self.input_file, file_prefix)
        Validations().validate_output(self.output_extension, file_prefix)

    def manege_data(self, file_prefix):
        """Sets the format of the output file name"""
        self.get_data(file_prefix)
        if self.output_extension[0] != '.':
            self.output_extension = '.' + str(self.output_extension)
        self.filename = secure_filename(self.input_file.filename)

    def save_data(self):
        """Saves the uploaded file in uploads folder"""
        self.input_file.save(os.path.join(UPLOAD_FOLDER, self.filename))
        checksum = 1
        CRUD.insert_data(self.filename, checksum, os.path.join(UPLOAD_FOLDER, self.filename))

    def generate_path(self, file_prefix):
        """Generates the input file path, the output file path, and the download file link"""
        self.manege_data(file_prefix)
        self.save_data()
        self.in_file = os.path.join(UPLOAD_FOLDER, self.filename)
        if file_prefix == 'imJpg-':
            self.output_extension = file_prefix + self.filename.split('.')[0] + '-%4d' + str(self.output_extension)
        else:
            self.output_extension = file_prefix + self.filename.split('.')[0] + str(self.output_extension)
        url = 'http://localhost:5000/download?file_name=' + os.path.basename(self.output_extension)
        self.output_extension = os.path.join(RESPONSE_FOLDER, self.output_extension)
        return [self.in_file, self.output_extension, url]


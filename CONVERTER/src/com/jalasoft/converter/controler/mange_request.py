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
from werkzeug.utils import secure_filename
import os
from CONVERTER.src.com.jalasoft.converter.common.exception.input_exception import InvalidInputException
from CONVERTER.src.com.jalasoft.converter.config import DOWNLOAD_DIR
from CONVERTER.src.com.jalasoft.converter.config import UPLOAD_FOLDER
from CONVERTER.src.com.jalasoft.converter.config import RESPONSE_FOLDER
from CONVERTER.src.com.jalasoft.converter.common.valid_data import Validations
from CONVERTER.src.com.jalasoft.converter.database.checksum import compare_checksum, checksum_generator_md5


class ManageData:
    """Manages the data received in the endpoint"""
    def __init__(self):
        self.filename = None
        self.output_file_extension = None
        self.in_file = None
        self.input_file = None
        self.output_extension = None
        self.checksum_param = None

    def get_data(self, file_prefix):
        """Gets data from the form"""
        try:
            self.input_file = request.files["input_file"]
            self.output_extension = request.form["output_file"]
            self.checksum_param = request.form["checksum_param"]
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
        self.in_file = os.path.join(UPLOAD_FOLDER, self.filename)

    def generate_path(self, file_prefix):
        """Generates the input file path, the output file path, and the download file link"""
        self.manege_data(file_prefix)
        self.save_data()
        if self.checksum_param != str(checksum_generator_md5(self.in_file)):
            return None
        else:
            self.in_file = compare_checksum(self.filename, self.in_file)
        if file_prefix == 'imJpg-':
            self.output_extension = file_prefix + self.filename.split('.')[0] + '-%4d' + str(self.output_extension)
        else:
            self.output_extension = file_prefix + self.filename.split('.')[0] + str(self.output_extension)
        url = DOWNLOAD_DIR + os.path.basename(self.output_extension)
        self.output_extension = os.path.join(RESPONSE_FOLDER, self.output_extension)
        return [self.in_file, self.output_extension, url]


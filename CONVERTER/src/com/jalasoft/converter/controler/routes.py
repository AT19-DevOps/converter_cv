#
# @routes.py Copyright (c) 2023 Jalasoft.
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
from CONVERTER.src.com.jalasoft.converter.common.allowed_files import AllowedExtensions
from CONVERTER.src.com.jalasoft.converter.controler.config import UPLOAD_FOLDER
from CONVERTER.src.com.jalasoft.converter.controler.config import RESPONSE_FOLDER
from CONVERTER.src.com.jalasoft.converter.database.db_commands import CRUD

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "Converter"
    }
)

def validate_inputs(file_prefix):
    """Validates input files and generates a reliable paths"""
    input_file = request.files["input_file"]
    output_file = request.form["output_file"]
    out_file = '.' + str(output_file) if str(output_file)[0] != '.' else str(output_file)
    allowed_file = AllowedExtensions().validate_extension(input_file.filename)
    allowed_output = AllowedExtensions().validate_extension(out_file)
    if allowed_file and allowed_output:
        filename = secure_filename(input_file.filename)
        checksum = 1
        CRUD.insert_data(filename, checksum, os.path.join(UPLOAD_FOLDER, filename))
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        in_file = os.path.join(UPLOAD_FOLDER, filename)
        if file_prefix == 'imJpg-':
            out_file = file_prefix + filename.split('.')[0] + '-%4d' + str(out_file)
        else:
            out_file = file_prefix + filename.split('.')[0] + str(out_file)
        port = os.getenv("CONVERTER_PORT")
        url = os.getenv("CONVERTER_HOST")
        download_url = f"{url}:{port}/download?file_name={os.path.basename(out_file)}"
        out_file = os.path.join(RESPONSE_FOLDER, out_file)
        return [in_file, out_file, download_url]
    else:
        raise FileNotFoundError('ConverterError: Invalid input file')


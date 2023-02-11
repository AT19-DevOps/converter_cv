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

import os
from flask import request
from werkzeug.utils import secure_filename
from CONVERTER.src.com.jalasoft.converter.config import UPLOAD_FOLDER
from CONVERTER.src.com.jalasoft.converter.config import RESPONSE_FOLDER
from CONVERTER.src.com.jalasoft.converter.config import DOWNLOAD_DIR
from CONVERTER.src.com.jalasoft.converter.common.allowed_files import AllowedExtensions
from CONVERTER.src.com.jalasoft.converter.database.checksum import checksum_generator_md5
from CONVERTER.src.com.jalasoft.converter.database.checksum import compare_checksum


def validate_inputs(file_prefix):
    """Validates input files and generates a reliable paths"""
    input_file = request.files["input_file"]
    output_file = request.form["output_file"]
    checksum_param = str(request.form["checksum_param"])
    out_file = '.' + str(output_file) if str(output_file)[0] != '.' else str(output_file)
    allowed_file = AllowedExtensions().validate_extension(input_file.filename)
    allowed_output = AllowedExtensions().validate_extension(out_file)
    if allowed_file and allowed_output:
        filename = secure_filename(input_file.filename)
        input_file.save(os.path.join(UPLOAD_FOLDER, filename))
        in_file = os.path.join(UPLOAD_FOLDER, filename)
        if checksum_param != checksum_generator_md5(in_file):
            return None
        else:
            in_file = compare_checksum(filename, in_file)
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

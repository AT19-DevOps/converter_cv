#
# @zip_video.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft

import zipfile
import os

# Path folder compress
file_path = "C:/converters/AT19_CONVERTER/CONVERTER/src/com/jalasoft/converter/uploads/video"

# CZipfile object creation, Zipfile naming
zip = zipfile.ZipFile('Compress.zip', 'w')

# filtration of files
matchlist = ['.png', '.txt', '.pdf', '.py', '.jpg']

# Filtration of files to be compressed according to file extension
for archivo in os.listdir(file_path):
    for ext in matchlist:
        # Validate file extension with list
        if archivo.endswith(ext):
            zip.write(os.path.join(file_path, archivo))

zip.close()


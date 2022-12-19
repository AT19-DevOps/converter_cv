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


file_path = "/AT19_CONVERTER/CONVERTER/src/com/jalasoft/converter/uploads/video"
zip = zipfile.ZipFile('Compress.zip', 'w')
matchlist = ['.png', '.txt', '.pdf', '.py', '.jpg']
for archivo in os.listdir(file_path):
    for ext in matchlist:
        if archivo.endswith(ext):
                zip.write(os.path.join(file_path, archivo))

zip.close()

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

import shutil



class Zipfiles:
    def __init__(self, upath, folder_to_zip, name_of_zip):
        self.upath = upath
        self.folder_to_zip = folder_to_zip
        self.name_of_zip = name_of_zip
    
    def compress(self):
        #print(self.upath)
        #print(self.folder_to_zip)
        shutil.make_archive(self.name_of_zip, "zip", self.folder_to_zip)
        name = self.name_of_zip + '.zip'
        shutil.move(name, os.path.join(self.upath, name))
        return name



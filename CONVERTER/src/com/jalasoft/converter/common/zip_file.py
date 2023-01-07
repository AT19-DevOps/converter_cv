#
# @zip_file.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft
#

import shutil
import os


class ZipFiles:
    """Defines ZipFiles criteria"""
    def __init__(self, upath, folder_to_zip, name_of_zip, destination):
        self.upath = upath
        self.folder_to_zip = folder_to_zip
        self.name_of_zip = name_of_zip
        self.destination = destination
    
    def compress(self):
        """Defines compress method"""
        shutil.make_archive(self.name_of_zip, "zip", 'images' + self.folder_to_zip)
        name = self.name_of_zip + '.zip'
        shutil.move(name, os.path.join(self.destination, name))
        return name


# import os, shutil
# def make_archive(source, destination):
#         base = os.path.basename(destination)
#         name = base.split('.')[0]
#         format = base.split('.')[1]
#         archive_from = os.path.dirname(source)
#         archive_to = os.path.basename(source.strip(os.sep))
#         print(source, destination, archive_from, archive_to)
#         shutil.make_archive(name, format, archive_from, archive_to)
#         shutil.move('%s.%s'%(name,format), destination)

# make_archive('/path/to/folder', '/path/to/folder.zip')
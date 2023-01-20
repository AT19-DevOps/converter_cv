#
# @allowed_files.py Copyright (c) 2023 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'avi', "mp3", "opus", "wav"}


class AllowedExtensions:
    """Defines Allowed extensions criteria"""
    def allowed_extension(self, file):
        """Check if the extension file is allowed"""
        file_check = file.split('.')
        if file_check[1] in ALLOWED_EXTENSIONS:
            return True
        return False

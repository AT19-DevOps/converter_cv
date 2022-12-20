#
# @paths.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

import os


class Path:
    """Verifies and builds paths for input and output files""" 
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    
        
    def paths(self):
        """Returns path strings, used only in VideoToImages  """
        BASE_DIR = os.getcwd()
        destination_dir = os.path.join(BASE_DIR, self.input_file.split(".")[0])#uniendo base dir con (video.mp4), solo toma video y forma la carpeta destino
        source = os.path.join(BASE_DIR, self.input_file)#toma el base dir y se lo pone al nombre video, construye la ruta cpmpleta al archivo video mp4
        if not os.path.exists(destination_dir): os.mkdir(destination_dir)# si no existe destinatio dir que se creo en la 27 solo la ruta
        destination = os.path.join(destination_dir, '%06d.' + self.output_file)#va a crear el directorio, va hacer el grupo de archivos que se va a crear, 06d significa un numero de 6 digitos
        print(source, "\n", destination)
        return [source, destination] 
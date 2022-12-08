# Video Converter Module  
# Requeriments: ffmpeg library (for linux)
# How to: using command line
# Project starter: Daniel Villarroel
# General syntax: fmpeg [global_options] {[input_file_options] -i input_url} ... {[output_file_options] output_url} ...

import subprocess, os

class Converter:
    
    def __init__(self, input_file, output_file, fps): #, **kwargs):
        self.input_file = input_file
        self.output_file = output_file
        #self.fps = fps
        #self.kwargs = kwargs
    
    def convert(self):
        pass

    def video_paths(self): # Unnecessary
        source = os.path.join(os.getcwd(), self.input_file)
        destination = os.path.join(os.getcwd(),self.input_file.split(".")[0])
        if not os.path.exists(destination): os.mkdir(destination)
        destination = os.path.join(destination, self.output_file)
        return [source, destination] 

class Video_to_images(Converter): # Working, ok.
    
    def __init__(self, input_file, output_file, fps): #, **kwargs):
        Converter.__init__(self, input_file, output_file,fps) #, **kwargs)        
        
    def convert(self):
        paths = Converter('file_example_MP4_1920_18MG.mp4', 'image%06d.jpg', "1").video_paths()
        vti = subprocess.Popen(['ffmpeg','-i', paths[0],'-r','1', paths[1]])
        print("The exit code was: %d" % vti)
    
class Zip_files(Converter): # Not implemented

   def zip_images():
        pass
    
class Video_to_video(Converter): # Not tested
    def __init__(self, input_file, output_file):
        Converter.__init__(self, input_file, output_file,fps) #, **kwargs)
    
    def convert(self):    
        paths = Converter(self.input_file, self.output_file).video_paths()
        vtv = subprocess.Popen(['ffmpeg','-i',paths[0],'1',paths[1]])
        print("The exit code was: %d" % vtv)


tmp = Video_to_images('file_example_MP4_1920_18MG.mp4', 'image%06d.jpg', "1").convert()
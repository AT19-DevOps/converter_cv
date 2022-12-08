import os


class Converter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        pass

    def move_file(self):
        pass


class AudioConvert(Converter):
    def convert(self):
        command = f'ffmpeg -i {self.input_file} {self.output_file}'
        os.system(command)


class IncreaseVolume(Converter):
    def convert(self):
        command = f'ffmpeg -i {self.input_file} -vol 512 {self.output_file}'
        print(command)
        os.system(command)


class ExtractAudio(Converter):
    def convert(self):
        command = f'ffmpeg -i {self.input_file} -vn {self.output_file}'
        os.system(command)


class MixAudio(Converter):
    def convert(self):
        command = f'ffmpeg -i {self.input_file} -i {self.output_file} -filter_complex amerge audio_mix.mp3'
        os.system(command)


class DeleteSilence(Converter):
    def convert(self):
        command = f'ffmpeg -i {self.input_file} -af silenceremove=1:0:-50dB:1:0:-75dB {self.output_file}'
        os.system(command)


class SaveOutput(Converter):
    def convert(self):
        command = f'MOVE "{self.input_file}" "{self.output_file}"'
        os.system(command)




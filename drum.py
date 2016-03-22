import os
import const
import subprocess


class Audio(object):
    ''' Pygamii Audio Class '''
    _file = None
    song = None

    def __init__(self, f=None, *args, **kwargs):
        if f:
            self._file = f

        if self._file is None:
            raise AssertionError("audio need a file")

    def play(self, volume=1.0):
        subprocess.Popen(
            [
                'mplayer',
                '-volume',
                str(volume * 200),
                self._file
            ],
            stdout=subprocess.PIPE
        )


class DrumComponent(object):
    '''A Drum  Component'''
    audio_file = None
    auto_stop = True
    max_power = 127
    _absolute_audio_path = None

    def __init__(self):
        self.audio = Audio(self.get_audio_file())

    def get_audio_file(self):
        if not self._absolute_audio_path:
            self._absolute_audio_path = os.path.join(
                const.MEDIA_ROOT,
                self.audio_file
            )
        return self._absolute_audio_path

    def shot(self, power=None):
        if power is None:
            power = self.max_power

        self.audio.play(power / self.max_power)


class DemoShot(DrumComponent):
    audio_file = 'shot.ogg'


class Crash(DrumComponent):
    audio_file = 'crash.wav'


class Snare(DrumComponent):
    audio_file = 'snare.wav'


class HiHat(DrumComponent):
    audio_file = 'hi-hat.aiff'
    max_power = 150


class Bass(DrumComponent):
    audio_file = 'bass.aiff'
    max_power = 110


class Cymbal(DrumComponent):
    audio_file = 'cymbal.aiff'
    max_power = 110


class HiTom(DrumComponent):
    audio_file = 'hi_tom.wav'


class LowTom(DrumComponent):
    audio_file = 'low_tom.wav'

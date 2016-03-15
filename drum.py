import pygame
import os
import const


class Audio(object):
    ''' Pygamii Audio Class '''
    _file = None
    song = None

    def __init__(self, f=None, auto_loading=True, *args, **kwargs):
        if f:
            self._file = f

        if self._file is None:
            raise AssertionError("audio need a file")

        if auto_loading:
            self.load_file()

    def load_file(self):
        pygame.mixer.init()
        self.song = pygame.mixer.Sound(self._file)

    def play(self, loop=False):
        if loop:
            self.song.play(-1)
        else:
            self.song.play()

    def stop(self):
        self.song.stop()

    def set_volume(self, volume):
        self.song.set_volume(volume)


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

        self.audio.stop()
        self.audio.set_volume(self.max_power / power)
        self.audio.play()


class DemoShot(DrumComponent):
    audio_file = 'shot.ogg'

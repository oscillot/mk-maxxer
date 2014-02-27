from timbre.mixer import OSC1Level as TimbreOSC1Level
from timbre.mixer import Noise as TimbreNoise
from microkorg_abstract import MicroKorgAbstractParameter


class OSC1Level(TimbreOSC1Level):
    def _get_offset(self):
        self.offset = 15


class EXT1Level(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'MIXER EXT1 Level: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 16


class Noise(TimbreNoise):
    def _get_offset(self):
        self.offset = 17
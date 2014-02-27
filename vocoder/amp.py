from timbre.amp import Level as TimbreLevel
from timbre.amp import Distortion as TimbreDistortion
from timbre.amp import VelocitySense as TimbreVelocitySense
from timbre.amp import KeyboardTrack as TimbreKeyboardTrack
from microkorg_abstract import MicroKorgAbstractParameter


class Level(TimbreLevel):
    def _get_offset(self):
        self.offset = 27


class DirectLevel(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'AMP Direct Level: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 28


class Distortion(TimbreDistortion):
    def _get_offset(self):
        self.offset = 29
        self.bits = [0]


class VelocitySense(TimbreVelocitySense):
    def _get_offset(self):
        self.offset = 30


class KeyboardTrack(TimbreKeyboardTrack):
    def _get_offset(self):
        self.offset = 31
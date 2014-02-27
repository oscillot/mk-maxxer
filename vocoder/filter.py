from timbre.filter import Cutoff as TimbreCutoff
from timbre.filter import Resonance as TimbreResonance
from microkorg_abstract import MicroKorgAbstractParameter
from constants.tn import T13


class Shift(MicroKorgAbstractParameter):
    def __repr__(self):
        SHIFTS = {
            0: '0',
            1: '+1',
            2: '+2',
            3: '-1',
            4: '-2'
        }
        return 'FILTER Shift: %s' % SHIFTS[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 5):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 21


class Cutoff(TimbreCutoff):
    def _get_offset(self):
        self.offset = 22


class Resonance(TimbreResonance):
    def _get_offset(self):
        self.offset = 23


class ModSource(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'MIXER ModSource: %s' % T13[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 24


class Intensity(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'MIXER Intensity: %s' % (self.value.intle - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 25


class EFSense(MicroKorgAbstractParameter):
    def __repr__(self):
        if self.value.intle == 127:
            v = 'HOLD'
        else:
            v = self.value.intle
        return 'MIXER E.F. Sense: %s' % v

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 26
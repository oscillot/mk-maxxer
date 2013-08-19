from bitstring import BitArray

from microkorg_abstract import MicroKorgAbstractParamater
from constants import STATES, T1


class Sync(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Sync: %s' % STATES[self.value.int]

    def _check_value(self):
        if self.value.int not in [0, 1]:
            raise ValueError('Parameter is out of range: %d' % self.value.int)

    def _get_offset(self):
        self.offset = 19
        self.bits = [7]


class TimeBase(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Time Base: %s' % T1[self.value.int]

    def _check_value(self):
        if self.value.int not in range(0, 15):
            raise ValueError('Parameter is out of range: %d' % self.value.int)

    def _get_offset(self):
        self.offset = 19
        self.bits = range(0, 4)


class Time(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Time: %s' % self.value

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 20
        self.bits = range(0, 8)


class Depth(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Depth: %s' % self.value

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 21
        self.bits = range(0, 8)


class Type(MicroKorgAbstractParamater):
    def __repr__(self):
        TYPES = {
            '000': 'No Delay',
            '100': 'Stereo Delay',
            '010': 'Cross Delay',
            '001': 'L/R Delay',
        }
        return 'DLY Type: %s' % TYPES[self.value.bin]

    def _check_value(self):
        if self.value.bin not in ['000', '100', '010', '001']:
            ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 22
        self.bits = range(0, 8)
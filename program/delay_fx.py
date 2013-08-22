from microkorg_abstract import MicroKorgAbstractParamater
from constants import STATES, T1


class Sync(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Sync: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in [0, 1]:
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 19
        self.bits = [7]


class TimeBase(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Time Base: %s' % T1[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 15):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

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
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value
            .intle)

    def _get_offset(self):
        self.offset = 21
        self.bits = range(0, 8)


class Type(MicroKorgAbstractParamater):
    def __repr__(self):
        TYPES = {
            0: 'No Delay',
            4: 'Stereo Delay',
            2: 'Cross Delay',
            1: 'L/R Delay',
        }
        return 'DLY Type: %s' % TYPES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in [0, 4, 2, 1]:
            ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 22
        self.bits = range(0, 8)
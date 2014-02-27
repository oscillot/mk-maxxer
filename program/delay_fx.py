from microkorg_abstract import MicroKorgAbstractParameter
from constants import STATES, T1


class Sync(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'DLY Sync: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in [0, 1]:
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 19
        self.bits = [7]


class TimeBase(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'DLY Time Base: %s' % T1[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 15):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 19
        self.bits = range(0, 4)


class Time(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'DLY Time: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value
                .intle)

    def _get_offset(self):
        self.offset = 20
        self.bits = range(0, 8)


class Depth(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'DLY Depth: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value
            .intle)

    def _get_offset(self):
        self.offset = 21
        self.bits = range(0, 8)


class Type(MicroKorgAbstractParameter):
    def __repr__(self):
        TYPES = {
            0: 'No Delay',
            1: 'L/R Delay',
            2: 'Cross Delay',

            4: 'Stereo Delay',
        }
        return 'DLY Type: %s' % TYPES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 3):
            ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 22
        self.bits = range(0, 8)
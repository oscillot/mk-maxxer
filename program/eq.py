from microkorg_abstract import MicroKorgAbstractParameter
from constants import T10, T11


class HiFreq(MicroKorgAbstractParameter):
    def __repr__(self):
        try:
            return 'EQ Hi Freq: %dKHz' % T10[self.value.intle]
        except KeyError:
            return 'WARN!: EQ Hi Freq UNKNOWN (Valid 0-29, got %d)' % self\
                .value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 32):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 26
        self.bits = range(0, 6)


class HiGain(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'EQ Hi Gain: %s+/-12 (64=0?)' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 65):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 27
        self.bits = range(0, 8)


class LoFreq(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'EQ Lo Freq: %dHz' % T11[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 30):
            raise ValueError('Parameter is out of range: %d' % self.value.intle
            .intle)

    def _get_offset(self):
        self.offset = 28
        self.bits = range(0, 8)


class LoGain(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'EQ Lo Gain: %s+/-12 (64=0?)' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 65):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 27
        self.bits = range(0, 8)
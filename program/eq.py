from microkorg_abstract import MicroKorgAbstractParamater
from helpers import slope


class HiFreq(MicroKorgAbstractParamater):
    def __repr__(self):
        x1, y1 = 0, 1.00
        x2, y2 = 29, 18.0
        freq_scale = slope((x1, y1), (x2, y2))

        return 'EQ Hi Freq: %dKHz' % int(self.value)*freq_scale

    def _check_value(self):
        if self.value not in range(0, 30):
            raise ValueError('Parameter is out of range: ' + self.value)

    def _get_offset(self):
        self.offset = 26
        self.bits = [range(0, 8)]


class HiGain(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'EQ Hi Gain: %s+/-12 (64=0?)' % self.value

    def _check_value(self):
        if self.value not in range(0, 64):
            raise ValueError('Parameter is out of range: ' + self.value)

    def _get_offset(self):
        self.offset = 27
        self.bits = [range(0, 8)]


class LoFreq(MicroKorgAbstractParamater):
    def __repr__(self):
        x1, y1 = 0, 40
        x2, y2 = 29, 1000
        freq_scale = slope((x1, y1), (x2, y2))

        return 'EQ Lo Freq: %dHz' % int(self.value)*freq_scale

    def _check_value(self):
        if self.value not in range(0, 30):
            raise ValueError('Parameter is out of range: ' + self.value)

    def _get_offset(self):
        self.offset = 28
        self.bits = [range(0, 8)]


class LoGain(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'EQ Lo Gain: %s+/-12 (64=0?)' % self.value

    def _check_value(self):
        if self.value not in range(0, 64):
            raise ValueError('Parameter is out of range: ' + self.value)

    def _get_offset(self):
        self.offset = 27
        self.bits = [range(0, 8)]
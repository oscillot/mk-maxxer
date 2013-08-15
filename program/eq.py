from bitstring import BitArray

from microkorg_abstract import MicroKorgAbstractParamater
from constants import T10, T11


class HiFreq(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'EQ Hi Freq: %dKHz' % T10[self.value]

    def _check_value(self):
        if self.value not in range(0, 30):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 26
        self.bits = range(0, 8)


class HiGain(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'EQ Hi Gain: %s+/-12 (64=0?)' % self.value

    def _check_value(self):
        if self.value not in range(0, 64):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 27
        self.bits = range(0, 8)


class LoFreq(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'EQ Lo Freq: %dHz' % T11[self.value]

    def _bitmask(self):
        b = BitArray(uint=self.value, length=8)
        keep = b.bin[0:5]
        discard = b.bin[5:] #might need this later?
        new_bin = keep[::-1].zfill(8)
        b2 = BitArray(bin='0b%s' % new_bin)
        self.value = b2.int

    def _check_value(self):
        if self.value not in range(0, 30):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 28
        self.bits = range(0, 8)


class LoGain(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'EQ Lo Gain: %s+/-12 (64=0?)' % self.value

    def _check_value(self):
        if self.value not in range(0, 64):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 27
        self.bits = range(0, 8)
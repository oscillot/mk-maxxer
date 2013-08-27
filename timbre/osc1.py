from microkorg_abstract import MicroKorgAbstractParamater
from constants import T2


class Wave(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'OSC1 Wave: %s' % T2[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 8):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 7


class WaveformCTRL1(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'OSC1 Waveform CTRL 1: %s' % self.value

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 8


class WaveformCTRL2(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'OSC1 Waveform CTRL 2: %s' % self.value

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 9


class DWGSWave(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'OSC1 DWGS Wave: %d' % (int(self.value.intle) + 1)

    def _check_value(self):
        if self.value.intle not in range(0, 64):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 10
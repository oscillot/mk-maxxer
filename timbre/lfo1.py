from microkorg_abstract import MicroKorgAbstractParameter
from constants import STATES, VOICES, WAVEFORMS, T5


class KeySync(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO1 Key Sync: %s' % VOICES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 3):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 38
        self.bits = [4, 5] #probably just one of these


class Wave(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO1 Wave: %s' % WAVEFORMS[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 38
        self.bits = [0, 1] #probably just one of these


class Frequency(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO1 Frequency: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 39


class TempoSync(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO1 TempoSync: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in [0, 1]:
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 40
        self.bits = [7]


class SyncNote(MicroKorgAbstractParameter):
    def __repr__(self):
        try:
            return 'LFO1 SyncNote: %s' % T5[self.value.intle]
        except KeyError:
            return 'WARN! LFO1 SyncNote UNKNOWN: expected 0-15, got %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 16):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 40
        self.bits = range(0, 5)
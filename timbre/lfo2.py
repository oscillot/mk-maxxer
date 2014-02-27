from microkorg_abstract import MicroKorgAbstractParameter
from constants import STATES, VOICES, WAVEFORMS, T5


class KeySync(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO2 Key Sync: %s' % VOICES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 41
        self.bits = [4, 5] #probably just one of these


class Wave(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO2 Wave: %s' % WAVEFORMS[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 41
        self.bits = [0, 1] #probably just one of these
        
        
class Frequency(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO2 Frequency: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 42


class TempoSync(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'LFO2 TempoSync: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in [0, 1]:
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 43
        self.bits = [7]
        
        
class SyncNote(MicroKorgAbstractParameter):
    def __repr__(self):
        try:
            return 'LFO2 SyncNote: %s' % T5[self.value.intle] #this might be
        except KeyError:# worng
            return 'WARN! LFO2 SyncNote UNKNOWN: expected 0-14, got %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 16):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 43
        self.bits = range(0, 5)
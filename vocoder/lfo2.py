from timbre.lfo2 import KeySync as TimbreKeySync
from timbre.lfo2 import Wave as TimbreWave
from timbre.lfo2 import Frequency as TimbreFrequency
from timbre.lfo2 import TempoSync as TimbreTempoSync
from timbre.lfo2 import SyncNote as TimbreSyncNote


class KeySync(TimbreKeySync):
    def _get_offset(self):
        self.offset = 43
        self.bits = [4, 5]


class Wave(TimbreWave):
    def _get_offset(self):
        self.offset = 43
        self.bits = [0, 1]


class Frequency(TimbreFrequency):
    def _get_offset(self):
        self.offset = 44


class TempoSync(TimbreTempoSync):
    def _get_offset(self):
        self.offset = 45
        self.bits = [7]


class SyncNote(TimbreSyncNote):
    def _get_offset(self):
        self.offset = 45
        self.bits = [0, 1, 2, 3, 4]
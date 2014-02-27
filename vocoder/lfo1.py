from timbre.lfo1 import KeySync as TimbreKeySync
from timbre.lfo1 import Wave as TimbreWave
from timbre.lfo1 import Frequency as TimbreFrequency
from timbre.lfo1 import TempoSync as TimbreTempoSync
from timbre.lfo1 import SyncNote as TimbreSyncNote


class KeySync(TimbreKeySync):
    def _get_offset(self):
        self.offset = 40
        self.bits = [4, 5]


class Wave(TimbreWave):
    def _get_offset(self):
        self.offset = 40
        self.bits = [0, 1]


class Frequency(TimbreFrequency):
    def _get_offset(self):
        self.offset = 41


class TempoSync(TimbreTempoSync):
    def _get_offset(self):
        self.offset = 42
        self.bits = [7]


class SyncNote(TimbreSyncNote):
    def _get_offset(self):
        self.offset = 42
        self.bits = [0, 1, 2, 3, 4]
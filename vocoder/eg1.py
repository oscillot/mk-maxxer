from timbre.eg1 import Attack as TimbreAttack
from timbre.eg1 import Decay as TimbreDecay
from timbre.eg1 import Sustain as TimbreSustain
from timbre.eg1 import Release as TimbreRelease


class Attack(TimbreAttack):
    def _get_offset(self):
        self.offset = 32


class Decay(TimbreDecay):
    def _get_offset(self):
        self.offset = 33


class Sustain(TimbreSustain):
    def _get_offset(self):
        self.offset = 34


class Release(TimbreRelease):
    def _get_offset(self):
        self.offset = 35
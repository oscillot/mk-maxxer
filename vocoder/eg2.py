from timbre.eg2 import Attack as TimbreAttack
from timbre.eg2 import Decay as TimbreDecay
from timbre.eg2 import Sustain as TimbreSustain
from timbre.eg2 import Release as TimbreRelease


class Attack(TimbreAttack):
    def _get_offset(self):
        self.offset = 36
        
        
class Decay(TimbreDecay):
    def _get_offset(self):
        self.offset = 37
        
        
class Sustain(TimbreSustain):
    def _get_offset(self):
        self.offset = 38
        
        
class Release(TimbreRelease):
    def _get_offset(self):
        self.offset = 39

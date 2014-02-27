from microkorg_abstract import MicroKorgAbstractParameter
from constants import T4, T3


class Destination(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'patch3 Destination: %s' % T4[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 8):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 48
        self.bits = range(4, 8)
        
        
class Source(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'patch3 Source: %s' % T3[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 8):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 48
        self.bits = range(0, 4)
        
        
class Intensity(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'patch3 Intensity: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 49
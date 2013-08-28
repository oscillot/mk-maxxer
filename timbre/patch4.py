from microkorg_abstract import MicroKorgAbstractParamater
from constants import T4, T3


class Destination(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'patch4 Destination: %s' % T4[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 8):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 50
        self.bits = range(4, 8)
        
        
class Source(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'patch4 Source: %s' % T3[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 8):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 50
        self.bits = range(0, 4)
        
        
class Intensity(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'patch4 Intensity: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 51
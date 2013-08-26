from microkorg_abstract import MicroKorgAbstractParamater


class KeyboardOctave(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'KBD Octave: Shift Octave(s) [%s raw shift]' % self.value.intle

    def _check_value(self):
        pass
        # print self.value.bin
        # print self.value.intle
        # if self.value not in range(-3, 4):
        #     raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 37
        self.bits = range(0, 8)
from microkorg_abstract import MicroKorgAbstractParamater


class KeyboardOctave(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'KBD Octave: Shift %d Octave(s)' % self.value

    def _check_value(self):
        if self.value not in range(-3, 4):
            raise ValueError('Parameter is out of range: ' + self.value)

    def _get_offset(self):
        self.offset = 37
        self.bits = [range(0, 8)]
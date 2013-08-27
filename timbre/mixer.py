from microkorg_abstract import MicroKorgAbstractParamater


class OSC1Level(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'MIXER OSC1 Level: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 16


class OSC2Level(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'MIXER OSC2 Level: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 17


class Noise(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'MIXER Noise: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 18
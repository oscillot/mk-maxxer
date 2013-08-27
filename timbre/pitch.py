from microkorg_abstract import MicroKorgAbstractParamater


class Tune(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'PITCH Tune: %d+/-50[cent]' % (self.value.intle - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 3


class BendRange(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'PITCH Bend Range: %d+/-12[note]' % (self.value.intle - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 4


class Transpose(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'PITCH Transpose: %d+/-24[note]' % (self.value.intle - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 5


class VibratoInt(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'PITCH Vibrato Int: %d+/-63' % (self.value.intle - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 6


class PortamentoTime(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'PITCH Portamento Time: %s' % self.value

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 15
        self.bits = range(7)
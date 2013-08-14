from microkorg_abstract import MicroKorgAbstractParamater


class LFOSpeed(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'MODFX LFO Speed: %s' % self.value

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 23
        self.bits = range(0, 8)


class Depth(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'MODFX Depth: %s' % self.value

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 24
        self.bits = range(0, 8)


class Type(MicroKorgAbstractParamater):
    def __repr__(self):
        TYPES = {
            0: 'Chorus/Flanger',
            1: 'Ensemble',
            2: 'Phaser',

        }
        #FIXME
        try:
            return 'MODFX Type: %s' % TYPES[self.value]
        except KeyError:
            return 'MODFX Type: FIXME'

    def _check_value(self):
        if self.value not in range(0, 3):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 25
        self.bits = range(0, 8)
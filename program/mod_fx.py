from microkorg_abstract import MicroKorgAbstractParameter


class LFOSpeed(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'MODFX LFO Speed: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle
            .intle)

    def _get_offset(self):
        self.offset = 23
        self.bits = range(0, 8)


class Depth(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'MODFX Depth: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle
            .intle)

    def _get_offset(self):
        self.offset = 24
        self.bits = range(0, 8)


class Type(MicroKorgAbstractParameter):
    def __repr__(self):
        TYPES = {
            0: 'Chorus/Flanger',
            1: 'Ensemble',
            2: 'Phaser',

        }
        try:
            return 'MODFX Type: %s' % TYPES[self.value.intle]
        except KeyError:
            return 'WARN! MODFX Type UNKNOWN!: expected 0-2, got %s' % self\
                .value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %d' % self.value.int)

    def _get_offset(self):
        self.offset = 25
        self.bits = range(0, 8)
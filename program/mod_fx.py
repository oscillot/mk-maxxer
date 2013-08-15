from bitstring import BitArray

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
        return 'MODFX Type: %s' % TYPES[self.value]

    def _bitmask(self):
        b = BitArray(uint=self.value, length=8)
        keep = b.bin[0:2]
        discard = b.bin[2:] #might need this later?
        new_bin = keep[::-1].zfill(8)
        b2 = BitArray(bin='0b%s' % new_bin)
        self.value = b2.int

    def _check_value(self):
        if self.value not in range(0, 3):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 25
        self.bits = range(0, 8)
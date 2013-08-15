from microkorg_abstract import MicroKorgAbstractParamater


class ModSelect(MicroKorgAbstractParamater):
    def __repr__(self):
        MODS = {
            0: 'Off',
            1: 'Ring',
            2: 'Sync',
            3: 'RingSync'
        }
        return 'OSC2 Mod Select: %s' % MODS[self.value]

    def _check_value(self):
        if self.value not in range(0, 4):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 12
        self.bits = [4, 5]


class Wave(MicroKorgAbstractParamater):
    def __repr__(self):
        WAVES = {
            0: 'Saw',
            1: 'Square',
            2: 'Triangle',
        }
        return 'OSC2 Wave: %s' % WAVES[self.value]

    def _check_value(self):
        if self.value not in range(0, 3):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 13
        self.bits = [0, 1]


class Semitone(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'OSC2 Semitone: %d+/-24[note]' % (int(self.value) - 64)

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 14


class Tune(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'OSC2 Tune: %d+/-63' % (int(self.value) - 64)

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 15
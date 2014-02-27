from microkorg_abstract import MicroKorgAbstractParameter


class ModSelect(MicroKorgAbstractParameter):
    def __repr__(self):
        MODS = {
            0: 'Off',
            1: 'Ring',
            2: 'Sync',
            3: 'RingSync'
        }
        return 'OSC2 Mod Select: %s' % MODS[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 12
        self.bits = [4, 5]


class Wave(MicroKorgAbstractParameter):
    def __repr__(self):
        WAVES = {
            0: 'Saw',
            1: 'Square',
            2: 'Triangle',
        }
        return 'OSC2 Wave: %s' % WAVES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 3):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 13
        self.bits = [0, 1]


class Semitone(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'OSC2 Semitone: %d+/-24[note]' % (int(self.value.intle) - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 14


class Tune(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'OSC2 Tune: %d+/-63' % (int(self.value.intle) - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 15
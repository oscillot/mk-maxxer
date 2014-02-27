from microkorg_abstract import MicroKorgAbstractParameter


class Attack(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'EG1 Attack: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 30


class Decay(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'EG1 Decay: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 31


class Sustain(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'EG1 Sustain: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 32


class Release(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'EG1 Release: %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 33
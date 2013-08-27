from microkorg_abstract import MicroKorgAbstractParamater


class Type(MicroKorgAbstractParamater):
    def __repr__(self):
        TYPES = {
            0: '24LPF',
            1: '12LPF',
            2: '12BPF',
            3: '12HPF'
        }
        return 'FILTER Type: %s' % TYPES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 19


class Cutoff(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'FILTER Cutoff: %s' % self.value

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 20


class Resonance(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'FILTER Resonance: %s' % self.value

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 21


class EG1Intensity(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'FILTER EG1 Intensity: %d+/-63' % (int(self.value.intle) - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 22


class VelocitySense(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'FILTER Velocity Sense: %d' % (int(self.value.intle) - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 23


class KeyboardTrack(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'FILTER Keyboard Track: %d+/-63' % (int(self.value.intle) - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 24
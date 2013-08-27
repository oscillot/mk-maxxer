from microkorg_abstract import MicroKorgAbstractParamater
from constants import STATES


class Level(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'AMP Level: %s' % self.value

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 25


class Panpot(MicroKorgAbstractParamater):
    def __repr__(self):
        pp = int(self.value.intle)
        if pp < 0:
            repr_val = 'L%d' % abs(pp)
        elif pp == 0:
            repr_val = 'CNT'
        elif pp > 0:
            repr_val = 'R%d' % pp
        else:
            raise ValueError('Shit: %s' % self.value.intle)
        return 'AMP Panpot: %s' % repr_val

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 26


class AmpSW(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'AMP Amp Sw (0=EG2): %s' % self.value

    def _check_value(self):
        # if self.value.intle not in range(0, 128):
        #     raise ValueError('Parameter is out of range: %s' % self.value.intle)
        pass

    def _get_offset(self):
        self.offset = 27
        self.bits = [6]


class Distortion(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'AMP Distortion: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in [0, 1]:
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 27
        self.bits = [0]


class VelocitySense(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'AMP Velocity Sense: %d' % (int(self.value.intle) - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 28


class KeyboardTrack(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'AMP Keyboard Track: %d+/-63' % (int(self.value.intle) - 64)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 29
from microkorg_abstract import MicroKorgAbstractParameter
from constants.states import STATES


class HPFGate(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'HPFGate: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 2):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 12
        self.bits = [0]


class HPFLevel(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'HPFGate: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 18


class GateSense(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'HPFGate: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 19


class Threshold(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'HPFGate: %s' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %s' % self.value.intle)

    def _get_offset(self):
        self.offset = 20
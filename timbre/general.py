from constants import STATES
from microkorg_abstract import MicroKorgAbstractParamater


class MidiChannel(MicroKorgAbstractParamater):
    def __repr__(self):
        repr_str = 'MIDI Channel: %s' % self.value
        if self.value == '-1':
            repr_str += ' (Global)'
        return repr_str

    def _check_value(self):
        if self.value not in range(-1, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 0


class AssignMode(MicroKorgAbstractParamater):
    def __repr__(self):
        MODES = {
            0: 'Mono',
            1: 'Poly',
            2: 'Unison'
        }
        return 'SYN Assign Mode: %s' % MODES[self.value]

    def _check_value(self):
        if self.value not in range(0, 3):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 1
        self.bits = [6, 7]


class EG2Reset(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'SYN EG2 Reset: %s' % STATES[self.value]

    def _check_value(self):
        if self.value not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 1
        self.bits = [5]


class EG1Reset(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'SYN EG1 Reset: %s' % STATES[self.value]

    def _check_value(self):
        if self.value not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 1
        self.bits = [4]


class TriggerMode(MicroKorgAbstractParamater):
    def __repr__(self):
        MODES = {
            0: 'Single',
            1: 'Multi'
        }
        return 'SYN Trigger Mode: %s' % MODES[self.value]

    def _check_value(self):
        if self.value not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 1
        self.bits = [3]


class KeyPriority(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'SYN Key Priority: %s (0=Last)' % self.value

    def _check_value(self):
        # if self.value not in range(0, 2):
        #     raise ValueError('Parameter is out of range: %d' % self.value)
        pass

    def _get_offset(self):
        self.offset = 1
        self.bits = [0, 1]
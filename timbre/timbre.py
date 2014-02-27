from constants import STATES, plus_minus
from microkorg_abstract import MicroKorgAbstractParameter


class MidiChannel(MicroKorgAbstractParameter):
    def __repr__(self):
        repr_str = 'MIDI Channel: %s' % self.value.intle
        if self.value.intle == -1:
            repr_str += ' (Global)'
        return repr_str

    def _check_value(self):
        if self.value.int not in range(-1, 128):
            raise ValueError('Parameter is out of range: %d' % self.value
            .intle)

    def _get_offset(self):
        self.offset = 0


class AssignMode(MicroKorgAbstractParameter):
    def __repr__(self):
        MODES = {
            0: 'Mono',
            1: 'Poly',
            2: 'Unison',
            3: 'FIXME'
        }
        return 'SYN Assign Mode: %s' % MODES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 1
        self.bits = [6, 7]


class EG2Reset(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'SYN EG2 Reset: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 1
        self.bits = [5]


class EG1Reset(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'SYN EG1 Reset: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 1
        self.bits = [4]


class TriggerMode(MicroKorgAbstractParameter):
    def __repr__(self):
        MODES = {
            0: 'Single',
            1: 'Multi'
        }
        return 'SYN Trigger Mode: %s' % MODES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 1
        self.bits = [3]


class KeyPriority(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'SYN Key Priority: %s (0=Last)' % self.value.intle

    def _check_value(self):
        # if self.value.intle not in range(0, 2):
        #     raise ValueError('Parameter is out of range: %d' % self.value.intle)
        pass

    def _get_offset(self):
        self.offset = 1
        self.bits = [0, 1]


class UnisonDetune(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'SYN Unison Detune: %s [cent]' % plus_minus(self.value.intle)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 2
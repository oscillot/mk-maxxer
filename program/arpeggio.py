from bitstring import BitArray

from microkorg_abstract import MicroKorgAbstractParamater
from constants import STATES, T12


class TriggerLength(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Trigger Length: %d Step' % (int(self.value.uint) + 1)

    def _check_value(self):
        if self.value.uint not in range(0, 8):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 14
        self.bits = range(0, 3)


class TriggerPattern(MicroKorgAbstractParamater):
    def __repr__(self):
        repr_msg = ''
        for i, v in enumerate(self.value.uint):
            repr_msg += 'ARP Trigger Pattern %d: %s\n' % (i + 1, STATES[v])
        return repr_msg

    def _check_value(self):
        for v in self.value:
            if v not in [0, 1]:
                raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 15
        self.bits = range(0, 8)


class VoiceMode(MicroKorgAbstractParamater):
    def __repr__(self):

        VOICEMODES = {
            0: 'Single',
            2: 'Layer',
            3: 'Vocoder'
        }

        return 'ARP Voice Mode: %s' % VOICEMODES[self.value.int]

    def _check_value(self):
        if self.value.uint not in [0, 2, 3]:
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 16
        self.bits = [4, 5]


class ScaleKey(MicroKorgAbstractParamater):
    def __repr__(self):
        SCALES = {
            0: 'C',
            1: 'C#',
            2: 'D',
            3: 'D#',
            4: 'E',
            5: 'F',
            6: 'F#',
            7: 'G',
            8: 'G#',
            9: 'A',
            10: 'A#',
            11: 'B',
        }

        return 'ARP Scale Key: %s=%s' % (self.value.int,
                                         SCALES[self.value.int])

    def _check_value(self):
        if self.value.uint not in range(0, 12):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 17
        self.bits = range(4, 8)


class ScaleType(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Scale Type: %s (0=Equal Temp)' % self.value.int

    def _check_value(self):
        # if self.value.uint not in [0]:
        #     raise ValueError('Parameter is out of range: %d' % self.value.uint)
        pass

    def _get_offset(self):
        self.offset = 17
        self.bits = range(0, 4)


class TempoMSB(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Tempo (MSB): %s bpm (seq tempo)' % self.value

    def _check_value(self):
        if self.value.uint not in range(20, 301):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 30
        self.bits = range(0, 8)


class TempoLSB(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Tempo (LSB): %s bpm (seq tempo)' % self.value

    def _check_value(self):
        if self.value.uint not in range(20, 301):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 31
        self.bits = range(0, 8)


class OnOff(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP On/Off: %s' % STATES[self.value.int]

    def _check_value(self):
        if self.value.uint not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 32
        self.bits = [7]


class Latch(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Latch: %s' % STATES[self.value.int]

    def _check_value(self):
        if self.value.uint not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 32
        self.bits = [6]


class Target(MicroKorgAbstractParamater):
    def __repr__(self):
        TARGETS = {
            '00': 'Both',
            '01': 'Timbre 1',
            '10': 'Timbre 2'
        }
        return 'ARP Target: %s' % TARGETS[self.value.bin]

    def _check_value(self):
        if self.value.bin not in ['00', '01', '10']:
            raise ValueError('Parameter is out of range: %d' % self.value.bin)

    def _get_offset(self):
        self.offset = 32
        self.bits = [4, 5]


class KeySync(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Key Sync: %s' % STATES[self.value.int]

    def _check_value(self):
        if self.value.uint not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 32
        self.bits = [0]


class Type(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Type: %s' % T12[self.value.int]

    def _check_value(self):
        if self.value.uint not in range(0, 6):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 33
        self.bits = range(0, 4)


class Range(MicroKorgAbstractParamater):
    def __repr__(self):
        octaves = []
        for i, c in enumerate(self.value.bin):
            if c == '1':
                octaves += [i + 1]

        return 'ARP Range Octave(s): %s' % str(octaves)

    def _check_value(self):
        if abs(self.value.uint) not in range(0, 16):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 33
        self.bits = range(4, 8)


class GateTime(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Gate Time: %s%%' % self.value

    def _check_value(self):
        if self.value.uint not in range(0, 101):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 34
        self.bits = range(0, 8)


class Resolution(MicroKorgAbstractParamater):
    def __repr__(self):
        RESOS = {
            0: '1/24',
            1: '1/16',
            2: '1/12',
            3: '1/8',
            4: '1/6',
            5: '1/4'
        }
        return 'ARP Resolution: %s' % RESOS[self.value]

    def _check_value(self):
        if self.value.uint not in range(0, 6):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 35
        self.bits = range(0, 8)


class Swing(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'ARP Swing: +/-%s%%' % self.value

    def _check_value(self):
        if self.value.uint not in range(0, 101):
            raise ValueError('Parameter is out of range: %d' % self.value.uint)

    def _get_offset(self):
        self.offset = 36
        self.bits = range(0, 8)
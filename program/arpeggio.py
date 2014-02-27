from microkorg_abstract import MicroKorgAbstractParameter
from constants import STATES, T12, plus_minus


class TriggerLength(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Trigger Length: %d Step' % (int(self.value.intle) + 1)

    def _check_value(self):
        if self.value.intle not in range(0, 8):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 14
        self.bits = range(0, 3)


class TriggerPattern(MicroKorgAbstractParameter):
    def __repr__(self):
        repr_msg = ''
        for i, b in enumerate(self.value.bin):
            repr_msg += 'ARP Trigger Pattern %d: %s\n' % (i + 1, STATES[b])
        return repr_msg

    def _check_value(self):
        for i, b in enumerate(self.value.bin):
            if b not in ['0', '1']:
                raise ValueError('Parameter is out of range: %s at bit '
                                 'position: %d' % (b, i))

    def _get_offset(self):
        self.offset = 15
        self.bits = range(0, 8)


class VoiceMode(MicroKorgAbstractParameter):
    def __repr__(self):

        VOICEMODES = {
            0: 'Single',
            2: 'Layer',
            3: 'Vocoder'
        }

        return 'ARP Voice Mode: %s' % VOICEMODES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in [0, 2, 3]:
            raise ValueError('Parameter is out of range: %s' % self.value
            .intle)

    def _get_offset(self):
        self.offset = 16
        self.bits = [4, 5]


class ScaleKey(MicroKorgAbstractParameter):
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

        return 'ARP Scale Key: %s=%s' % (self.value.intle,
                                         SCALES[self.value.intle])

    def _check_value(self):
        if self.value.intle not in range(0, 12):
            raise ValueError('Parameter is out of range: %d' % self.value
            .intle)

    def _get_offset(self):
        self.offset = 17
        self.bits = range(4, 8)


class ScaleType(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Scale Type: %s (0=Equal Temp)' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 16): #this is only checking for a
        # 4-bit number, the docs give NO idea what to expect here:
#+-----------+-------------------+-----------------------------------+
#| 17 B4~7 | Scale Key | 0=C |
#| -------+-------------------+-----------------------------------+
#| B0~3 | Scale Type | 0=Equal Temp |
#+-----------+-------------------+-----------------------------------+
            raise ValueError('Parameter is out of range: %d' % self.value.intle)
        #pass

    def _get_offset(self):
        self.offset = 17
        self.bits = range(0, 4)


class Tempo(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Tempo: %s bpm (seq tempo)' % self.value.intle

    def _check_value(self):
        #print self.value.bin
        if self.value.intle not in range(0, 256): #another byte-only check,
        # spec says this but I keep getting zeroes:
        #+-----------+-------------------+-----------------------------------+
        #| ARPEGGIO |
        #+-----------+-------------------+-----------------------------------+
        #| 30 | tempo (MSB) | 20~300 |
        #| 31 | (LSB) | (SEQ tempo) |
        #+-----------+-------------------+-----------------------------------+
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 30
        self.bits = range(0, 16)


class OnOff(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP On/Off: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 32
        self.bits = [7]


class Latch(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Latch: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 32
        self.bits = [6]


class Target(MicroKorgAbstractParameter):
    def __repr__(self):
        TARGETS = {
            0: 'Both',
            1: 'Timbre 1',
            2: 'Timbre 2'
        }
        try:
            return 'ARP Target: %s' % TARGETS[self.value.intle]
        except KeyError:
            return 'WARN! ARP Target UNKNOWN!: expected 0-2, got %s' % self\
                .value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 4):
            raise ValueError('Parameter is out of range: %d' % self.value
            .intle)

    def _get_offset(self):
        self.offset = 32
        self.bits = [4, 5]


class KeySync(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Key Sync: %s' % STATES[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 2):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 32
        self.bits = [0]


class Type(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Type: %s' % T12[self.value.intle]

    def _check_value(self):
        if self.value.intle not in range(0, 6):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 33
        self.bits = range(0, 4)


class Range(MicroKorgAbstractParameter):
    def __repr__(self):
        octaves = []
        for i, c in enumerate(self.value.bin):
            if c == '1':
                octaves += [i + 1]

        return 'ARP Range Octave(s): %s' % str(octaves)

    def _check_value(self):
        if abs(self.value.intle) not in range(0, 16):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 33
        self.bits = range(4, 8)


class GateTime(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Gate Time: %s%%' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 101):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 34
        self.bits = range(0, 8)


class Resolution(MicroKorgAbstractParameter):
    def __repr__(self):
        RESOS = {
            0: '1/24',
            1: '1/16',
            2: '1/12',
            3: '1/8',
            4: '1/6',
            5: '1/4'
        }
        try:
            return 'ARP Resolution: %s' % RESOS[self.value.intle]
        except KeyError:
            return 'WARN! ARP Resolution UNKNOWN: Expcted 0-5, got %d' % self.value.intle

    def _check_value(self):
        if self.value.intle not in range(0, 8):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 35
        self.bits = range(0, 4)


class Swing(MicroKorgAbstractParameter):
    def __repr__(self):
        return 'ARP Swing: +/-%s%%' % plus_minus(self.value.intle)

    def _check_value(self):
        if self.value.intle not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value.intle)

    def _get_offset(self):
        self.offset = 36
        self.bits = range(0, 8)
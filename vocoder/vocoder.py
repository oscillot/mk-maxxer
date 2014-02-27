from timbre import MidiChannel as TimbreMidiChannel
from timbre import AssignMode as TimbreAssignMode
from timbre import EG1Reset as TimbreEG1Reset
from timbre import EG2Reset as TimbreEG2Reset
from timbre import TriggerMode as TimbreTriggerMode
from timbre import KeyPriority as TimbreKeyPriority
from timbre import UnisonDetune as TimbreUnisonDetune


class MidiChannel(TimbreMidiChannel):
    pass


class AssignMode(TimbreAssignMode):
    pass


class EG2Reset(TimbreEG2Reset):
    pass


class EG1Reset(TimbreEG1Reset):
    pass


class TriggerMode(TimbreTriggerMode):
    pass


class KeyPriority(TimbreKeyPriority):
    pass


class UnisonDetune(TimbreUnisonDetune):
    pass
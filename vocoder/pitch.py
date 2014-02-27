from microkorg_abstract import MicroKorgAbstractParameter
from timbre.pitch import Tune as TimbreTune
from timbre.pitch import BendRange as TimbreBendRange
from timbre.pitch import Transpose as TimbreTranspose
from timbre.pitch import VibratoInt as TimbreVibratoInt
from timbre.pitch import PortamentoTime as TimbrePortamentoTime


class Tune(TimbreTune):
    pass


class BendRange(TimbreBendRange):
    pass


class Transpose(TimbreTranspose):
    pass


class VibratoInt(TimbreVibratoInt):
    pass


class PortamentoTime(TimbrePortamentoTime):
    def _get_offset(self):
        self.offset = 14
        self.bits = range(7)
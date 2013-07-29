from bitstring import BitArray

from helpers import endian_translate


class MicroKorgAbstractData():
    def read_bytes(self, number=1):
        return self.data.read(number)

    def get_next_bytes(self, number=1):
        byts = self.read_bytes(number)
        return ord(byts)

    def _get_binary_data(self, number=1):
        byte = self.get_next_bytes(number)
        b = BitArray(uint=byte, length=8)
        return b.bin.zfill(8*number)


class MicroKorgAbstractParamater():
    def __init__(self, value):
        self.value = value
        self._get_offset()
        self._fix_endianness()
        self._check_value()

    def _check_value(self):
        raise NotImplementedError

    def _get_offset(self):
        raise NotImplementedError

    def _fix_endianness(self):
        if self.bits == range(0, 8):
            self.value = endian_translate(self.value)
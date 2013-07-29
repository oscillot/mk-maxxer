from bitstring import BitArray


class MicroKorgAbstractData():
    def read_bytes(self, number=1):
        return self.data.read(number)

    def get_next_bytes(self, number=1):
        byts = self.read_bytes(number)
        return ord(byts)

    def _get_binary_data(self, number=1):
        byte = self.get_next_bytes(number)
        b = BitArray(byte)
        return b.bin.zfill(8*number)

class MicroKorgAbstractParamater():
    def __init__(self, value):
        self.value = value
        self._get_offset()
        self._check_value()

    def _check_value(self):
        raise NotImplementedError

    def _get_offset(self):
        raise NotImplementedError
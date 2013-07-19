from bitstring import BitArray


class MicroKorgAbstractData():
    def get_next_bytes(self, number=1):
        return self.data.read(number)

    def _get_binary_data(self, number=1):
        byte = self.get_next_bytes(number)
        b = BitArray(hex(ord(byte)))
        return b.bin.zfill(8*number)
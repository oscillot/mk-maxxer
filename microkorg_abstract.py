import struct
import traceback
from bitstring import BitArray
from byte_counter import ByteCounter

bc = ByteCounter()


class MicroKorgAbstractData():
    def read_bytes(self, number=1):
        bc.count(number)
        return self.data.read(number)

    def get_next_bytes(self, number=1):
        byts = self.read_bytes(number)
        fmt = '>'
        for r in range(number):
            fmt += 'b'
        #e.g. fmt string might be '>bbb'
        return struct.unpack(fmt, byts)[0]

    def _get_binary_data(self, number=1):
        byte = self.get_next_bytes(number)
        b = BitArray(uint=byte, length=8)
        return b.bin.zfill(8*number)


class MicroKorgAbstractParamater():
    def __init__(self, value):
        self.value = value
        self.mask = set()
        self._bitmask()
        self._get_offset()
        #This is temp. We will enforce this once all decoding is in line.
        try:
            self._check_value()
        except ValueError as e:
            print traceback.format_exc()

    def _bitmask(self):
        """
        This exists to be overwritten in the cases where something that is
        documented as a byte seems to actually be encoded into a bitmap with
        a bunch of junk data (possibly leftovers from the synths ms2000
        origins?) At any rate, bitmasking will allow us to discard the junk
        data and continue normally.
        """
        pass


    def _check_value(self):
        raise NotImplementedError

    def _get_offset(self):
        """
        I did this so I wouldn't forget to set the offset. It's totally
        unnecessary to do this this way and will likely go away eventually
        """
        raise NotImplementedError
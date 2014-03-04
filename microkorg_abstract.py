from bitstring import BitStream


class SysExStream(BitStream):
    def zfill(self, endian='be'):
        if endian.lower() not in ['be', 'le']:
            raise ValueError('Endianness must be one of `le`, `be.`')
        while len(self.value) % 8 != 0:
            if 'be' == endian:
                self.value.append('0b0')
            elif 'le' == endian:
                self.prepend('0b0')
            print len(self.value)


class MicroKorgAbstractData():
    def read_bits(self, number=1):
        print 'Byte Position: %d' % self.program_bitstream.bytepos
        return self.program_bitstream.read(number)

    def read_bytes(self, number=1):
        print 'Bit Position: %d' % self.program_bitstream.bitpos
        return self.read_bits(number * 8)

    def zfill(self, bits):
        while len(bits) % 8 != 0:
            bits.append('0b0')


class MicroKorgAbstractParameter():
    def __init__(self, value):
        self.value = SysExStream(bin='0b%s' % value.bin).zfill()
        self._get_offset()
        if hasattr(self, 'mask'):
            self._mask()
        self._check_value()

    def _mask(self):
        for idx in self.mask:
            self.value.overwrite('0b0', pos=(idx))

    def _check_value(self):
        raise NotImplementedError

    def _get_offset(self):
        """
        I did this so I wouldn't forget to set the offset. It's totally
        unnecessary to do this this way and will likely go away eventually
        """
        raise NotImplementedError
from bitstring import BitArray


def get_bits(data):
    zeroes = []
    ones = []
    s = data.bin
    for i, c in enumerate(s):
        if c == '0':
            zeroes.append(i)
        if c == '1':
            ones.append(i)
    return {'ones': ones, 'zeroes': zeroes}


def get_ones(data):
    bits = get_bits(data)
    return bits['ones']


def get_zeroes(data):
    bits = get_bits(data)
    return bits['ones']


def get_bit(data):
    ones = get_ones(data)
    if len(ones) != 1:
        raise ValueError('Not exactly one bit set: %s' % len(ones))
    return ones[0]


# b = BitArray(bin='0b01011010')
# b = BitArray(bin='0b01000000')
# print get_bits(b)
# print get_zeroes(b)
# print get_ones(b)
# print get_bit(b)
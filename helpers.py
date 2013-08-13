from bitstring import BitArray

#this probably isn't used anymore now that the T# tables are added in tn.py
def slope((x1, y1), (x2, y2)):
    return (y2-y1)/(x2-x1)


def endian_translate(number):
        b = BitArray(uint=number, length=8)
        bprime = BitArray(uint=int(b.bin[::-1], 2), length=8)
        return bprime.uint
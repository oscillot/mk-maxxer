

class ByteCounter(object):
    def __init__(self):
        self.position = -1

    def count(self, number=1):
        self.position += number
        print '\n\tByte: %d' % self.position
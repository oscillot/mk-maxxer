from microkorg_abstract import MicroKorgAbstractParamater


class Sync(MicroKorgAbstractParamater):
    def __repr__(self):
        STATES = {
            0: 'Off',
            1: 'On'
        }
        return 'DLY Sync: %s' % STATES[self.value]

    def _check_value(self):
        if self.value not in [0, 1]:
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 19
        self.bits = [7]


class TimeBase(MicroKorgAbstractParamater):
    def __repr__(self):
        BASES = {
            0: '1/32',
            1: '1/28',
            2: '1/24',
            3: '1/20',
            4: '1/18',
            5: '1/16',
            6: '1/14',
            7: '1/12',
            8: '1/10',
            9: '1/8',
            10: '1/6',
            11: '1/4',
            12: '1/3',
            13: '1/2',
            14: '1/1'
        }
        return 'DLY Time Base: %s (THIS MAY BE WRONG!)' % BASES[self.value]

    def _check_value(self):
        if self.value not in range(0, 15):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 19
        self.bits = range(0, 4)


class Time(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Time: %s' % self.value

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 20
        self.bits = range(0, 8)


class Depth(MicroKorgAbstractParamater):
    def __repr__(self):
        return 'DLY Depth: %s' % self.value

    def _check_value(self):
        if self.value not in range(0, 128):
            raise ValueError('Parameter is out of range: %d' % self.value)

    def _get_offset(self):
        self.offset = 21
        self.bits = range(0, 8)


class Type(MicroKorgAbstractParamater):
    def __repr__(self):
        TYPES = {
            0: 'Stereo Delay',
            1: 'Cross Delay',
            2: 'L/R Delay',
        }
        repr_msg = ''
        for i, v in enumerate(self.value):
            if v == 1:
                repr_msg += 'DLY Type: %s\n' % TYPES[i]
        return repr_msg

    def _check_value(self):
        for v in self.value:
            if v not in [0, 1]:
                raise ValueError('Parameter is out of range: %d' % v)

    def _get_offset(self):
        self.offset = 22
        self.bits = range(0, 8)

    def _fix_endianness(self):
        #Need to short-circuit here
        pass
import itertools

GOOD_STATUS = 0xf0

#for the microkorg specificaly A11-B88
PGMS = [''.join(f) for f in itertools.product(['A', 'B'],
                                        [str(r) for r in range(1,9)],
                                        [str(r) for r in range(1,9)])]

MFGR_LOOKUPS = {
    0x01: 'Sequential Circuits',
    0x02: 'Big Briar',
    0x03: 'Octave _ Plateau',
    0x04: 'Moog',
    0x05: 'Passport Designs',
    0x06: 'Lexicon',
    0x07: 'Kurzweil',
    0x08: 'Fender',
    0x09: 'Gulbransen',
    0x0A: 'Delta Labs',
    0x0B: 'Sound Comp.',
    0x0C: 'General Electro',
    0x0D: 'Techmar',
    0x0E: 'Matthews Research',
    0x10: 'Oberheim',
    0x11: 'PAIA',
    0x12: 'Simmons',
    0x13: 'DigiDesign',
    0x14: 'Fairlight',
    0x16: 'JL Cooper',
    0x17: 'Lowery',
    0x18: 'Lin',
    0x19: 'Emu',
    0x1B: 'Peavey',
    0x20: 'Bon Tempi',
    0x21: 'S.I.E.L.',
    0x23: 'SyntheAxe',
    0x24: 'Hohner',
    0x25: 'Crumar',
    0x26: 'Solton',
    0x27: 'Jellinghaus Ms',
    0x28: 'CTS',
    0x29: 'PPG',
    0x2F: 'Elka',
    0x36: 'Cheetah',
    0x3E: 'Waldorf',
    0x40: 'Kawai',
    0x41: 'Roland',
    0x42: 'Korg',
    0x43: 'Yamaha',
    0x44: 'Casio',
    0x45: 'Akai',
    0x7D: 'Educational Use',  # SPECIAL CASE ANYONE CAN USE SO LONG AS USE IS
    #  SOLELY NON-COMMERCIAL
    0x0041: 'Microsoft',
}

DUMP_TYPES = {
    0x0E: 'GBL Data Dump Request',
    0x0F: 'ALL Data Dump Request',
    0x10: 'Current PGM Data Dump Request',
    0x11: 'PGM Write Request',
    0x1C: 'PGM Data Dump Request', #needs 7-bit dest pp pgm
    0x21: 'Write Completed',
    0x22: 'Write Error',
    0x23: 'Data Load Completed',
    0x24: 'Data Load Error',
    0x26: 'Data Format Error',
    0x40: 'Current PGM Data Dump',
    0x4C: 'PGM Data Dump',
    0x50: 'ALL Data Dump',
    0x51: 'GBL Data Dump',
}
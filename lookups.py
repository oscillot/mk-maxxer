import itertools

GOOD_STATUS = 'f0'

#for the microkorg specificaly A11-B88
PGMS = [''.join(f) for f in itertools.product(['A', 'B'],
                                        [str(r) for r in range(1,9)],
                                        [str(r) for r in range(1,9)])]

MFGR_LOOKUPS = {
    '01': 'Sequential Circuits',
    '02': 'Big Briar',
    '03': 'Octave _ Plateau',
    '04': 'Moog',
    '05': 'Passport Designs',
    '06': 'Lexicon',
    '07': 'Kurzweil',
    '08': 'Fender',
    '09': 'Gulbransen',
    '0A': 'Delta Labs',
    '0B': 'Sound Comp.',
    '0C': 'General Electro',
    '0D': 'Techmar',
    '0E': 'Matthews Research',
    '10': 'Oberheim',
    '11': 'PAIA',
    '12': 'Simmons',
    '13': 'DigiDesign',
    '14': 'Fairlight',
    '16': 'JL Cooper',
    '17': 'Lowery',
    '18': 'Lin',
    '19': 'Emu',
    '1B': 'Peavey',
    '20': 'Bon Tempi',
    '21': 'S.I.E.L.',
    '23': 'SyntheAxe',
    '24': 'Hohner',
    '25': 'Crumar',
    '26': 'Solton',
    '27': 'Jellinghaus Ms',
    '28': 'CTS',
    '29': 'PPG',
    '2F': 'Elka',
    '36': 'Cheetah',
    '3E': 'Waldorf',
    '40': 'Kawai',
    '41': 'Roland',
    '42': 'Korg',
    '43': 'Yamaha',
    '44': 'Casio',
    '45': 'Akai',
    '7D': 'Educational Use',  # SPECIAL CASE ANYONE CAN USE SO LONG AS USE IS
    #  SOLELY NON-COMMERCIAL
    '0041': 'Microsoft',
}

DUMP_TYPES = {
    '0E': 'GBL Data Dump Request',
    '0F': 'ALL Data Dump Request',
    '10': 'Current PGM Data Dump Request',
    '11': 'PGM Write Request',
    '1C': 'PGM Data Dump Request', #needs 7-bit dest pp pgm
    '21': 'Write Completed',
    '22': 'Write Error',
    '23': 'Data Load Completed',
    '24': 'Data Load Error',
    '26': 'Data Format Error',
    '40': 'Current PGM Data Dump',
    '4C': 'PGM Data Dump',
    '50': 'ALL Data Dump',
    '51': 'GBL Data Dump',
}
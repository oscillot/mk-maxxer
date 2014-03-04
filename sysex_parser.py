import os
from bitstring import BitStream

from lookups import *

from microkorg_pgm import MicroKorgPGM

here = os.path.abspath(os.path.dirname(__file__))


f_sysex = open(os.path.join(here, 'sample_data/microkorg-6-30-13.syx'), 'rb')

sysex = f_sysex.read()
f_sysex.close()

# print len(sysex)

sysex_bitstream = BitStream(bytes=sysex)

status = sysex_bitstream.read(8).hex

if status != GOOD_STATUS:
    raise ValueError('Bad Status: %s Expected: 0xf0' % status)
else:
    print 'Status OK!'

mfgr_code = sysex_bitstream.read(8).hex
if mfgr_code == '0x00':  # Indicates extended MFGR bytes
    # discard the first byte and read the next two (e.g. see MS above)
    mfgr_code = sysex_bitstream.read(16).hex

mfgr = MFGR_LOOKUPS[mfgr_code]
print 'SysEx for "%s" device.' % mfgr

family_id = sysex_bitstream.read(8).hex
if family_id == '3a':
    print 'MS2000 series Family Product'
else:
    print 'Unknown Family ID: %s' % family_id

member_id = sysex_bitstream.read(8).hex
if member_id == '58':
    print 'Unknown Member ID: %s (Micro-Korg?)' % member_id
else:
    print 'Unknown Member ID: %s' % member_id

if status == GOOD_STATUS:
    dump_type = DUMP_TYPES[sysex_bitstream.read(8).hex]
    print 'SysEx Msg Type: %s' % dump_type


for pgm in PGMS:
    print 'PGM: %s' % pgm
    locals()[pgm] = MicroKorgPGM(sysex_bitstream.read(254 * 8)) # read 254
    # bytes off...


# print A18
# print B88
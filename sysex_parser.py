import os
import StringIO

from lookups import *

from microkorg_pgm import MicroKorgPGM

here = os.path.abspath(os.path.dirname(__file__))


def unpack_sysex(byte):
    return int(hex(ord(byte)), 16)

f_sysex = open(os.path.join(here, 'sample_data/microkorg-6-30-13.syx'), 'rb')

sysex = f_sysex.read()
f_sysex.close()

# print len(sysex)

sysex_buf = StringIO.StringIO(sysex)

status = unpack_sysex(sysex_buf.read(1))

if status != GOOD_STATUS:
    raise ValueError('Bad Status: %s Expected: 0xf0' % hex(status))
else:
    print 'Status OK!'

mfgr_code = unpack_sysex(sysex_buf.read(1))
if mfgr_code == 0x00:  # Indicates extended MFGR bytes
    # discard the first byte and read the next two (e.g. see MS above)
    mfgr_code = unpack_sysex(sysex_buf.read(2))

mfgr = MFGR_LOOKUPS[mfgr_code]
print 'SysEx for "%s" device.' % mfgr

family_id = unpack_sysex(sysex_buf.read(1))
if family_id == 0x3a:
    print 'MS2000 series Family Product'
else:
    print 'Unknown Family ID: %s' % hex(family_id)

member_id = unpack_sysex(sysex_buf.read(1))
if member_id == 0x58:
    print 'Unknown Member ID: %s (Micro-Korg?)' % hex(member_id)
else:
    print 'Unknown Member ID: %s' % hex(member_id)

if status == GOOD_STATUS:
    dump_type = DUMP_TYPES[unpack_sysex(sysex_buf.read(1))]
    print 'SysEx Msg Type: %s' % dump_type


for pgm in PGMS:
    print 'PGM: %s' % pgm
    locals()[pgm] = MicroKorgPGM(sysex_buf.read(254))


# print A18
# print B88
import StringIO

from microkorg_abstract import MicroKorgAbstractData
from microkorg_timbre_data import MicroKorgTimbreData
from microkorg_vocoder_data import MicroKorgVocoderData

class MicroKorgPGM(MicroKorgAbstractData):
    def __init__(self, data):
        self.data = StringIO.StringIO(data)

        print 'GENERAL'
        #bytes 0~11
        self.program_name = self.get_next_bytes(11)
        print 'Program name: %s' % self.program_name
        #bytes 12,13
        self.get_next_bytes(2)

        print 'ARPEGGIO'
        ##ARPEGGIO_TRIGGER
        #byte 14 !!!BITMAP
        self.arp_trigger_length = self.get_next_bytes()
        print 'ARP Trigger Length: %s' % hex(ord(self.arp_trigger_length))
        #byte 15
        self.arp_trigger_pattern = self.get_next_bytes()
        print 'ARP Trigger Pattern: %s' % hex(ord(self.arp_trigger_pattern))

        #byte 16 !!!BITMAP
        self.voice_mode = self.get_voice_mode()
        print 'Voice Mode: %s' % hex(self.voice_mode)
        #byte 17 !!!BITMAP
        self.scale_key, self.scale_type = self.get_scale_key_and_type()
        print 'Scale Key: %s' % hex(self.scale_key)
        print 'Scale Type: %s' % hex(self.scale_type)
        #byte 18
        self.get_next_bytes(1)

        print 'DELAY'
        ##DELAY FX
        #byte 19 !!!BITMAP
        self.delay_sync, self.delay_time_base = self\
            .get_delay_sync_and_time_base()
        print 'Delay Sync: %s' % hex(self.delay_sync)
        print 'Delay Time Base: %s' % hex(self.delay_time_base)
        #byte 20
        self.delay_time = self.get_next_bytes()
        print 'Delay Time: %s' % hex(ord(self.delay_time))
        #byte 21
        self.delay_depth = self.get_next_bytes()
        print 'Delay Depth: %s' % hex(ord(self.delay_depth))
        #byte 22
        self.delay_type = self.get_next_bytes()
        print 'Delay Type: %s' % hex(ord(self.delay_type))

        print 'MOD FX'
        ##MOD FX
        #byte 23
        self.mod_lfo_speed = self.get_next_bytes()
        print 'Mod LFO Speed: %s' % hex(ord(self.mod_lfo_speed))
        #byte 24
        self.mod_depth = self.get_next_bytes()
        print 'Mod Depth: %s' % hex(ord(self.mod_depth))
        #byte 25
        self.mod_type = self.get_next_bytes()
        print 'Mod Type: %s' % hex(ord(self.mod_type))

        print 'EQ'
        ##EQ
        #byte 26
        self.eq_hi_freq = self.get_next_bytes()
        print 'EQ Hi Freq: %s' % hex(ord(self.eq_hi_freq))
        #byte 27
        self.eq_hi_gain = self.get_next_bytes()
        print 'EQ Hi Gain: %s' % hex(ord(self.eq_hi_gain))
        #byte 28
        self.eq_low_freq = self.get_next_bytes()
        print 'EQ Low Freq: %s' % hex(ord(self.eq_low_freq))
        #byte 29
        self.eq_low_gain = self.get_next_bytes()
        print 'EQ Low Gain: %s' % hex(ord(self.eq_low_gain))

        print 'ARPEGGIO'
        ##ARPEGGIO
        #byte 30
        self.arp_tempo_msb = self.get_next_bytes()
        print 'ARP Tempo MSB: %s' % hex(ord(self.arp_tempo_msb))
        #byte 31
        self.arp_tempo_lsb = self.get_next_bytes()
        print 'ARP Tempo LSB: %s' % hex(ord(self.arp_tempo_lsb))
        #byte 32 !!!BITMAP
        self.arp_on_off, self.arp_latch, self.arp_target, self.arp_key_sync =\
            self.get_arp_bmp_32()
        print 'ARP On/Off: %s' % hex(self.arp_on_off)
        print 'ARP Latch: %s' % hex(self.arp_latch)
        print 'ARP Target: %s' % hex(self.arp_target)
        print 'ARP Key Sync: %s' % hex(self.arp_key_sync)
        #byte 33 !!!BITMAP
        self.arp_type, self.arp_range = self.get_arp_type_and_range()
        print 'ARP Type: %s' % hex(self.arp_type)
        print 'ARP Range: %s' % hex(self.arp_range)
        #byte 34
        self.arp_gate_time = self.get_next_bytes()
        print 'ARP Gate TIme: %s' % hex(ord(self.arp_gate_time))
        #byte 35
        self.arp_resolution = self.get_next_bytes()
        print 'ARP Resolution: %s' % hex(ord(self.arp_resolution))
        #byte 36
        self.arp_swing = self.get_next_bytes()
        print 'ARP Swing: %s' % hex(ord(self.arp_swing))

        print 'KBD OCTAVE'
        ##KBD OCTAVE
        #byte 37
        self.kbd_octave = self.get_next_bytes()
        print 'KBD Octave: %s' % hex(ord(self.kbd_octave))

        ###EITHER
        if self.voice_mode in [0x0, 0x2]:
            ##TIMBRE1 DATA
            #bytes 38-145
            print 'TIMBRE1'
            self.timbre1 = MicroKorgTimbreData(data=self.data.read(107))

            if self.voice_mode == 0x2: #i think??
                ##TIMBRE2 DATA
                #bytes 146-253
                print 'TIMBRE2'
                self.timbre2 = MicroKorgTimbreData(data=self.data.read(107))
        ###OR
        elif self.voice_mode == 0x5:
            ##VOCODER DATA
            #bytes 38-141
            print 'VOCODER'
            self.vocoder = MicroKorgVocoderData(data=self.data.read(103))
            #bytes 142-253 (dummy if vocoder)
            self.data.read(111)

    def get_scale_key_and_type(self):
        b = self._get_binary_data()
        scale_key = b[0:4]
        scale_type = b[4:]
        return int(scale_key, 2), int(scale_type, 2)

    def get_delay_sync_and_time_base(self):
        b = self._get_binary_data()
        delay_sync = b[0:4]
        delay_time_base = b[-1]
        return int(delay_sync, 2), int(delay_time_base, 2)

    def get_arp_bmp_32(self):
        b = self._get_binary_data()
        arp_on_off = b[7]
        latch = b[6]
        target = b[4:6]
        key_sync = b[0]
        return int(arp_on_off, 2), int(latch, 2), int(target, 2), \
               int(key_sync, 2)

    def get_arp_type_and_range(self):
        b = self._get_binary_data()
        arp_type = b[0:4]
        arp_range = b[4:]
        return int(arp_type, 2), int(arp_range, 2)

    def get_voice_mode(self):
        b = self._get_binary_data()
        bits = b[4:6][::-1] #[::-1] reverses the string for endianness
        # print bits
        return int(bits, 2)
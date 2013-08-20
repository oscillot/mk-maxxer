import StringIO

from microkorg_abstract import MicroKorgAbstractData
from microkorg_timbre_data import MicroKorgTimbreData
from microkorg_vocoder_data import MicroKorgVocoderData

from program import *

class MicroKorgPGM(MicroKorgAbstractData):
    def __init__(self, data):
        self.data = StringIO.StringIO(data)

        print 'GENERAL'
        #bytes 0~11
        self.program_name = self.read_bytes(12)
        print 'Program name: %s' % self.program_name
        #bytes 12,13 (dummy bytes)
        self.read_bytes(2)

        print 'ARPEGGIO TRIGGER CTRL'
        ##ARPEGGIO_TRIGGER
        #byte 14 !!!BITMAP
        self.arp_trigger_length = arpeggio.TriggerLength(self.get_next_bytes())
        print self.arp_trigger_length
        #byte 15
        self.arp_trigger_pattern = arpeggio.TriggerPattern(
            self.get_arp_trigger_pattern())
        print self.arp_trigger_pattern

        #byte 16 !!!BITMAP
        self.voice_mode = arpeggio.VoiceMode(self.get_voice_mode())
        print self.voice_mode
        #byte 17 !!!BITMAP
        scale_key, scale_type = self.get_scale_key_and_type()
        self.scale_key = arpeggio.ScaleKey(scale_key)
        self.scale_type = arpeggio.ScaleType(scale_type)
        print self.scale_key
        print self.scale_type
        #byte 18 (dummy)
        self.read_bytes(1)

        print 'DELAY FX'
        ##DELAY FX
        #byte 19 !!!BITMAP
        delay_sync, delay_time_base = self.get_delay_sync_and_time_base()
        self.delay_sync = delay_fx.Sync(delay_sync)
        self.delay_time_base = delay_fx.TimeBase(delay_time_base)
        print self.delay_sync
        print self.delay_time_base
        #byte 20
        self.delay_time = delay_fx.Time(self.get_next_bytes())
        print self.delay_time
        #byte 21
        self.delay_depth = delay_fx.Depth(self.get_next_bytes())
        print self.delay_depth
        #byte 22
        self.delay_type = delay_fx.Type(self.get_delay_type())
        print self.delay_type

        print 'MOD FX'
        ##MOD FX
        #byte 23
        self.mod_lfo_speed = mod_fx.LFOSpeed(self.get_next_bytes())
        print self.mod_lfo_speed
        #byte 24
        self.mod_depth = mod_fx.Depth(self.get_next_bytes())
        print self.mod_depth
        #byte 25
        self.mod_type = mod_fx.Type(self.get_mod_type())
        print self.mod_type

        print 'EQ'
        ##EQ
        #byte 26
        self.eq_hi_freq = eq.HiFreq(self.get_next_bytes())
        print self.eq_hi_freq
        #byte 27
        self.eq_hi_gain = eq.HiGain(self.get_next_bytes())
        print self.eq_hi_gain
        #byte 28
        self.eq_low_freq = eq.LoFreq(self.get_eq_low_freq())
        print self.eq_low_freq
        #byte 29
        self.eq_low_gain = eq.LoGain(self.get_next_bytes())
        print self.eq_low_gain

        print 'ARPEGGIO'
        ##ARPEGGIO
        #byte 30
        self.arp_tempo_msb = arpeggio.TempoMSB(self.get_next_bytes())
        print self.arp_tempo_msb
        #byte 31
        self.arp_tempo_lsb = arpeggio.TempoLSB(self.get_next_bytes())
        print self.arp_tempo_lsb
        #byte 32 !!!BITMAP
        arp_on_off, arp_latch, arp_target, arp_key_sync = self.get_arp_bmp_32()
        self.arp_on_off = arpeggio.OnOff(arp_on_off)
        self.arp_latch = arpeggio.Latch(arp_latch)
        self.arp_target = arpeggio.Target(arp_target)
        self.arp_key_sync = arpeggio.KeySync(arp_key_sync)
        print self.arp_on_off
        print self.arp_latch
        print self.arp_target
        print self.arp_key_sync
        #byte 33 !!!BITMAP
        arp_type, arp_range = self.get_arp_type_and_range()
        self.arp_type = arpeggio.Type(arp_type)
        self.arp_range = arpeggio.Range(arp_range)
        print self.arp_type
        print self.arp_range
        #byte 34
        self.arp_gate_time = arpeggio.GateTime(self.get_next_bytes())
        print self.arp_gate_time
        #byte 35
        self.arp_resolution = arpeggio.Resolution(self.get_next_bytes())
        print self.arp_resolution
        #byte 36
        self.arp_swing = arpeggio.Swing(self.get_next_bytes())
        print self.arp_swing

        print 'KBD OCTAVE'
        ##KBD OCTAVE
        #byte 37
        self.kbd_octave = kbd_octave.KeyboardOctave(self.get_next_bytes())
        print self.kbd_octave

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
        b = self.get_next_bytes()
        scale_key = BitArray(bin=b[0:4])
        scale_type = BitArray(bin=b[4:])
        return scale_key, scale_type

    def get_delay_sync_and_time_base(self):
        b = self.get_next_bytes()
        delay_sync = BitArray(bin=b[7])
        delay_time_base = BitArray(bin=b[0:3])
        return delay_sync, delay_time_base

    def get_eq_low_freq(self):
        b = self.get_next_bytes()
        eq_low_freq = BitArray(bin=b[0:6])
        return eq_low_freq

    def get_arp_bmp_32(self):
        b = self.get_next_bytes()
        arp_on_off = BitArray(bin=b[7])
        latch = BitArray(bin=b[6])
        target = BitArray(bin=b[4:6])  # this says 4&5?
        key_sync = BitArray(bin=b[0])
        return arp_on_off, latch, target, key_sync

    def get_arp_type_and_range(self):
        b = self.get_next_bytes()
        arp_type = BitArray(bin=b[0:4])
        arp_range = BitArray(bin=b[4:])
        return arp_type, arp_range

    def get_voice_mode(self):
        b = self.get_next_bytes()
        bits = BitArray(bin=b[4:6])
        return bits

    def get_arp_trigger_pattern(self):
        b = self.get_next_bytes()
        # return [int(t, 16) for t in b]
        arp_trigger_pattern = BitArray(bin=b)
        return arp_trigger_pattern

    def get_delay_type(self):
        b = self.get_next_bytes()
        delay_type = BitArray(bin=b[0:3])
        return delay_type

    def get_mod_type(self):
        b = self.get_next_bytes()
        mod_type = BitArray(bin=b[0:3])
        return mod_type
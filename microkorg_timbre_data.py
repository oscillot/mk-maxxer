from microkorg_abstract import MicroKorgAbstractData, SysExStream

from timbre import *


class MicroKorgTimbreData(MicroKorgAbstractData):
    def __init__(self, bitstream):
        self.program_bitstream = SysExStream(bitstream)

        print 'GENERAL'
        #byte offset 0
        self.midi_channel = timbre.MidiChannel(self.read_bytes())
        print self.midi_channel
        #byte offset 1 !!!BITMAP

    # def get_bmp1_values(self):
    #     b = self.read_bytes()
        key_priority = self.read_bits(2) #0,1
        # key_priority = BitArray(bin='0b000000%s' % key_data)
        self.read_bits() #2
        trigger_mode = self.read_bits() #3
        # trigger_mode = BitArray(bin='0b0000000%s' % trigger_data)
        eg1_reset = self.read_bits() #4
        # eg1_reset = BitArray(bin='0b0000000%s' % eg1_data)
        eg2_reset = self.read_bits() #5
        # eg2_reset = BitArray(bin='0b0000000%s' % eg2_data)
        assign_mode = self.read_bits(2) #6,7
        # assign_mode = BitArray(bin='0b000000%s' % assign_data)
        # return assign_mode, eg2_reset, eg1_reset, \
        #     trigger_mode, key_priority
        # assign_mode, eg2_reset, eg1_reset, trigger_mode, key_priority = \
        #     self.get_bmp1_values()
        self.assign_mode = timbre.AssignMode(assign_mode)
        self.eg2_reset = timbre.EG2Reset(eg2_reset)
        self.eg1_reset = timbre.EG1Reset(eg1_reset)
        self.trigger_mode = timbre.TriggerMode(trigger_mode)
        self.key_priority = timbre.KeyPriority(key_priority)
        print self.assign_mode
        print self.eg2_reset
        print self.eg1_reset
        print self.trigger_mode
        print self.key_priority
        #byte offset 2
        self.unison_detune = timbre.UnisonDetune(self.read_bytes())
        print self.unison_detune

        print 'PITCH'
        ##PITCH
        #byte offset 3
        self.pitch_tune = pitch.Tune(self.read_bytes())
        print self.pitch_tune
        #byte offset 4
        self.pitch_bend_range = pitch.BendRange(self.read_bytes())
        print self.pitch_bend_range
        #byte offset 5
        self.pitch_transpose = pitch.Transpose(self.read_bytes())
        print self.pitch_transpose
        #byte offset 6
        self.pitch_vibrato_int = pitch.VibratoInt(self.read_bytes())
        print self.pitch_vibrato_int

        print 'OSC1'
        ##OSC1
        #byte offset 7
        osc1_wave = self.get_osc1_wave()
        self.osc1_wave = osc1.Wave(osc1_wave)
        print self.osc1_wave
        #byte offset 8
        self.osc1_waveform_ctrl1 = osc1.WaveformCTRL1(self.read_bytes())
        print self.osc1_waveform_ctrl1
        #byte offset 9
        self.osc1_waveform_ctrl2 = osc1.WaveformCTRL2(self.read_bytes())
        print self.osc1_waveform_ctrl2
        #byte offset 10
        self.osc1_dwgs_wave = osc1.DWGSWave(self.get_dwgs_wave())
        print self.osc1_dwgs_wave
        #byte offset 11 (dummy)
        self.read_bytes(1)

        print 'OSC2'
        ##OSC2
        #byte offset 12 !!!BITMAP
        osc2_wave, osc2_mod_select = self.get_osc2_wave_and_mod()
        self.osc2_wave = osc2.Wave(osc2_wave)
        self.osc2_mod_select = osc2.ModSelect(osc2_mod_select)
        print self.osc2_wave
        print self.osc2_mod_select
        #byte offset 13
        self.osc2_semitone = osc2.Semitone(self.read_bytes())
        print self.osc2_semitone
        #byte offset 14
        self.osc2_tune = osc2.Tune(self.read_bytes())
        print self.osc2_tune

        print 'PITCH'
        ##PITCH
        #byte offset 15
        self.pitch_portamento_time = pitch.PortamentoTime(
            self.read_bytes())
        print self.pitch_portamento_time

        print 'MIXER'
        ##MIXER
        #byte offset 16
        self.osc1_level = mixer.OSC1Level(self.read_bytes())
        print self.osc1_level
        #byte offset 17
        self.osc2_level = mixer.OSC2Level(self.read_bytes())
        print self.osc2_level
        #byte offset 18
        self.noise_level = mixer.Noise(self.read_bytes())
        print self.noise_level

        print 'FILTER'
        ##FILTER
        #byte offset 19
        self.filter_type = filter.Type(self.get_filter_type())
        print self.filter_type
        #byte offset 20
        self.filter_cutoff = filter.Cutoff(self.read_bytes())
        print self.filter_cutoff
        #byte offset 21
        self.filter_resonance = filter.Resonance(self.read_bytes())
        print self.filter_resonance
        #byte offset 22
        self.filter_eg1_intensity = filter.EG1Intensity(self.read_bytes())
        print self.filter_eg1_intensity
        #byte offset 23
        self.filter_velocity_sense = filter.VelocitySense(
            self.read_bytes())
        print self.filter_velocity_sense
        #byte offset 24
        self.filter_keyboard_track = filter.KeyboardTrack(
            self.read_bytes())
        print self.filter_keyboard_track

        print 'AMP'
        ##AMP
        #byte offset 25
        self.amp_level = amp.Level(self.read_bytes())
        print self.amp_level
        #byte offset 26
        self.amp_panpot = amp.Panpot(self.read_bytes())
        print self.amp_panpot
        #byte offset 27 !!!BITMAP
        amp_sw, amp_distortion = self.get_amp_sw_and_distortion()
        self.amp_sw = amp.AmpSW(amp_sw)
        self.amp_distortion = amp.Distortion(amp_distortion)
        print self.amp_sw
        print self.amp_distortion
        #byte offset 28
        self.amp_velocity_sense = amp.VelocitySense(self.read_bytes())
        print self.amp_velocity_sense
        #byte offset 29
        self.amp_keyboard_track = amp.KeyboardTrack(self.read_bytes())
        print self.amp_keyboard_track

        print 'EG1'
        ##EG1
        #byte offset 30
        self.eg1_attack = eg1.Attack(self.read_bytes())
        print self.eg1_attack
        #byte offset 31
        self.eg1_decay = eg1.Decay(self.read_bytes())
        print self.eg1_decay
        #byte offset 32
        self.eg1_sustain = eg1.Sustain(self.read_bytes())
        print self.eg1_sustain
        #byte offset 33
        self.eg1_release = eg1.Release(self.read_bytes())
        print self.eg1_release

        print 'EG2'
        ##EG2
        #byte offset 34
        self.eg2_attack = eg2.Attack(self.read_bytes())
        print self.eg2_attack
        #byte offset 35
        self.eg2_decay = eg2.Decay(self.read_bytes())
        print self.eg2_decay
        #byte offset 36
        self.eg2_sustain = eg2.Sustain(self.read_bytes())
        print self.eg2_sustain
        #byte offset 37
        self.eg2_release = eg2.Release(self.read_bytes())
        print self.eg2_release

        print 'LFO1'
        ##LFO1
        #byte offset 38 !!!BITMAP
        lfo1_key_sync, lfo1_wave = self.get_lfo_key_sync_and_wave()
        self.lfo1_key_sync = lfo1.KeySync(lfo1_key_sync)
        self.lfo1_wave = lfo1.Wave(lfo1_wave)
        print self.lfo1_key_sync
        print self.lfo1_wave
        #byte offset 39
        self.lfo1_frequency = lfo1.Frequency(self.read_bytes())
        print self.lfo1_frequency
        #byte offset 40 !!!BITMAP
        lfo1_tempo_sync, lfo1_sync_note = self\
            .get_lfo_tempo_sync_and_sync_note()
        self.lfo1_tempo_sync = lfo1.TempoSync(lfo1_tempo_sync)
        self.lfo1_sync_note = lfo1.SyncNote(lfo1_sync_note)
        print self.lfo1_tempo_sync
        print self.lfo1_sync_note

        print 'LFO2'
        ##LFO2
        #byte offset 41 !!!BITMAP
        lfo2_key_sync, lfo2_wave = self.get_lfo_key_sync_and_wave()
        self.lfo2_key_sync = lfo2.KeySync(lfo2_key_sync)
        self.lfo2_wave = lfo2.Wave(lfo2_wave)
        print self.lfo2_key_sync
        print self.lfo2_wave
        #byte offset 42
        self.lfo2_frequency = lfo2.Frequency(self.read_bytes())
        print self.lfo2_frequency
        #byte offset 43 !!!BITMAP
        lfo2_tempo_sync, lfo2_sync_note = self\
            .get_lfo_tempo_sync_and_sync_note()
        self.lfo2_tempo_sync = lfo2.TempoSync(lfo2_tempo_sync)
        self.lfo2_sync_note = lfo2.SyncNote(lfo2_sync_note)
        print self.lfo2_tempo_sync
        print self.lfo2_sync_note

        ##PATCH
        print 'PATCH1'
        #byte offset 44
        patch1_destination, patch1_source = self\
            .get_patch_destination_and_source()
        self.patch1_destination = patch1.Destination(patch1_destination)
        self.patch1_source = patch1.Source(patch1_source)
        print self.patch1_destination
        print self.patch1_source
        #byte offset 45
        self.patch1_intensity = patch1.Intensity(self.read_bytes())
        print self.patch1_intensity
        print 'PATCH2'
        #byte offset 46
        patch2_destination, patch2_source = self\
            .get_patch_destination_and_source()
        self.patch2_destination = patch2.Destination(patch2_destination)
        self.patch2_source = patch2.Source(patch2_source)
        print self.patch2_destination
        print self.patch2_source
        #byte offset 47
        self.patch2_intensity = patch2.Intensity(self.read_bytes())
        print self.patch2_intensity
        print 'PATCH3'
        #byte offset 48
        patch3_destination, patch3_source = self\
            .get_patch_destination_and_source()
        self.patch3_destination = patch3.Destination(patch3_destination)
        self.patch3_source = patch3.Source(patch3_source)
        print self.patch3_destination
        print self.patch3_source
        #byte offset 49
        self.patch3_intensity = patch3.Intensity(self.read_bytes())
        print self.patch3_intensity
        print 'PATCH4'
        #byte offset 50
        patch4_destination, patch4_source = self\
            .get_patch_destination_and_source()
        self.patch4_destination = patch4.Destination(patch4_destination)
        self.patch4_source = patch4.Source(patch4_source)
        print self.patch4_destination
        print self.patch4_source
        #byte offset 51
        self.patch4_intensity = patch4.Intensity(self.read_bytes())
        print self.patch4_intensity
        #byte offset 52-107 (dummy)
        self.read_bytes(55)



    def get_osc1_wave(self):
        b = self.read_bytes()
        wave_data = b.bin[0:2]
        wave = BitArray(bin='0b000000%s' % wave_data)
        return wave

    def get_dwgs_wave(self):
        b = self.read_bytes()
        dwgs_data = b.bin[0:7]
        dwgs = BitArray(bin='0b0%s' % dwgs_data)
        return dwgs

    def get_osc2_wave_and_mod(self):
        b = self.read_bytes()
        wave_data = b.bin[0:2]
        wave = BitArray(bin='0b000000%s' % wave_data)
        mod_select_data = b.bin[4:6]
        mod_select = BitArray(bin='0b000000%s' % mod_select_data)
        return wave, mod_select

    def get_filter_type(self):
        b = self.read_bytes()
        type_data = b.bin[0:3]
        filter_type = BitArray(bin='0b00000%s' % type_data)
        return filter_type

    def get_amp_sw_and_distortion(self):
        b = self.read_bytes()
        sw_data = b.bin[6]
        sw = BitArray(bin='0b0000000%s' % sw_data)
        distortion_data = b.bin[0]
        distortion = BitArray(bin='0b0000000%s' % distortion_data)
        return sw, distortion

    def get_lfo_key_sync_and_wave(self):
        b = self.read_bytes()
        key_sync_data = b.bin[4:6]
        print key_sync_data
        key_sync = BitArray('0b000000%s' % key_sync_data)
        wave_data = b.bin[0:2]
        wave = BitArray(bin='0b000000%s' % wave_data)
        return key_sync, wave

    def get_lfo_tempo_sync_and_sync_note(self):
        b = self.read_bytes()
        tempo_sync_data = b.bin[7]
        tempo_sync = BitArray(bin='0b0000000%s' % tempo_sync_data)
        sync_note_data = b.bin[0:5]
        sync_note = BitArray(bin='0b000%s' % sync_note_data)
        return tempo_sync, sync_note

    def get_patch_destination_and_source(self):
        b = self.read_bytes()
        destination_data = b.bin[4:7]
        destination = BitArray(bin='0b00000%s' % destination_data)
        source_data = b.bin[0:3]
        source = BitArray(bin='0b00000%s' % source_data)
        return destination, source
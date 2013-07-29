import StringIO

from microkorg_abstract import MicroKorgAbstractData


class MicroKorgTimbreData(MicroKorgAbstractData):
    def __init__(self, data):
        self.data = StringIO.StringIO(data)

        print 'GENERAL'
        #byte offset 0
        self.midi_channel = self.get_next_bytes()
        print 'MIDI Channel: %s' % self.midi_channel
        #byte offset 1 !!!BITMAP
        self.assign_mode, self.eg2_reset, self.eg1_reset, self.trigger_mode, \
            self.key_priority = self.get_bmp1_values()
        print 'Assign Mode: %s' % self.assign_mode
        print 'EG2 Reset: %s' % self.eg2_reset
        print 'EG1 Reset: %s' % self.eg1_reset
        print 'Trigger Mode: %s' % self.trigger_mode
        #byte offset 2
        self.unison_detune = self.get_next_bytes()
        print 'Unison Detune: %s' % self.unison_detune

        print 'PITCH'
        ##PITCH
        #byte offset 3
        self.pitch_tune = self.get_next_bytes()
        print 'Pitch Tune: %s' % self.pitch_tune
        #byte offset 4
        self.pitch_bend_range = self.get_next_bytes()
        print 'Pitch Bend Range: %s' % self.pitch_bend_range
        #byte offset 5
        self.pitch_transpose = self.get_next_bytes()
        print 'Pitch Transpose: %s' % self.pitch_transpose
        #byte offset 6
        self.pitch_vibrato_int = self.get_next_bytes()
        print 'Pitch Vibrato Int: %s' % self.pitch_vibrato_int

        print 'OSC1'
        ##OSC1
        #byte offset 7
        self.osc1_wave = self.get_next_bytes()
        print 'OSC1 Wave: %s' % self.osc1_wave
        #byte offset 8
        self.osc1_waveform_ctrl1 = self.get_next_bytes()
        print 'OSC1 Waveform CTRL1: %s' % self.osc1_waveform_ctrl1
        #byte offset 9
        self.osc1_waveform_ctrl2 = self.get_next_bytes()
        print 'OSC1 Waveform CTRL2: %s' % self.osc1_waveform_ctrl2
        #byte offset 10
        self.osc1_dwgs_wave = self.get_next_bytes()
        print 'OSC1 DWGS Wave: %s' % self.osc1_dwgs_wave
        #byte offset 11 (dummy)
        self.get_next_bytes()

        print 'OSC2'
        ##OSC2
        #byte offset 12 !!!BITMAP
        self.osc2_wave, self.osc2_mod_select = self.get_osc2_wave_and_mod()
        print 'OSC2 Wave: %s' % self.osc2_wave
        print 'OSC2 Mod Select: %s' % self.osc2_mod_select
        #byte offset 13
        self.osc2_semitone = self.get_next_bytes()
        print 'OSC2 Semitone: %s' % self.osc2_semitone
        #byte offset 14
        self.osc2_tune = self.get_next_bytes()
        print 'OSC2 Tune: %s' % self.osc2_tune

        print 'PITCH'
        ##PITCH
        #byte offset 15
        self.pitch_portamento_time = self.get_next_bytes()
        print 'PITCH Portamento Time: %s' % self.pitch_portamento_time

        print 'MIXER'
        ##MIXER
        #byte offset 16
        self.osc1_level = self.get_next_bytes()
        print 'OSC1 Level: %s' % self.osc1_level
        #byte offset 17
        self.osc2_level = self.get_next_bytes()
        print 'OSC2 Level: %s' % self.osc2_level
        #byte offset 18
        self.noise_level = self.get_next_bytes()
        print 'Noise Level: %s' % self.noise_level

        print 'FILTER'
        ##FILTER
        #byte offset 19
        self.filter_type = self.get_next_bytes()
        print 'Filter Type: %s' % self.filter_type
        #byte offset 20
        self.filter_cutoff = self.get_next_bytes()
        print 'Filter Cutoff: %s' % self.filter_cutoff
        #byte offset 21
        self.filter_resonance = self.get_next_bytes()
        print 'Filter Resonance: %s' % self.filter_resonance
        #byte offset 22
        self.filter_eg1_intensity = self.get_next_bytes()
        print 'Filter EG1 Intensity: %s' % self.filter_eg1_intensity
        #byte offset 23
        self.filter_velocity_sense = self.get_next_bytes()
        print 'Filter Velocity Sense: %s' % self.filter_velocity_sense
        #byte offset 24
        self.filter_keyboard_track = self.get_next_bytes()
        print 'Filter Keyboard Track: %s' % self.filter_keyboard_track

        print 'AMP'
        ##AMP
        #byte offset 25
        self.amp_level = self.get_next_bytes()
        print 'AMP Level: %s' % self.amp_level
        #byte offset 26
        self.amp_panpot = self.get_next_bytes()
        print 'AMP Panpot: %s' % self.amp_panpot
        #byte offset 27 !!!BITMAP
        self.amp_sw, self.amp_distortion = self.get_amp_sw_and_distortion()
        print 'AMP SW: %s' % self.amp_sw
        print 'AMP Distortion: %s' % self.amp_distortion
        #byte offset 28
        self.amp_velocity_sense = self.get_next_bytes()
        print 'AMP Velocity Sense: %s' % self.amp_velocity_sense
        #byte offset 29
        self.amp_keyboard_track = self.get_next_bytes()
        print 'AMP Keyboard Track: %s' % self.amp_keyboard_track

        print 'EG1'
        ##EG1
        #byte offset 30
        self.eg1_attack = self.get_next_bytes()
        print 'EG1 Attack: %s' % self.eg1_attack
        #byte offset 31
        self.eg1_decay = self.get_next_bytes()
        print 'EG1 Decay: %s' % self.eg1_decay
        #byte offset 32
        self.eg1_sustain = self.get_next_bytes()
        print 'EG1 Sustain: %s' % self.eg1_sustain
        #byte offset 33
        self.eg1_release = self.get_next_bytes()
        print 'EG1 Release: %s' % self.eg1_release

        print 'EG2'
        ##EG2
        #byte offset 34
        self.eg2_attack = self.get_next_bytes()
        print 'EG2 Attack: %s' % self.eg2_attack
        #byte offset 35
        self.eg2_decay = self.get_next_bytes()
        print 'EG2 Decay: %s' % self.eg2_decay
        #byte offset 36
        self.eg2_sustain = self.get_next_bytes()
        print 'EG2 Sustain: %s' % self.eg2_sustain
        #byte offset 37
        self.eg2_release = self.get_next_bytes()
        print 'EG2 Release: %s' % self.eg2_release

        print 'LFO1'
        ##LFO1
        #byte offset 38 !!!BITMAP
        self.lfo1_key_sync, self.lfo1_wave = self.get_lfo_key_sync_and_wave()
        print 'LFO1 Key Sync: %s' % self.lfo1_key_sync
        print 'LFO1 Wave: %s' % self.lfo1_wave
        #byte offset 39
        self.lfo1_frequency = self.get_next_bytes()
        print 'LFO1 Frequency: %s' % self.lfo1_frequency
        #byte offset 40 !!!BITMAP
        self.lfo1_tempo_sync, self.lfo1_sync_note = self\
            .get_lfo_tempo_sync_and_sync_note()
        print 'LFO1 Tempo Sync: %s' % self.lfo1_tempo_sync
        print 'LFO1 Sync Note: %s' % self.lfo1_sync_note

        print 'LFO2'
        ##LFO2
        #byte offset 41 !!!BITMAP
        self.lfo2_key_sync, self.lfo2_wave = self.get_lfo_key_sync_and_wave()
        print 'LFO2 Key Sync: %s' % self.lfo2_key_sync
        print 'LFO2 Wave: %s' % self.lfo2_wave
        #byte offset 42
        self.lfo2_frequency = self.get_next_bytes()
        print 'LFO2 Frequency: %s' % self.lfo2_frequency
        #byte offset 43 !!!BITMAP
        self.lfo2_tempo_sync, self.lfo2_sync_note = self\
            .get_lfo_tempo_sync_and_sync_note()
        print 'LFO2 Tempo Sync: %s' % self.lfo2_tempo_sync
        print 'LFO2 Sync Note: %s' % self.lfo2_sync_note

        print 'PATCH'
        ##PATCH
        #byte offset 44
        self.patch1_destination, self.patch1_source = self\
            .get_patch_destination_and_source()
        print 'Patch1 Destination: %s' % self.patch1_destination
        print 'Patch1 Source: %s' % self.patch1_source
        #byte offset 45
        self.patch1_intensity = self.get_next_bytes()
        print 'Patch1 Intensity: %s' % self.patch1_intensity
        #byte offset 46
        self.patch2_destination, self.patch2_source = self\
            .get_patch_destination_and_source()
        print 'Patch2 Destination: %s' % self.patch2_destination
        print 'Patch2 Source: %s' % self.patch2_source
        #byte offset 47
        self.patch2_intensity = self.get_next_bytes()
        print 'Patch2 Intensity: %s' % self.patch2_intensity
        #byte offset 48
        self.patch3_destination, self.patch3_source = self\
            .get_patch_destination_and_source()
        print 'Patch3 Destination: %s' % self.patch3_destination
        print 'Patch3 Source: %s' % self.patch3_source
        #byte offset 49
        self.patch3_intensity = self.get_next_bytes()
        print 'Patch3 Intensity: %s' % self.patch3_intensity
        #byte offset 50
        self.patch4_destination, self.patch4_source = self\
            .get_patch_destination_and_source()
        print 'Patch4 Destination: %s' % self.patch4_destination
        print 'Patch4 Source: %s' % self.patch4_source
        #byte offset 51
        self.patch4_intensity = self.get_next_bytes()
        print 'Patch4 Intensity: %s' % self.patch4_intensity
        #byte offset 52-107 (dummy)
        self.read_bytes(55)

    def get_bmp1_values(self):
        b = self._get_binary_data()
        key_priority = hex(int(b[0:2], 16))
        trigger_mode = hex(int(b[3], 16))
        eg1_reset = hex(int(b[4], 16))
        eg2_reset = hex(int(b[5], 16))
        assign_mode = hex(int(b[6:], 16))
        return assign_mode, eg2_reset, eg1_reset, \
            trigger_mode, key_priority

    def get_osc2_wave_and_mod(self):
        b = self._get_binary_data()
        wave = hex(int(b[0:2], 16))
        mod_select = hex(int(b[4:6], 16))
        return wave, mod_select

    def get_amp_sw_and_distortion(self):
        b = self._get_binary_data()
        sw = hex(int(b[6], 16))
        distortion = hex(int(b[0], 16))
        return sw, distortion

    def get_lfo_key_sync_and_wave(self):
        b = self._get_binary_data()
        key_sync = hex(int(b[4:6], 16))
        wave = hex(int(b[0:2], 16))
        return key_sync, wave

    def get_lfo_tempo_sync_and_sync_note(self):
        b = self._get_binary_data()
        tempo_sync = hex(int(b[7], 16))
        sync_note = hex(int(b[0:5], 16))
        return tempo_sync, sync_note

    def get_patch_destination_and_source(self):
        b = self._get_binary_data()
        destination = hex(int(b[4:], 16))
        source = hex(int(b[0:4], 16))
        return destination, source
import StringIO

from microkorg_abstract import MicroKorgAbstractData


class MicroKorgTimbreData(MicroKorgAbstractData):
    def __init__(self, data):
        self.data = StringIO.StringIO(data)

        print 'GENERAL'
        #byte offset 0
        self.midi_channel = self.get_next_bytes()
        print 'MIDI Channel: %s' % hex(ord(self.midi_channel))
        #byte offset 1 !!!BITMAP
        self.assign_mode, self.eg2_reset, self.eg1_reset, self.trigger_mode, \
            self.key_priority = self.get_bmp1_values()
        print 'Assign Mode: %s' % hex(self.assign_mode)
        print 'EG2 Reset: %s' % hex(self.eg2_reset)
        print 'EG1 Reset: %s' % hex(self.eg1_reset)
        print 'Trigger Mode: %s' % hex(self.trigger_mode)
        #byte offset 2
        self.unison_detune = self.get_next_bytes()
        print 'Unison Detune: %s' % hex(ord(self.unison_detune))

        print 'PITCH'
        ##PITCH
        #byte offset 3
        self.pitch_tune = self.get_next_bytes()
        print 'Pitch Tune: %s' % hex(ord(self.pitch_tune))
        #byte offset 4
        self.pitch_bend_range = self.get_next_bytes()
        print 'Pitch Bend Range: %s' % hex(ord(self.pitch_bend_range))
        #byte offset 5
        self.pitch_transpose = self.get_next_bytes()
        print 'Pitch Transpose: %s' % hex(ord(self.pitch_transpose))
        #byte offset 6
        self.pitch_vibrato_int = self.get_next_bytes()
        print 'Pitch Vibrato Int: %s' % hex(ord(self.pitch_vibrato_int))

        print 'OSC1'
        ##OSC1
        #byte offset 7
        self.osc1_wave = self.get_next_bytes()
        print 'OSC1 Wave: %s' % hex(ord(self.osc1_wave))
        #byte offset 8
        self.osc1_waveform_ctrl1 = self.get_next_bytes()
        print 'OSC1 Waveform CTRL1: %s' % hex(ord(self.osc1_waveform_ctrl1))
        #byte offset 9
        self.osc1_waveform_ctrl2 = self.get_next_bytes()
        print 'OSC1 Waveform CTRL2: %s' % hex(ord(self.osc1_waveform_ctrl2))
        #byte offset 10
        self.osc1_dwgs_wave = self.get_next_bytes()
        print 'OSC1 DWGS Wave: %s' % hex(ord(self.osc1_dwgs_wave))
        #byte offset 11 (dummy)
        self.get_next_bytes()

        print 'OSC2'
        ##OSC2
        #byte offset 12 !!!BITMAP
        self.osc2_wave, self.osc2_mod_select = self.get_osc2_wave_and_mod()
        print 'OSC2 Wave: %s' % hex(self.osc2_wave)
        print 'OSC2 Mod Select: %s' % hex(self.osc2_mod_select)
        #byte offset 13
        self.osc2_semitone = self.get_next_bytes()
        print 'OSC2 Semitone: %s' % hex(ord(self.osc2_semitone))
        #byte offset 14
        self.osc2_tune = self.get_next_bytes()
        print 'OSC2 Tune: %s' % hex(ord(self.osc2_tune))

        print 'PITCH'
        ##PITCH
        #byte offset 15
        self.pitch_portamento_time = self.get_next_bytes()
        print 'PITCH Portamento Time: %s' % hex(ord(self.pitch_portamento_time))

        print 'MIXER'
        ##MIXER
        #byte offset 16
        self.osc1_level = self.get_next_bytes()
        print 'OSC1 Level: %s' % hex(ord(self.osc1_level))
        #byte offset 17
        self.osc2_level = self.get_next_bytes()
        print 'OSC2 Level: %s' % hex(ord(self.osc2_level))
        #byte offset 18
        self.noise_level = self.get_next_bytes()
        print 'Noise Level: %s' % hex(ord(self.noise_level))

        print 'FILTER'
        ##FILTER
        #byte offset 19
        self.filter_type = self.get_next_bytes()
        print 'Filter Type: %s' % hex(ord(self.filter_type))
        #byte offset 20
        self.filter_cutoff = self.get_next_bytes()
        print 'Filter Cutoff: %s' % hex(ord(self.filter_cutoff))
        #byte offset 21
        self.filter_resonance = self.get_next_bytes()
        print 'Filter Resonance: %s' % hex(ord(self.filter_resonance))
        #byte offset 22
        self.filter_eg1_intensity = self.get_next_bytes()
        print 'Filter EG1 Intensity: %s' % hex(ord(self.filter_eg1_intensity))
        #byte offset 23
        self.filter_velocity_sense = self.get_next_bytes()
        print 'Filter Velocity Sense: %s' % hex(ord(self.filter_velocity_sense))
        #byte offset 24
        self.filter_keyboard_track = self.get_next_bytes()
        print 'Filter Keyboard Track: %s' % hex(ord(self.filter_keyboard_track))

        print 'AMP'
        ##AMP
        #byte offset 25
        self.amp_level = self.get_next_bytes()
        print 'AMP Level: %s' % hex(ord(self.amp_level))
        #byte offset 26
        self.amp_panpot = self.get_next_bytes()
        print 'AMP Panpot: %s' % hex(ord(self.amp_panpot))
        #byte offset 27 !!!BITMAP
        self.amp_sw, self.amp_distortion = self.get_amp_sw_and_distortion()
        print 'AMP SW: %s' % hex(self.amp_sw)
        print 'AMP Distortion: %s' % hex(self.amp_distortion)
        #byte offset 28
        self.amp_velocity_sense = self.get_next_bytes()
        print 'AMP Velocity Sense: %s' % hex(ord(self.amp_velocity_sense))
        #byte offset 29
        self.amp_keyboard_track = self.get_next_bytes()
        print 'AMP Keyboard Track: %s' % hex(ord(self.amp_keyboard_track))

        print 'EG1'
        ##EG1
        #byte offset 30
        self.eg1_attack = self.get_next_bytes()
        print 'EG1 Attack: %s' % hex(ord(self.eg1_attack))
        #byte offset 31
        self.eg1_decay = self.get_next_bytes()
        print 'EG1 Decay: %s' % hex(ord(self.eg1_decay))
        #byte offset 32
        self.eg1_sustain = self.get_next_bytes()
        print 'EG1 Sustain: %s' % hex(ord(self.eg1_sustain))
        #byte offset 33
        self.eg1_release = self.get_next_bytes()
        print 'EG1 Release: %s' % hex(ord(self.eg1_release))

        print 'EG2'
        ##EG2
        #byte offset 34
        self.eg2_attack = self.get_next_bytes()
        print 'EG2 Attack: %s' % hex(ord(self.eg2_attack))
        #byte offset 35
        self.eg2_decay = self.get_next_bytes()
        print 'EG2 Decay: %s' % hex(ord(self.eg2_decay))
        #byte offset 36
        self.eg2_sustain = self.get_next_bytes()
        print 'EG2 Sustain: %s' % hex(ord(self.eg2_sustain))
        #byte offset 37
        self.eg2_release = self.get_next_bytes()
        print 'EG2 Release: %s' % hex(ord(self.eg2_release))

        print 'LFO1'
        ##LFO1
        #byte offset 38 !!!BITMAP
        self.lfo1_key_sync, self.lfo1_wave = self.get_lfo_key_sync_and_wave()
        print 'LFO1 Key Sync: %s' % hex(self.lfo1_key_sync)
        print 'LFO1 Wave: %s' % hex(self.lfo1_wave)
        #byte offset 39
        self.lfo1_frequency = self.get_next_bytes()
        print 'LFO1 Frequency: %s' % hex(ord(self.lfo1_frequency))
        #byte offset 40 !!!BITMAP
        self.lfo1_tempo_sync, self.lfo1_sync_note = self\
            .get_lfo_tempo_sync_and_sync_note()
        print 'LFO1 Tempo Sync: %s' % hex(self.lfo1_tempo_sync)
        print 'LFO1 Sync Note: %s' % hex(self.lfo1_sync_note)

        print 'LFO2'
        ##LFO2
        #byte offset 41 !!!BITMAP
        self.lfo2_key_sync, self.lfo2_wave = self.get_lfo_key_sync_and_wave()
        print 'LFO2 Key Sync: %s' % hex(self.lfo2_key_sync)
        print 'LFO2 Wave: %s' % hex(self.lfo2_wave)
        #byte offset 42
        self.lfo2_frequency = self.get_next_bytes()
        print 'LFO2 Frequency: %s' % hex(ord(self.lfo2_frequency))
        #byte offset 43 !!!BITMAP
        self.lfo2_tempo_sync, self.lfo2_sync_note = self\
            .get_lfo_tempo_sync_and_sync_note()
        print 'LFO2 Tempo Sync: %s' % hex(self.lfo2_tempo_sync)
        print 'LFO2 Sync Note: %s' % hex(self.lfo2_sync_note)

        print 'PATCH'
        ##PATCH
        #byte offset 44
        self.patch1_destination, self.patch1_source = self\
            .get_patch_destination_and_source()
        print 'Patch1 Destination: %s' % hex(self.patch1_destination)
        print 'Patch1 Source: %s' % hex(self.patch1_source)
        #byte offset 45
        self.patch1_intensity = self.get_next_bytes()
        print 'Patch1 Intensity: %s' % hex(ord(self.patch1_intensity))
        #byte offset 46
        self.patch2_destination, self.patch2_source = self\
            .get_patch_destination_and_source()
        print 'Patch2 Destination: %s' % hex(self.patch2_destination)
        print 'Patch2 Source: %s' % hex(self.patch2_source)
        #byte offset 47
        self.patch2_intensity = self.get_next_bytes()
        print 'Patch2 Intensity: %s' % hex(ord(self.patch2_intensity))
        #byte offset 48
        self.patch3_destination, self.patch3_source = self\
            .get_patch_destination_and_source()
        print 'Patch3 Destination: %s' % hex(self.patch3_destination)
        print 'Patch3 Source: %s' % hex(self.patch3_source)
        #byte offset 49
        self.patch3_intensity = self.get_next_bytes()
        print 'Patch3 Intensity: %s' % hex(ord(self.patch3_intensity))
        #byte offset 50
        self.patch4_destination, self.patch4_source = self\
            .get_patch_destination_and_source()
        print 'Patch4 Destination: %s' % hex(self.patch4_destination)
        print 'Patch4 Source: %s' % hex(self.patch4_source)
        #byte offset 51
        self.patch4_intensity = self.get_next_bytes()
        print 'Patch4 Intensity: %s' % hex(ord(self.patch4_intensity))
        #byte offset 52-107 (dummy
        self.get_next_bytes(55)

    def get_bmp1_values(self):
        b = self._get_binary_data()
        key_priority = b[0:2]
        trigger_mode = b[3]
        eg1_reset = b[4]
        eg2_reset = b[5]
        assign_mode = b[6:]
        return int(assign_mode, 2), int(eg2_reset, 2), int(eg1_reset, 2), \
            int(trigger_mode, 2), int(key_priority, 2)

    def get_osc2_wave_and_mod(self):
        b = self._get_binary_data()
        wave = b[0:2]
        mod_select = b[4:6]
        return int(wave, 2), int(mod_select, 2)

    def get_amp_sw_and_distortion(self):
        b = self._get_binary_data()
        sw = b[6]
        distortion = b[0]
        return int(sw, 2), int(distortion, 2)

    def get_lfo_key_sync_and_wave(self):
        b = self._get_binary_data()
        key_sync = b[4:6]
        wave = b[0:2]
        return int(key_sync, 2), int(wave, 2)

    def get_lfo_tempo_sync_and_sync_note(self):
        b = self._get_binary_data()
        tempo_sync = b[7]
        sync_note = b[0:5]
        return int(tempo_sync, 2), int(sync_note, 2)

    def get_patch_destination_and_source(self):
        b = self._get_binary_data()
        destination = b[4:]
        source = b[0:4]
        return int(destination, 2), int(source, 2)
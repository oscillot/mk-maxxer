from bitstring import BitStream
from vocoder import *
from microkorg_timbre_data import MicroKorgTimbreData


class MicroKorgVocoderData(MicroKorgTimbreData):
    def __init__(self, bitstream):
        self.program_bitstream = BitStream(bitstream)

        print 'GENERAL'
        #byte offset 0
        self.midi_channel = vocoder.MidiChannel(self.read_bytes())
        print 'MIDI Channel: %s' % self.midi_channel
        #byte offset 1 !!!BITMAP
        assign_mode, eg2_reset, eg1_reset, trigger_mode, \
            key_priority = self.get_bmp1_values()
        self.assign_mode = vocoder.AssignMode(assign_mode)
        self.eg2_reset = vocoder.EG2Reset(eg2_reset)
        self.eg1_reset = vocoder.EG1Reset(eg1_reset)
        self.trigger_mode = vocoder.TriggerMode(trigger_mode)
        self.key_priority = vocoder.KeyPriority(key_priority)
        print self.assign_mode
        print self.eg1_reset
        print self.eg2_reset
        print self.trigger_mode
        print self.key_priority
        #byte offset 2
        self.unison_detune = vocoder.UnisonDetune(self.read_bytes())
        print self.unison_detune

        print 'PITCH'
        ## PITCH
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

        print 'OSC'
        ## OSC
        #byte offset 7
        self.osc_wave = osc.Wave(self.read_bytes())
        print self.osc_wave
        #byte offset 8
        self.osc_waveform_ctrl1 = osc.WaveformCTRL1(self.read_bytes())
        print self.osc_waveform_ctrl1
        #byte offset 9
        self.osc_waveform_ctrl2 = osc.WaveformCTRL2(self.read_bytes())
        print self.osc_waveform_ctrl2
        #byte offset 10
        self.osc_dwgs_wave = osc.DWGSWave(self.read_bytes())
        print self.osc_dwgs_wave
        #byte offset 11 (dummy)
        self.read_bytes()


        print 'AUDIO IN1'
        ## AUDIO IN1
        #byte offset 12
        self.audio_in1_hpf_gate = audio_in.HPFGate(self.read_bytes())
        print self.audio_in1_hpf_gate
        #byte offset 13 (dummy)
        self.read_bytes()


        print 'PITCH continued?'
        ## PITCH (2)
        #byte offset 14
        self.pitch_portamento_time = pitch.PortamentoTime(self
                                                            .read_bytes())
        print self.pitch_portamento_time

        print 'MIXER'
        ## MIXER
        #byte offset 15
        self.mixer_osc1_level = mixer.OSC1Level(self.read_bytes())
        print self.mixer_osc1_level
        #byte offset 16
        self.mixer_ext1_level = mixer.EXT1Level(self.read_bytes())
        print self.mixer_ext1_level
        #byte offset 17
        self.mixer_noise_level = mixer.Noise(self.read_bytes())
        print self.mixer_noise_level


        print 'AUDIO IN1 continued?'
        ##AUDIO IN1 (2)
        #byte offset 18
        self.audio_in1_hpf_level = mixer.HPFLevel(self.read_bytes())
        print self.audio_in1_hpf_level
        #byte offset 19
        self.audio_in1_gate_sense = mixer.GateSense(self.read_bytes())
        print self.audio_in1_gate_sense
        #byte offset 20
        self.audio_in1_threshold = mixer.Threshold(self.read_bytes())
        print self.audio_in1_threshold


        print 'FILTER'
        ##FILTER
        #byte offset 21
        self.filter_shift = filter.Shift(self.read_bytes())
        print self.filter_shift
        #byte offset 22
        self.filter_cutoff = filter.Cutoff(self.read_bytes())
        print self.filter_cutoff
        #byte offset 23
        self.filter_resonance = filter.Resonance(self.read_bytes())
        print self.filter_resonance
        #byte offset 24
        self.filter_mod_source = filter.ModSource(self.read_bytes())
        print self.filter_mod_source
        #byte offset 25
        self.filter_intensity = filter.Intensity(self.read_bytes())
        print self.filter_intensity
        #byte offset 26
        self.filter_e_f_sense = filter.EFSense(self.read_bytes())
        print self.filter_e_f_sense


        print 'AMP'
        ##AMP
        #byte offset 27
        self.amp_level = amp.Level(self.read_bytes())
        print self.amp_level
        #byte offset 28
        self.amp_direct_level = amp.DirectLevel(self.read_bytes())
        print self.amp_direct_level
        #byte offset 29
        self.amp_distortion_on_off = amp.Distortion(self.read_bytes())
        print self.amp_distortion_on_off
        #byte offset 30
        self.amp_velocity_sense = amp.VelocitySense(self.read_bytes())
        print self.amp_velocity_sense
        #byte offset 31
        self.amp_keytrack = amp.KeyboardTrack(self.read_bytes())
        print self.amp_keytrack


        print 'EG1'
        ##EG1
        #byte offset 32
        self.eg1_attack = eg1.Attack(self.read_bytes())
        print self.eg1_attack
        #byte offset 33
        self.eg1_decay = eg1.Decay(self.read_bytes())
        print self.eg1_decay
        #byte offset 34
        self.eg1_sustain = eg1.Sustain(self.read_bytes())
        print self.eg1_sustain
        #byte offset 35
        self.eg1_release = eg1.Release(self.read_bytes())
        print self.eg1_release

        ##EG2
        #byte offset 36
        self.eg2_attack = eg2.Attack(self.read_bytes())
        print self.eg2_attack
        #byte offset 37
        self.eg2_decay = eg2.Decay(self.read_bytes())
        print self.eg2_decay
        #byte offset 38
        self.eg2_sustain = eg2.Sustain(self.read_bytes())
        print self.eg2_sustain
        #byte offset 39
        self.eg2_release = eg2.Release(self.read_bytes())
        print self.eg2_release


        print 'LFO1'
        ##LFO1
        #byte offset 40 !!!BITMAP
        lfo1_key_sync, lfo1_wave = self.get_lfo_key_sync_lfo_wave()
        self.lfo1_key_sync = lfo1.KeySync(lfo1_key_sync)
        self.lfo1_wave = lfo1.Wave(lfo1_wave)
        print self.lfo1_key_sync
        print self.lfo1_wave
        #byte offset 41
        self.lfo1_frequency = lfo1.Frequency(self.read_bytes())
        print self.lfo1_frequency
        #byte offset 42 !!!BITMAP
        lfo1_tempo_sync, lfo1_sync_note = \
            self.get_lfo_tempo_sync_lfo_sync_note()
        self.lfo1_tempo_sync = lfo1.TempoSync(lfo1_tempo_sync)
        self.lfo1_sync_note = lfo1.SyncNote(lfo1_sync_note)
        print self.lfo1_tempo_sync
        print self.lfo1_sync_note

        ##LFO2
        #byte offset 43 !!!BITMAP
        lfo2_key_sync, lfo2_wave = self.get_lfo_key_sync_lfo_wave()
        self.lfo2_key_sync = lfo2.KeySync(lfo2_key_sync)
        self.lfo2_wave = lfo2.Wave(lfo2_wave)
        print self.lfo2_key_sync
        print self.lfo2_wave
        #byte offset 44
        self.lfo2_frequency = lfo2.Frequency(self.read_bytes())
        print self.lfo2_frequency
        #byte offset 45 !!!BITMAP
        lfo2_tempo_sync, lfo2_sync_note = self\
            .get_lfo_tempo_sync_lfo_sync_note()
        self.lfo2_tempo_sync = lfo2.TempoSync(lfo2_tempo_sync)
        self.lfo2_sync_note = lfo2.SyncNote(lfo2_sync_note)
        print self.lfo2_tempo_sync
        print self.lfo2_sync_note

        ##LEVELS
        #byte offset 46
        self.level_1 = self.read_bytes()
        print 'Level 1: %s' % self.level_1
        #byte offset 47
        self.level_2 = self.read_bytes()
        print 'Level 2: %s' % self.level_2
        #byte offset 48
        self.level_3 = self.read_bytes()
        print 'Level 3: %s' % self.level_3
        #byte offset 49
        self.level_4 = self.read_bytes()
        print 'Level 4: %s' % self.level_4
        #byte offset 50
        self.level_5 = self.read_bytes()
        print 'Level 5: %s' % self.level_5
        #byte offset 51
        self.level_6 = self.read_bytes()
        print 'Level 6: %s' % self.level_6
        #byte offset 52
        self.level_7 = self.read_bytes()
        print 'Level 7: %s' % self.level_7
        #byte offset 53
        self.level_8 = self.read_bytes()
        print 'Level 8: %s' % self.level_8
        #byte offset 54
        self.level_9 = self.read_bytes()
        print 'Level 9: %s' % self.level_9
        #byte offset 55
        self.level_10 = self.read_bytes()
        print 'Level 10: %s' % self.level_10
        #byte offset 56
        self.level_11 = self.read_bytes()
        print 'Level 11: %s' % self.level_11
        #byte offset 57
        self.level_12 = self.read_bytes()
        print 'Level 12: %s' % self.level_12
        #byte offset 58
        self.level_13 = self.read_bytes()
        print 'Level 13: %s' % self.level_13
        #byte offset 59
        self.level_14 = self.read_bytes()
        print 'Level 14: %s' % self.level_14
        #byte offset 60
        self.level_15 = self.read_bytes()
        print 'Level 15: %s' % self.level_15
        #byte offset 61
        self.level_16 = self.read_bytes()
        print 'Level 16: %s' % self.level_16


        print 'PAN'
        ##PAN
        #byte offset 62
        self.pan_1 = self.read_bytes()
        print 'PAN 1: %s' % self.pan_1
        #byte offset 63
        self.pan_2 = self.read_bytes()
        print 'PAN 2: %s' % self.pan_2
        #byte offset 64
        self.pan_3 = self.read_bytes()
        print 'PAN 3: %s' % self.pan_3
        #byte offset 65
        self.pan_4 = self.read_bytes()
        print 'PAN 4: %s' % self.pan_4
        #byte offset 66
        self.pan_5 = self.read_bytes()
        print 'PAN 5: %s' % self.pan_5
        #byte offset 67
        self.pan_6 = self.read_bytes()
        print 'PAN 6: %s' % self.pan_6
        #byte offset 68
        self.pan_7 = self.read_bytes()
        print 'PAN 7: %s' % self.pan_7
        #byte offset 69
        self.pan_8 = self.read_bytes()
        print 'PAN 8: %s' % self.pan_8
        #byte offset 70
        self.pan_9 = self.read_bytes()
        print 'PAN 9: %s' % self.pan_9
        #byte offset 71
        self.pan_10 = self.read_bytes()
        print 'PAN 10: %s' % self.pan_10
        #byte offset 72
        self.pan_11 = self.read_bytes()
        print 'PAN 11: %s' % self.pan_11
        #byte offset 73
        self.pan_12 = self.read_bytes()
        print 'PAN 12: %s' % self.pan_12
        #byte offset 74
        self.pan_13 = self.read_bytes()
        print 'PAN 13: %s' % self.pan_13
        #byte offset 75
        self.pan_14 = self.read_bytes()
        print 'PAN 14: %s' % self.pan_14
        #byte offset 76
        self.pan_15 = self.read_bytes()
        print 'PAN 15: %s' % self.pan_15
        #byte offset 77
        self.pan_16 = self.read_bytes()
        print 'PAN 16: %s' % self.pan_16


        print 'EF HOLD LEVEL'
        ##EF HOLD LEVEL
        #byte offset 78
        self.ef_hold_level_high_1 = self.read_bytes()
        print 'EF Hold Level High 1: %s' % self.ef_hold_level_high_1
        #byte offset 79
        self.ef_hold_level_mid_high_1 = self.read_bytes()
        print 'EF Hold Level Mid-High 1: %s' % self.ef_hold_level_mid_high_1
        #byte offset 80
        self.ef_hold_level_mid_low_1 = self.read_bytes()
        print 'EF Hold Level Mid-Low 1: %s' % self.ef_hold_level_mid_low_1
        #byte offset 81
        self.ef_hold_level_low_1 = self.read_bytes()
        print 'EF Hold Level Low 1: %s' % self.ef_hold_level_low_1
        #byte offset 82
        self.ef_hold_level_high_2 = self.read_bytes()
        print 'EF Hold Level High 2: %s' % self.ef_hold_level_high_2
        #byte offset 83
        self.ef_hold_level_mid_high_2 = self.read_bytes()
        print 'EF Hold Level Mid-High 2: %s' % self.ef_hold_level_mid_high_2
        #byte offset 84
        self.ef_hold_level_mid_low_2 = self.read_bytes()
        print 'EF Hold Level Mid-Low 2: %s' % self.ef_hold_level_mid_low_2
        #byte offset 85
        self.ef_hold_level_low_2 = self.read_bytes()
        print 'EF Hold Level Low 2: %s' % self.ef_hold_level_low_2
        #byte offset 86
        self.ef_hold_level_high_3 = self.read_bytes()
        print 'EF Hold Level High 3: %s' % self.ef_hold_level_high_3
        #byte offset 87
        self.ef_hold_level_mid_high_3 = self.read_bytes()
        print 'EF Hold Level Mid-High 3: %s' % self.ef_hold_level_mid_high_3
        #byte offset 88
        self.ef_hold_level_mid_low_3 = self.read_bytes()
        print 'EF Hold Level Mid-Low 3: %s' % self.ef_hold_level_mid_low_3
        #byte offset 89
        self.ef_hold_level_low_3 = self.read_bytes()
        print 'EF Hold Level Low 3: %s' % self.ef_hold_level_low_3
        #byte offset 90
        self.ef_hold_level_high_4 = self.read_bytes()
        print 'EF Hold Level High 4: %s' % self.ef_hold_level_high_4
        #byte offset 91
        self.ef_hold_level_mid_high_4 = self.read_bytes()
        print 'EF Hold Level Mid-High 4: %s' % self.ef_hold_level_mid_high_4
        #byte offset 92
        self.ef_hold_level_mid_low_4 = self.read_bytes()
        print 'EF Hold Level Mid-Low 4: %s' % self.ef_hold_level_mid_low_4
        #byte offset 93
        self.ef_hold_level_low_4 = self.read_bytes()
        print 'EF Hold Level Low 4: %s' % self.ef_hold_level_low_4
        #byte offset 94
        self.ef_hold_level_high_5 = self.read_bytes()
        print 'EF Hold Level High 5: %s' % self.ef_hold_level_high_5
        #byte offset 95
        self.ef_hold_level_mid_high_5 = self.read_bytes()
        print 'EF Hold Level Mid-High 5: %s' % self.ef_hold_level_mid_high_5
        #byte offset 96
        self.ef_hold_level_mid_low_5 = self.read_bytes()
        print 'EF Hold Level Mid-Low 5: %s' % self.ef_hold_level_mid_low_5
        #byte offset 97
        self.ef_hold_level_low_5 = self.read_bytes()
        print 'EF Hold Level Low 5: %s' % self.ef_hold_level_low_5
        #byte offset 98
        self.ef_hold_level_high_6 = self.read_bytes()
        print 'EF Hold Level High 6: %s' % self.ef_hold_level_high_6
        #byte offset 99
        self.ef_hold_level_mid_high_6 = self.read_bytes()
        print 'EF Hold Level Mid-High 6: %s' % self.ef_hold_level_mid_high_6
        #byte offset 100
        self.ef_hold_level_mid_low_6 = self.read_bytes()
        print 'EF Hold Level Mid-Low 6: %s' % self.ef_hold_level_mid_low_6
        #byte offset 101
        self.ef_hold_level_low_6 = self.read_bytes()
        print 'EF Hold Level Low 6: %s' % self.ef_hold_level_low_6
        #byte offset 102
        self.ef_hold_level_high_7 = self.read_bytes()
        print 'EF Hold Level High 7: %s' % self.ef_hold_level_high_7
        #byte offset 103
        self.ef_hold_level_mid_high_7 = self.read_bytes()
        print 'EF Hold Level Mid-High 7: %s' % self.ef_hold_level_mid_high_7
        #byte offset 104
        self.ef_hold_level_mid_low_7 = self.read_bytes()
        print 'EF Hold Level Mid-Low 7: %s' % self.ef_hold_level_mid_low_7
        #byte offset 105
        self.ef_hold_level_low_7 = self.read_bytes()
        print 'EF Hold Level Low 7: %s' % self.ef_hold_level_low_7
        #byte offset 106
        self.ef_hold_level_high_8 = self.read_bytes()
        print 'EF Hold Level High 8: %s' % self.ef_hold_level_high_8
        #byte offset 107
        self.ef_hold_level_mid_high_8 = self.read_bytes()
        print 'EF Hold Level Mid-High 8: %s' % self.ef_hold_level_mid_high_8
        #byte offset 108
        self.ef_hold_level_mid_low_8 = self.read_bytes()
        print 'EF Hold Level Mid-Low 8: %s' % self.ef_hold_level_mid_low_8
        #byte offset 109
        self.ef_hold_level_low_8 = self.read_bytes()
        print 'EF Hold Level Low 8: %s' % self.ef_hold_level_low_8
        #byte offset 110
        self.ef_hold_level_high_9 = self.read_bytes()
        print 'EF Hold Level High 9: %s' % self.ef_hold_level_high_9
        #byte offset 111
        self.ef_hold_level_mid_high_9 = self.read_bytes()
        print 'EF Hold Level Mid-High 9: %s' % self.ef_hold_level_mid_high_9
        #byte offset 112
        self.ef_hold_level_mid_low_9 = self.read_bytes()
        print 'EF Hold Level Mid-Low 9: %s' % self.ef_hold_level_mid_low_9
        #byte offset 113
        self.ef_hold_level_low_9 = self.read_bytes()
        print 'EF Hold Level Low 9: %s' % self.ef_hold_level_low_9
        #byte offset 114
        self.ef_hold_level_high_10 = self.read_bytes()
        print 'EF Hold Level High 10: %s' % self.ef_hold_level_high_10
        #byte offset 115
        self.ef_hold_level_mid_high_10 = self.read_bytes()
        print 'EF Hold Level Mid-High 10: %s' % self.ef_hold_level_mid_high_10
        #byte offset 116
        self.ef_hold_level_mid_low_10 = self.read_bytes()
        print 'EF Hold Level Mid-Low 10: %s' % self.ef_hold_level_mid_low_10
        #byte offset 117
        self.ef_hold_level_low_10 = self.read_bytes()
        print 'EF Hold Level Low 10: %s' % self.ef_hold_level_low_10
        #byte offset 118
        self.ef_hold_level_high_11 = self.read_bytes()
        print 'EF Hold Level High 11: %s' % self.ef_hold_level_high_11
        #byte offset 119
        self.ef_hold_level_mid_high_11 = self.read_bytes()
        print 'EF Hold Level Mid-High 11: %s' % self.ef_hold_level_mid_high_11
        #byte offset 120
        self.ef_hold_level_mid_low_11 = self.read_bytes()
        print 'EF Hold Level Mid-Low 11: %s' % self.ef_hold_level_mid_low_11
        #byte offset 121
        self.ef_hold_level_low_11 = self.read_bytes()
        print 'EF Hold Level Low 11: %s' % self.ef_hold_level_low_11
        #byte offset 122
        self.ef_hold_level_high_12 = self.read_bytes()
        print 'EF Hold Level High 12: %s' % self.ef_hold_level_high_12
        #byte offset 123
        self.ef_hold_level_mid_high_12 = self.read_bytes()
        print 'EF Hold Level Mid-High 12: %s' % self.ef_hold_level_mid_high_12
        #byte offset 124
        self.ef_hold_level_mid_low_12 = self.read_bytes()
        print 'EF Hold Level Mid-Low 12: %s' % self.ef_hold_level_mid_low_12
        #byte offset 125
        self.ef_hold_level_low_12 = self.read_bytes()
        print 'EF Hold Level Low 12: %s' % self.ef_hold_level_low_12
        #byte offset 126
        self.ef_hold_level_high_13 = self.read_bytes()
        print 'EF Hold Level High 13: %s' % self.ef_hold_level_high_13
        #byte offset 127
        self.ef_hold_level_mid_high_13 = self.read_bytes()
        print 'EF Hold Level Mid-High 13: %s' % self.ef_hold_level_mid_high_13
        #byte offset 128
        self.ef_hold_level_mid_low_13 = self.read_bytes()
        print 'EF Hold Level Mid-Low 13: %s' % self.ef_hold_level_mid_low_13
        #byte offset 129
        self.ef_hold_level_low_13 = self.read_bytes()
        print 'EF Hold Level Low 13: %s' % self.ef_hold_level_low_13
        #byte offset 130
        self.ef_hold_level_high_14 = self.read_bytes()
        print 'EF Hold Level High 14: %s' % self.ef_hold_level_high_14
        #byte offset 131
        self.ef_hold_level_mid_high_14 = self.read_bytes()
        print 'EF Hold Level Mid-High 14: %s' % self.ef_hold_level_mid_high_14
        #byte offset 132
        self.ef_hold_level_mid_low_14 = self.read_bytes()
        print 'EF Hold Level Mid-Low 14: %s' % self.ef_hold_level_mid_low_14
        #byte offset 133
        self.ef_hold_level_low_14 = self.read_bytes()
        print 'EF Hold Level Low 14: %s' % self.ef_hold_level_low_14
        #byte offset 134
        self.ef_hold_level_high_15 = self.read_bytes()
        print 'EF Hold Level High 15: %s' % self.ef_hold_level_high_15
        #byte offset 135
        self.ef_hold_level_mid_high_15 = self.read_bytes()
        print 'EF Hold Level Mid-High 15: %s' % self.ef_hold_level_mid_high_15
        #byte offset 136
        self.ef_hold_level_mid_low_15 = self.read_bytes()
        print 'EF Hold Level Mid-Low 15: %s' % self.ef_hold_level_mid_low_15
        #byte offset 137
        self.ef_hold_level_low_15 = self.read_bytes()
        print 'EF Hold Level Low 15: %s' % self.ef_hold_level_low_15
        #byte offset 138
        self.ef_hold_level_high_16 = self.read_bytes()
        print 'EF Hold Level High 16: %s' % self.ef_hold_level_high_16
        #byte offset 139
        self.ef_hold_level_mid_high_16 = self.read_bytes()
        print 'EF Hold Level Mid-High 16: %s' % self.ef_hold_level_mid_high_16
        #byte offset 140
        self.ef_hold_level_mid_low_16 = self.read_bytes()
        print 'EF Hold Level Mid-Low 16: %s' % self.ef_hold_level_mid_low_16
        #byte offset 141
        self.ef_hold_level_low_16 = self.read_bytes()
        print 'EF Hold Level Low 16: %s' % self.ef_hold_level_low_16

    def get_assign_mode_eg2_reset_eg1_reset_trigger_mode_key_priority(self):
        b = self._get_binary_data()
        assign_mode = hex(int(b[6:8], 16))
        eg2_reset = hex(int(b[5], 16))
        eg1_reset = hex(int(b[4], 16))
        trigger_mode = hex(int(b[3], 16))
        key_priority = hex(int(b[0:2], 16))
        return assign_mode, eg2_reset, eg1_reset, trigger_mode, key_priority
    
    def get_lfo_key_sync_lfo_wave(self):
        b = self._get_binary_data()
        lfo_key_sync = hex(int(b[4:6], 16))
        lfo_wave = hex(int(b[0:2], 16))
        return lfo_key_sync, lfo_wave

    def get_lfo_tempo_sync_lfo_sync_note(self):
        b = self._get_binary_data()
        lfo_tempo_sync = hex(int(b[7], 16))
        lfo_sync_note = hex(int(b[0], 16))
        return lfo_tempo_sync, lfo_sync_note
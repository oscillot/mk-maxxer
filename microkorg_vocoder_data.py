from microkorg_abstract import MicroKorgAbstractData

class MicroKorgVocoderData(MicroKorgAbstractData):
    def __init__(self, data):
        self.data = data

        #byte offset 0
        self.midi_channel = self.get_next_bytes()
        #byte offset 1 !!!BITMAP
        self.assign_mode, self.eg2_reset, self.eg1_reset, self.trigger_mode, \
        self.key_priority = self.get_next_bytes()
        #byte offset 2
        self.unison_detune = self.get_next_bytes()

        ##PITCH
        #byte offset 3
        self.pitch_tune = self.get_next_bytes()
        #byte offset 4
        self.pith_bend_range = self.get_next_bytes()
        #byte offset 5
        self.pitch_transpose = self.get_next_bytes()
        #byte offset 6
        self.pitch_vibrato_int = self.get_next_bytes()

        ##OSC
        #byte offset 7
        self.osc_wave = self.get_next_bytes()
        #byte offset 8
        self.osc_waveform_ctrl1 = self.get_next_bytes()
        #byte offset 9
        self.osc_waveform_ctrl2 = self.get_next_bytes()
        #byte offset 10
        self.osc_dwgs_wave = self.get_next_bytes()
        #byte offset 11 (dummy)


        ##AUDIO IN1
        #byte offset 12
        self.audio_in1_hpf_gate = self.get_next_bytes()
        #byte offset 13 (dummy)


        ##PITCH (2)
        #byte offset 14
        self.pitch_portamento_time = self.get_next_bytes()

        ##MIXER
        #byte offset 15
        self.mixer_osc1_level = self.get_next_bytes()
        #byte offset 16
        self.mixer_ext1_level = self.get_next_bytes()
        #byte offset 17
        self.mixer_noise_level = self.get_next_bytes()

        ##AUDIO IN1 (2)
        #byte offset 18
        self.audio_in1_hpf_level = self.get_next_bytes()
        #byte offset 19
        self.audio_in1_gate_sense = self.get_next_bytes()
        #byte offset 20
        self.audio_in1_theshold = self.get_next_bytes()

        ##FILTER
        #byte offset 21
        self.filter_shift = self.get_next_bytes()
        #byte offset 22
        self.filter_cutoff = self.get_next_bytes()
        #byte offset 23
        self.filter_resonance = self.get_next_bytes()
        #byte offset 24
        self.filter_mod_source = self.get_next_bytes()
        #byte offset 25
        self.filter_intensity = self.get_next_bytes()
        #byte offset 26
        self.filter_e_f_sense = self.get_next_bytes()

        ##AMP
        #byte offset 27
        self.amp_level = self.get_next_bytes()
        #byte offset 28
        self.amp_direct_level = self.get_next_bytes()
        #byte offset 29
        self.amp_distortion_on_off = self.get_next_bytes()
        #byte offset 30
        self.amp_velocity_sense = self.get_next_bytes()
        #byte offset 31
        self.amp_keytrack = self.get_next_bytes()

        ##EG1
        #byte offset 32
        self.eg1_attack = self.get_next_bytes()
        #byte offset 33
        self.eg1_decay = self.get_next_bytes()
        #byte offset 34
        self.eg1_sustain = self.get_next_bytes()
        #byte offset 35
        self.eg1_release = self.get_next_bytes()

        ##EG2
        #byte offset 36
        self.eg2_attack = self.get_next_bytes()
        #byte offset 37
        self.eg2_decay = self.get_next_bytes()
        #byte offset 38
        self.eg2_sustain = self.get_next_bytes()
        #byte offset 39
        self.eg2_release = self.get_next_bytes()

        ##LFO1
        #byte offset 40 !!!BITMAP
        self.lfo1_key_sync, self.lfo1_wave = self.get_next_bytes()
        #byte offset 41
        self.lfo1_frequency = self.get_next_bytes()
        #byte offset 42 !!!BITMAP
        self.lfo1_tempo_sync, self.lfo1_sync_note = self.get_next_bytes()

        ##LFO2
        #byte offset 43 !!!BITMAP
        self.lfo2_key_sync, self.lfo2_wave = self.get_next_bytes()
        #byte offset 44
        self.lfo2_frequency = self.get_next_bytes()
        #byte offset 45 !!!BITMAP
        self.lfo2_tempo_sync, self.lfo2_sync_note = self.get_next_bytes()

        ##LEVELS
        #byte offset 46
        self.level_1 = self.get_next_bytes()
        #byte offset 47
        self.level_2 = self.get_next_bytes()
        #byte offset 48
        self.level_3 = self.get_next_bytes()
        #byte offset 49
        self.level_4 = self.get_next_bytes()
        #byte offset 50
        self.level_5 = self.get_next_bytes()
        #byte offset 51
        self.level_6 = self.get_next_bytes()
        #byte offset 52
        self.level_7 = self.get_next_bytes()
        #byte offset 53
        self.level_8 = self.get_next_bytes()
        #byte offset 54
        self.level_9 = self.get_next_bytes()
        #byte offset 55
        self.level_10 = self.get_next_bytes()
        #byte offset 56
        self.level_11 = self.get_next_bytes()
        #byte offset 57
        self.level_12 = self.get_next_bytes()
        #byte offset 58
        self.level_13 = self.get_next_bytes()
        #byte offset 59
        self.level_14 = self.get_next_bytes()
        #byte offset 60
        self.level_15 = self.get_next_bytes()
        #byte offset 61
        self.level_16 = self.get_next_bytes()

        ##PAN
        #byte offset 62
        self.pan_1 = self.get_next_bytes()
        #byte offset 63
        self.pan_2 = self.get_next_bytes()
        #byte offset 64
        self.pan_3 = self.get_next_bytes()
        #byte offset 65
        self.pan_4 = self.get_next_bytes()
        #byte offset 66
        self.pan_5 = self.get_next_bytes()
        #byte offset 67
        self.pan_6 = self.get_next_bytes()
        #byte offset 68
        self.pan_7 = self.get_next_bytes()
        #byte offset 69
        self.pan_8 = self.get_next_bytes()
        #byte offset 70
        self.pan_9 = self.get_next_bytes()
        #byte offset 71
        self.pan_10 = self.get_next_bytes()
        #byte offset 72
        self.pan_11 = self.get_next_bytes()
        #byte offset 73
        self.pan_12 = self.get_next_bytes()
        #byte offset 74
        self.pan_13 = self.get_next_bytes()
        #byte offset 75
        self.pan_14 = self.get_next_bytes()
        #byte offset 76
        self.pan_15 = self.get_next_bytes()
        #byte offset 77
        self.pan_16 = self.get_next_bytes()

        ##EF HOLD LEVEL
        #byte offset 78
        self.ef_hold_level_high_1 = self.get_next_bytes()
        #byte offset 79
        self.ef_hold_level_mid_high_1 = self.get_next_bytes()
        #byte offset 80
        self.ef_hold_level_mid_low_1 = self.get_next_bytes()
        #byte offset 81
        self.ef_hold_level_low_1 = self.get_next_bytes()
        #byte offset 82
        self.ef_hold_level_high_2 = self.get_next_bytes()
        #byte offset 83
        self.ef_hold_level_mid_high_2 = self.get_next_bytes()
        #byte offset 84
        self.ef_hold_level_mid_low_2 = self.get_next_bytes()
        #byte offset 85
        self.ef_hold_level_low_2 = self.get_next_bytes()
        #byte offset 86
        self.ef_hold_level_high_3 = self.get_next_bytes()
        #byte offset 87
        self.ef_hold_level_mid_high_3 = self.get_next_bytes()
        #byte offset 88
        self.ef_hold_level_mid_low_3 = self.get_next_bytes()
        #byte offset 89
        self.ef_hold_level_low_3 = self.get_next_bytes()
        #byte offset 90
        self.ef_hold_level_high_4 = self.get_next_bytes()
        #byte offset 91
        self.ef_hold_level_mid_high_4 = self.get_next_bytes()
        #byte offset 92
        self.ef_hold_level_mid_low_4 = self.get_next_bytes()
        #byte offset 93
        self.ef_hold_level_low_4 = self.get_next_bytes()
        #byte offset 94
        self.ef_hold_level_high_5 = self.get_next_bytes()
        #byte offset 95
        self.ef_hold_level_mid_high_5 = self.get_next_bytes()
        #byte offset 96
        self.ef_hold_level_mid_low_5 = self.get_next_bytes()
        #byte offset 97
        self.ef_hold_level_low_5 = self.get_next_bytes()
        #byte offset 98
        self.ef_hold_level_high_6 = self.get_next_bytes()
        #byte offset 99
        self.ef_hold_level_mid_high_6 = self.get_next_bytes()
        #byte offset 100
        self.ef_hold_level_mid_low_6 = self.get_next_bytes()
        #byte offset 101
        self.ef_hold_level_low_6 = self.get_next_bytes()
        #byte offset 102
        self.ef_hold_level_high_7 = self.get_next_bytes()
        #byte offset 103
        self.ef_hold_level_mid_high_7 = self.get_next_bytes()
        #byte offset 104
        self.ef_hold_level_mid_low_7 = self.get_next_bytes()
        #byte offset 105
        self.ef_hold_level_low_7 = self.get_next_bytes()
        #byte offset 106
        self.ef_hold_level_high_8 = self.get_next_bytes()
        #byte offset 107
        self.ef_hold_level_mid_high_8 = self.get_next_bytes()
        #byte offset 108
        self.ef_hold_level_mid_low_8 = self.get_next_bytes()
        #byte offset 109
        self.ef_hold_level_low_8 = self.get_next_bytes()
        #byte offset 110
        self.ef_hold_level_high_9 = self.get_next_bytes()
        #byte offset 111
        self.ef_hold_level_mid_high_9 = self.get_next_bytes()
        #byte offset 112
        self.ef_hold_level_mid_low_9 = self.get_next_bytes()
        #byte offset 113
        self.ef_hold_level_low_9 = self.get_next_bytes()
        #byte offset 114
        self.ef_hold_level_high_10 = self.get_next_bytes()
        #byte offset 115
        self.ef_hold_level_mid_high_10 = self.get_next_bytes()
        #byte offset 116
        self.ef_hold_level_mid_low_10 = self.get_next_bytes()
        #byte offset 117
        self.ef_hold_level_low_10 = self.get_next_bytes()
        #byte offset 118
        self.ef_hold_level_high_11 = self.get_next_bytes()
        #byte offset 119
        self.ef_hold_level_mid_high_11 = self.get_next_bytes()
        #byte offset 120
        self.ef_hold_level_mid_low_11 = self.get_next_bytes()
        #byte offset 121
        self.ef_hold_level_low_11 = self.get_next_bytes()
        #byte offset 122
        self.ef_hold_level_high_12 = self.get_next_bytes()
        #byte offset 123
        self.ef_hold_level_mid_high_12 = self.get_next_bytes()
        #byte offset 124
        self.ef_hold_level_mid_low_12 = self.get_next_bytes()
        #byte offset 125
        self.ef_hold_level_low_12 = self.get_next_bytes()
        #byte offset 126
        self.ef_hold_level_high_13 = self.get_next_bytes()
        #byte offset 127
        self.ef_hold_level_mid_high_13 = self.get_next_bytes()
        #byte offset 128
        self.ef_hold_level_mid_low_13 = self.get_next_bytes()
        #byte offset 129
        self.ef_hold_level_low_13 = self.get_next_bytes()
        #byte offset 130
        self.ef_hold_level_high_14 = self.get_next_bytes()
        #byte offset 131
        self.ef_hold_level_mid_high_14 = self.get_next_bytes()
        #byte offset 132
        self.ef_hold_level_mid_low_14 = self.get_next_bytes()
        #byte offset 133
        self.ef_hold_level_low_14 = self.get_next_bytes()
        #byte offset 134
        self.ef_hold_level_high_15 = self.get_next_bytes()
        #byte offset 135
        self.ef_hold_level_mid_high_15 = self.get_next_bytes()
        #byte offset 136
        self.ef_hold_level_mid_low_15 = self.get_next_bytes()
        #byte offset 137
        self.ef_hold_level_low_15 = self.get_next_bytes()
        #byte offset 138
        self.ef_hold_level_high_16 = self.get_next_bytes()
        #byte offset 139
        self.ef_hold_level_mid_high_16 = self.get_next_bytes()
        #byte offset 140
        self.ef_hold_level_mid_low_16 = self.get_next_bytes()
        #byte offset 141
        self.ef_hold_level_low_16 = self.get_next_bytes()
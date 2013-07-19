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

        ##LEVEL
        #byte offset 46-61

        ##PAN
        #byte offset 62-77

        ##EF HOLD LEVEL
        #byte offset 78-141
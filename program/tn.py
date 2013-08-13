T1 = {
    0: '1/32',
    1: '1/24',
    2: '1/16',
    3: '1/12',
    4: '3/32',
    5: '1/8',
    6: '1/6',
    7: '3/16',
    8: '1/4',
    9: '1/3',
    10: '3/8',
    11: '1/2',
    12: '2/3',
    13: '3/4',
    14: '1/1'
}


T2 = {
    0: 'Saw',
    1: 'Pulse',
    2: 'Tri',
    3: 'Sin(Cross)',
    4: 'Vox Wave',
    5: 'DWGS',
    6: 'Noise',
    7: 'Audio In'
}


T3 = {
    0: 'EG1',
    1: 'EG2',
    2: 'LFO1',
    3: 'LFO2',
    4: 'VELOCITY',
    5: 'KBD TRACK',
    6: 'P.Bend(MIDI1)',
    7: 'Mod(MIDI2)'
}


T4 = {
    0: 'PITCH',
    1: 'OSC2 PITCH',
    2: 'OSC1 CNTL1',
    3: 'NOISE LEVEL',
    4: 'CUTOFF',
    5: 'AMP',
    6: 'PAN',
    7: 'LFO2 FREQ'
}


def build_T5():
    return {abs(k - 14): v for k, v in T1.items()}


T5 = build_T5()


def build_T6():
    T6 = {0: '1/48'}
    for r in range(0, 15):
        T6[r+1] = T1[r]
    return T6


T6 = build_T6()


#t7 might need to be a function outright... what is this for anyway? This
# might be way off... who knows, we'll see
def build_T7():
    T7 = {
        0: {
            'display': 'Crv',
            'Vel.Value': '***',
            'Vel.Curve': 2
        }
    }
    for r in range(1, 128):
        T7[r] = {
            'display': r,
            'Vel.Value': r,
            'Vel.Curve': 8
            }
    return T7


T7 = build_T7()


def build_T8():
    T8 = {}
    for t in range(0, 16):
        for r, d in zip(range(0+(8*t), 8+(8*t)), range(1, 9)):
            if r > 63:
                bank = 'B'
            else:
                bank = 'A'
            if t > 7:
                mid = t-7
            else:
                mid = t+1
            T8[r] = '%s%s%d' % (bank, mid, d)
    return T8


T8 = build_T8()


T9 = {
    0: 'Portamento',
    1: 'OSC1 Wave Sw',
    2: 'OSC1 Ctrl1',
    3: 'OSC1 Ctrl2',
    4: 'OSC2 Wave Sw',
    5: 'OSC2 Mod Sw',
    6: 'OSC2 Semitone',
    7: 'OSC2 Tune',
    8: 'OSC1 Level',
    9: 'OSC2 Level',
    10: 'Noise Level',
    11: 'Filter Type Sw',
    12: 'Cutoff',
    13: 'Resonance',
    14: 'EG1 Int',
    15: 'FLT KbdTrack',
    16: 'AMP Level',
    17: 'Panpot',
    18: 'EG2/Gate Sw',
    19: 'Distortion',
    20: 'EG1 Attack',
    21: 'EG1 Decay',
    22: 'EG1 Sustain',
    23: 'EG1 Release',
    24: 'EG2 Attack',
    25: 'EG2 Decay',
    26: 'EG2 Sustain',
    27: 'EG2 Release',
    28: 'LFO1 Wave',
    29: 'LFO1 Freq',
    30: 'LFO2 Wave',
    31: 'LFO2 Freq',
    32: 'PATCH1 Int',
    33: 'PATCH2 Int',
    34: 'PATCH3 Int',
    35: 'PATCH4 Int',
    36: 'SEQ Off/On Sw',
    37: 'Mod Speed',
    38: 'Mod Depth',
    39: 'Delay Time',
    40: 'Delay Feedback',
    41: '(dummy byte)'
}


def build_T10():
    T10 = {
        27: 14.0,
        28: 16.0,
        29: 18.0
    }
    for r in range(0, 21):
        T10[r] = 1.00 + (r*0.25)
    for r in range(21, 27):
        T10[r] = float(r-14)
    return T10


T10 = build_T10()


def build_T11():
    T11 = {}
    for r in range(0, 3):
        T11[r] = 40 + (r*10)
    for r in range(3, 25):
        T11[r] = 20 + (r*20)
    for r in range(25, 30):
        T11[r] = (r-19) * 100
    return T11


T11 = build_T11()


T12 = {
    0: 'Up',
    1: 'Down',
    2: 'Alt1',
    3: 'Alt2',
    4: 'Random',
    5: 'Trigger',
}


def build_T13():
    T13 = {k: v for k, v in T3.items()}
    T13[0] = '---'
    T13[1] = 'AEG'
    return T13

T13 = build_T13()
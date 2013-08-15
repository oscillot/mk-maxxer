"""
*T-1 :
        0: 1/32     5: 1/8      10: 3/8
        1: 1/24     6: 1/6      11: 1/2
        2: 1/16     7: 3/16     12: 2/3
        3: 1/12     8: 1/4      13: 3/4
        4: 3/32     9: 1/3      14: 1/1

"""

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

"""
*T-2 :
        0: Saw          4: Vox Wave
        1: Pulse        5: DWGS
        2: Tri          6: Noise
        3: Sin(Cross)   7: Audio In

"""

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

"""
*T-3 :
        0: EG1      4: VELOCITY
        1: EG2      5: KBD TRACK
        2: LFO1     6: P.Bend(MIDI1)
        3: LFO2     7: Mod(MIDI2)

"""


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

"""
*T-4 :
        0: PITCH            4: CUTOFF
        1: OSC2 PITCH       5: AMP
        2: OSC1 CNTL1       6: PAN
        3: NOISE LEVEL      7: LFO2 FREQ

"""


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

"""
*T-5 :
        0: 1/1      5: 1/3      10: 3/32
        1: 3/4      6: 1/4      11: 1/12
        2: 2/3      7: 3/16     12: 1/16
        3: 1/2      8: 1/6      13: 1/24
        4: 3/8      9: 1/8      14: 1/32

"""


def build_T5():
    return {abs(k - 14): v for k, v in T1.items()}


T5 = build_T5()

"""
*T-6 :
        0: 1/48     5: 3/32     10: 1/3     15: 1/1
        1: 1/32     6: 1/8      11: 3/8
        2: 1/24     7: 1/6      12: 1/2
        3: 1/16     8: 3/16     13: 2/3
        4: 1/12     9: 1/4      14: 3/4

"""


def build_T6():
    T6 = {0: '1/48'}
    for r in range(0, 15):
        T6[r+1] = T1[r]
    return T6


T6 = build_T6()

"""
*T-7 :
        display     Vel.Value   Vel.Curve
        Crv         ***         2
        1           1           8
        2           2           8
        ''          ''          ''
        127         127         8

"""


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

"""
*T-8 :
        P.Chg[000]  00  (A11)
        P.Chg[001]  01  (A12)
        P.Chg[002]  02  (A13)
        P.Chg[003]  03  (A14)
        P.Chg[004]  04  (A15)
        ''          ''  ''
        P.Chg[124]  7C  (b85)
        P.Chg[125]  7D  (b86)
        P.Chg[126]  7E  (b87)
        P.Chg[127]  7F  (b88)

"""


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

"""
*T-9 :
        [+00]: Portamento       [+20]: EG1 Attack       [+40]: Delay Feedback
        [+01]: OSC1 Wave Sw     [+21]: EG1 Decay        [+41]: (dummy byte)
        [+02]: OSC1 Ctrl1       [+22]: EG1 Sustain
        [+03]: OSC1 Ctrl2       [+23]: EG1 Release
        [+04]: OSC2 Wave Sw     [+24]: EG2 Attack
        [+05]: OSC2 Mod Sw      [+25]: EG2 Decay
        [+06]: OSC2 Semitone    [+26]: EG2 Sustain
        [+07]: OSC2 Tune        [+27]: EG2 Release
        [+08]: OSC1 Level       [+28]: LFO1 Wave
        [+09]: OSC2 Level       [+29]: LFO1 Freq
        [+10]: Noise Level      [+30]: LFO2 Wave
        [+11]: Filter Type Sw   [+31]: LFO2 Freq
        [+12]: Cutoff           [+32]: PATCH1 Int
        [+13]: Resonance        [+33]: PATCH2 Int
        [+14]: EG1 Int          [+34]: PATCH3 Int
        [+15]: FLT KbdTrack     [+35]: PATCH4 Int
        [+16]: AMP Level        [+36]: SEQ Off/On Sw
        [+17]: Panpot           [+37]: Mod Speed
        [+18]: EG2/Gate Sw      [+38]: Mod Depth
        [+19]: Distortion       [+39]: Delay Time

"""

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

"""
*T-10 :
        0: 1.00         10: 3.50        20: 6.00
        1: 1.25         11: 3.75        21: 7.00
        2: 1.50         12: 4.00        22: 8.00
        3: 1.75         13: 4.25        23: 9.00
        4: 2.00         14: 4.50        24: 10.0
        5: 2.25         15: 4.75        25: 11.0
        6: 2.50         16: 5.00        26: 12.0
        7: 2.75         17: 5.25        27: 14.0
        8: 3.00         18: 5.50        28: 16.0
        9: 3.25         19: 5.75        29: 18.0

"""

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

"""
*T-11 :

        0: 40           10: 220         20: 420
        1: 50           11: 240         21: 440
        2: 60           12: 260         22: 460
        3: 80           13: 280         23: 480
        4: 100          14: 300         24: 500
        5: 120          15: 320         25: 600
        6: 140          16: 340         26: 700
        7: 160          17: 360         27: 800
        8: 180          18: 380         28: 900
        9: 200          19: 400         29: 1000

"""

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

"""
*T-12 :

        0: Up
        1: Down
        2: Alt1
        3: Alt2
        4: Random
        5: Trigger

"""

T12 = {
    0: 'Up',
    1: 'Down',
    2: 'Alt1',
    3: 'Alt2',
    4: 'Random',
    5: 'Trigger',
}


"""
*T-13 :

        0: ---
        1: AEG
        2: LFO1
        3: LFO2
        4: VELOCITY
        5: KBD TRACK
        6: P.Bend(MIDI1)
        7: Mod(MIDI2)

"""

def build_T13():
    T13 = {k: v for k, v in T3.items()}
    T13[0] = '---'
    T13[1] = 'AEG'
    return T13

T13 = build_T13()
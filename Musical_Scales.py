# Musical_Scales.py

# musicalscales
# https://open.kattis.com/problems/musicalscales

# python Musical_Scales.py < Musical_Scales_in.txt

from collections import defaultdict

all_notes = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
noteconvert = dict(zip(all_notes,range(12)))
all_scale = defaultdict(set)
for i,note in enumerate(all_notes):
    all_scale[note] = set(all_notes[(i+n)%12]for n in [0,2,4,5,7,9,11])
input()
song = set(input().split())
fittable = []
for scale_name,scale_notes in all_scale.items():
    if not song-scale_notes:
        fittable.append(scale_name)
if fittable:
    print(*fittable,sep=' ')
else:
    print('none')
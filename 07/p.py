from sys import argv
from collections import Counter as cnt
from functools import partial as part

input = argv[1] if len(argv) > 1 else "input.txt"

with open(input) as f:
    lines = [(x[0], int(x[1])) for x in [x.split() for x in f.readlines()]]

def h(p, h):
    cards, w, f = ('J' if p else '')+'23456789TJQKA', [51,42,32,33,23,24,15], cnt(h[0])
    p and f.update({((f-cnt(J=5)).most_common(1) or [('K',0)])[0][0]:f.pop('J',0)})
    return [w.index(len(f)*10+f.most_common(1)[0][1])]+list(map(cards.find,h[0]))+[h[1]]

for p in [0,1]:
    print(sum([ x[0] * x[1][-1] for x in enumerate(sorted(lines,key=part(h, p)),1) ]))

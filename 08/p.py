from sys import argv
from math import lcm
with open(argv[1] if len(argv) > 1 else 'input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
direction, ld = lines[0] , len(lines[0])
maps = {x.split(' = ')[0]:x.split(' = ')[1][1:-1].split(', ') for x in lines[2:]}
parts = [['AAA'], filter(lambda x: x.endswith('A'), maps) ]
def dist(p):
    i = ( i for i,_ in enumerate(iter(int,1)) )
    while set(p[p.count('A')//len(p)-1:]) - set('Z'):
        p = maps[p][ord(direction[next(i)%ld])//6-12]
    return next(i)
[print(lcm(*[dist(p) for p in start])) for start in parts]

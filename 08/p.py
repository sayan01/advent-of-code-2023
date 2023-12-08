from sys import argv
from math import lcm
with open(argv[1] if len(argv) > 1 else 'input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
direction,_, *maps, ld = *lines , len(lines[0])
maps = {x.split(' = ')[0]:x.split(' = ')[1][1:-1].split(', ') for x in maps}
def dist(p):
    i = ( i for i,_ in enumerate(iter(int,1)) )
    while set(p[p.count('A')//len(p)-1:]) - set('Z'):
        p = maps[p][direction[next(i)%ld]=='R']
    return next(i)
print(dist('AAA'), lcm(*map(dist, filter(lambda x: x.endswith('A'), maps))), sep='\n')

from math import lcm
dir, _, *maps = [line.strip() for line in open('input.txt').readlines()]
maps={x.split(' = ')[0]:x.split(' = ')[1].strip('()').split(', ') for x in maps}
def dist(p):
    i = ( i for i,_ in enumerate(iter(int,1)) )
    while set(p[p.count('A')//len(p)-1:]) - set('Z'):
        p = maps[p][dir[next(i)%len(dir)]=='R']
    return next(i)
print(dist('AAA'), lcm(*map(dist, [x for x in maps if x.endswith('A')]  )), sep='\n')

from functools import reduce
input = 'input.txt'
with open(input, 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

allowed = { 'red': 12, 'green': 13, 'blue': 14 }
lines = [ [int(line.split(': ')[0].split(' ')[1]), [(int(y.split(' ')[0]), y.split(' ')[1]) for x in line.split(': ')[1].split('; ') for y in x.split(', ') ] ] for line in lines]
part1, part2 = 0, 0
for iid,line in lines:
    maxfound = { key: max(val for val,k in line if k == key) for _,key in line }
    part1 += iid if all([maxfound[key] <= allowed[key] for key in maxfound]) else 0
    part2 += reduce(lambda x,y: x*y, maxfound.values())

print(part1)
print(part2)

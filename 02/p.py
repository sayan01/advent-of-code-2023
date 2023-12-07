from math import prod
with open('input.txt') as f:
    lines = [line.strip().replace(';', ',')[5:].split(': ') for line in f.readlines()]

allowed = { 'red' : 12, 'green' : 13, 'blue' : 14 }
lines = [[int(i[0]), dict(sorted([[j[1], int(j[0])] for j in [k.split(' ') for k in i[1].split(', ')]]))] for i in lines]

part1 = sum([ i for i, line in lines if all([line[k] <= allowed[k] for k in line])])
part2 = sum([ prod(line.values()) for _, line in lines])
print(part1, part2, sep='\n')

from sys import argv
from math import sqrt, floor, ceil, prod, log10
from functools import reduce
input = argv[1] if len(argv) > 1 else "input.txt"
with open(input) as ff:
    lines = [line.strip() for line in ff.readlines()]

times, distances = [list(map(int,line.split(':')[1].strip().split())) for line in lines]

def findroots(t,d):
    return ceil((t + (disc:=(sqrt(t**2-4*d))))/2) - floor((t - disc)/2) - 1

total = prod(map(findroots, times, distances))
print(total)

def intjoin(a,b):
    return a*10**(floor(log10(b))+1)+b
newtime = reduce(intjoin, times)
newdist = reduce(intjoin, distances)
print(findroots(newtime,newdist))

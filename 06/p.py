from math import sqrt, floor, ceil, prod
t, d = [list(map(int,line.split(':')[1].strip().split())) for line in open('input.txt')]
def solve(t,d):
    return ceil((t + (disc:=(sqrt(t**2-4*d))))/2) - floor((t - disc)/2) - 1
print(prod(map(solve, t, d)))
print(solve(int(''.join(map(str, t))), int(''.join(map(str, d)))))

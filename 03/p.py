from sys import argv
input = (argv[1] if len(argv) > 1 else '' ) or 'input.txt'
with open(input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

current_number = ''
adjacent_symbol = set()
allnumbers = []
nmap = {}
digits = '0123456789'
lines = ['.'+line+'.' for line in lines]
lines = ['.'*len(lines[0])] + lines + ['.'*len(lines[0])]
for i,line in enumerate(lines):
    for j,char in enumerate(line):
        if char in digits:
            current_number += char
            for ii in range(max(0,i-1), min(i+2,len(lines))):
                for jj in range(max(0,j-1), min(j+2,len(line))):
                    if lines[ii][jj] not in digits+'.':
                        adjacent_symbol.add((lines[ii][jj],ii,jj))
        else:
            if current_number:
                current_number = int(current_number)
                if adjacent_symbol:
                    allnumbers.append(current_number)
                    nmap[(current_number,i,j)] = adjacent_symbol
                current_number = ''
                adjacent_symbol = set()

print(sum(allnumbers))
# part 2
#find gear ratio of all gear numbers (product of number with common * symbol(exactly 2))

def is_gear(x):
    return x[0] == '*'

def get_gears(x):
    return list(filter(is_gear, nmap[x]))

gear_numbers = { n:get_gears(n) for n in nmap if get_gears(n) }
gears = {}

for number in gear_numbers:
    for adj_star in gear_numbers[number]:
        gears[adj_star] = gears.get(adj_star,[]) + [number]

gears = {k:v for k,v in gears.items() if len(v) == 2}
print(sum([g[0][0]*g[1][0] for g in gears.values()]))

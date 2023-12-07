input = 'input.txt'
with open(input) as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

# Part 1

sumnumbers = 0
for line in lines:
    firstnumber = 0
    lastnumber = 0
    for i in range(len(line)):
        if line[i].isdigit():
            firstnumber = int(line[i])
            break

    for i in range(len(line), 0, -1):
        if line[i-1].isdigit():
            lastnumber = int(line[i-1])
            break

    sumnumbers += 10 * firstnumber + lastnumber

print(sumnumbers)

# Part 2
# the digits may also be spelled out (zero, one, two, three, four, five, six, seven, eight, nine)

digits = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four' : 4,
    'five' : 5,
    'six' : 6,
    'seven' : 7,
    'eight' : 8,
    'nine' : 9,
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9
}

sumnumbers = 0
for line in lines:
    firstindex = -1
    lastindex = -1
    firstnumber = 0
    lastnumber = 0
    for dig in digits:
        if dig in line:
            if line.index(dig) < firstindex or firstindex == -1:
                firstindex = line.index(dig)
                firstnumber = digits[dig]
            if line.rindex(dig) > lastindex or lastindex == -1:
                lastindex = line.rindex(dig)
                lastnumber = digits[dig]


    sumnumbers += 10 * firstnumber + lastnumber

print(sumnumbers)

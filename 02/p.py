from math import prod
L = [x.strip().replace(';',',')[5:].split(': ') for x in open('input.txt')]
L = [[int(i[0]),dict(sorted([[j[1],int(j[0])]for j in[k.split(' ')for k in i[1].split(', ')]]))]for i in L]
p1 = sum([i for i,x in L if all([x[k]<={'red':12,'green':13,'blue':14}[k] for k in x])])
print(p1, sum([ prod(line.values()) for _, line in L ]), sep='\n')

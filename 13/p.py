from Levenshtein import distance as D
S=[[x for x in s.split('\n')if x]for s in open('input.txt').read().split('\n\n')]

def h(x,i,r):
    return x[:i][-min(i,r-i):][::-1],x[i:][:min(i,r-i)]

def ci(s,d=0):
    r = range(1,len(s[0]))
    return next((i for i in r if sum(D(*h(x,i,r.stop))for x in s)==d),0)

def ri(s,d=0):
    r = range(1,len(s))
    return next((i for i in r if sum(D(x,y)for x,y in zip(*h(s,i,r.stop)))==d),0)

[print(sum(ri(s,p) for s in S) * 100 + sum(ci(s,p) for s in S))for p in [0,1]]

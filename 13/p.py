from Levenshtein import distance as D
S=[[x for x in s.split('\n')if x]for s in open('input.txt').read().split('\n\n')]
def c(s,d=0):
  r = range(1,len(s[0]))
  return next((i for i in r if sum(D(*zip(*zip(x[:i][::-1],x[i:]))) for x in s)==d),0)
[print(sum(c(list(zip(*s)),p) for s in S)*100+sum(c(s,p) for s in S)) for p in [0,1]]

from collections import Counter as c
lines = [(x[0], int(x[1])) for x in [x.split() for x in open('input.txt').readlines()]]
def key(h):
    f, j, w, cards = c(h[0]),c(J=5), [51,42,32,33,23,24,15], " J"[p]+'23456789TJQKA'
    f.update({((f-j).most_common(1) or [('K',0)])[0][0]:f.pop('J',0)} if p else {})
    return [w.index(len(f)*10+f.most_common(1)[0][1])]+list(map(cards.find,h[0]))+[h[1]]
for p in [0,1]:
    print(sum([ x[0] * x[1][-1] for x in enumerate(sorted(lines,key=key),1) ]))

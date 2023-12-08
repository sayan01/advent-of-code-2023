L=[line.strip()for line in open('input.txt').readlines()]
d=dict(zip(map(str,range(10)),range(10)))
for _ in 'hi':
 print(sum([d[f([x for x in d if x in l],key=k)]*i for l in L for i,f,k in[[10,min,l.find],[1,max,l.rfind]]]))
 d.update(dict(zip(['zero','one','two','three','four','five','six','seven','eight','nine'],range(10))))

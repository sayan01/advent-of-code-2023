from itertools import combinations as comb
L = [x.strip() for x in open('input.txt')]
n,m,L_ = list(range(len(L))), list(range(len(L[0]))), list(zip(*L))
er,ec = {i for i in n if set(L[i]) == {'.'}},{j for j in m if set(L_[j]) == {'.'}}
galaxies = [ (i, j) for i in n for j in m if L[i][j] == '#' ]
def expand(i, j, by=1):
  return i + by*len(set(range(i))&er), j + by*len(set(range(j))&ec)
parts = [[expand(*g, i) for g in galaxies] for i in [1, 999_999]]
for part in parts:
  print(sum(abs(p[0][0]-p[1][0]) + abs(p[0][1]-p[1][1]) for p in list(comb(part, 2))))

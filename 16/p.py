tiles,L,R,U,D,V,H=[x.strip()for x in open('input.txt')],'L','R','U','D','UD','LR'
dirs,n,m,={R:(1,0),L:(-1,0),U:(0,-1),D:(0,1)},list(range(len(tiles))),list(range(len(tiles[0])))
M={R:{'/':U,'\\':D,'|':V},L:{'/':D,'\\':U,'|':V},U:{'/':R,'\\':L,'-':H},D:{'/':L,'\\':R,'-':H}}
S=[(x,0,D)for x in m]+[(0,y,R)for y in n]+[(x,n[-1],U)for x in m]+[(m[-1],y,L)for y in n]
def traverse(s):
  lp,Q = set(),[s]
  while Q:
    x, y, dir = Q.pop(0)
    if (x, y, dir) not in lp and x in (n) and y in (m):
      lp.add((x, y, dir))
      [Q.append((x+dirs[d][0],y+dirs[d][1],d))for d in M[dir].get(tiles[y][x],dir)]
  return len({(x, y) for x, y, _ in lp})
print(traverse((0,0,R)),max(traverse(s) for s in S),sep='\n')

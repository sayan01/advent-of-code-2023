"""
| is a vertical pipe connecting up and down
- is a horizontal pipe connecting right and left
L is a 90-degree bend connecting up and right
J is a 90-degree bend connecting up and left
7 is a 90-degree bend connecting down and left
F is a 90-degree bend connecting down and right
. is ground; there is no pipe in this tile
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""
from sys import argv, setrecursionlimit
setrecursionlimit(100000)
lines = [line.strip() for line in open(argv[1] if len(argv) > 1 else 'input.txt')]

S_index = [ (i,j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == 'S' ][0]
pipes = {
  '|': [(-1,0),(1,0)],
  '-': [(0,-1),(0,1)],
  'L': [(-1,0),(0,1)],
  'J': [(-1,0),(0,-1)],
  '7': [(1,0),(0,-1)],
  'F': [(1,0),(0,1)],
  'S': [(-1,0),(1,0),(0,-1),(0,1)],
  '.': [],
}

def get_path(i, j, lines, path=None, visited=None, target='S'):
  path = path or []
  visited = visited or {(i,j),}
  if i < 0 or i >= len(lines) or j < 0 or j >= len(lines[i]):
      return [], False
  if lines[i][j] == target:
      return path, True
  for di, dj in pipes[lines[i][j]]:
    if (i+di, j+dj) not in visited and (-di,-dj) in pipes[lines[i+di][j+dj]]:
      p, found = get_path(i+di, j+dj, lines, path + [(i,j)], visited | {(i+di, j+dj)}, target)
      if found:
        return p, True
  return [], False
i, j = S_index
visited = {(i,j),}
ans = []
for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
  if (-di,-dj) not in pipes[lines[i+di][j+dj]]:
    continue
  p, found = get_path(i+di, j+dj, lines, [(i,j)])
  if found:
    ans.append(p)
    print("->".join(map(lambda x: lines[x[0]][x[1]], p)), (len(p))//2)

ans = max(ans, key=lambda x: len(x))
nests = 0
for i in range(len(lines)):
    up = False
    for j in range(len(lines[i])):
        if (i,j) in ans:
            print(lines[i][j], end='')
            if lines[i][j] in '|JLS':
                up = not up
        else:
            if up:
                nests += 1
                print('.', end='')
            else:
                print(' ', end='')
    print()

print(nests)

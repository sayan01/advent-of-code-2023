lines = [list(map(int,line.strip().split())) for line in open("input.txt")]
def n(seq:list[int]) -> list[int]:
  d = [seq[i+1] - seq[i] for i in range(len(seq)-1)]
  return seq+[seq[-1]+d[0]] if set(d)=={0} else seq+[seq[-1]+n(d)[-1]]
[ print(sum([n(line[::p])[-1] for line in lines])) for p in [1,-1] ]

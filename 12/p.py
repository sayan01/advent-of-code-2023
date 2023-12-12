from re import compile as re
@__import__('functools').cache
def per(pat, *res, mat=0, i=0):
    if not res:
        return 1-("#" in pat)
    while(m:=res[0].search(pat[i:])) and "#" not in pat[:i+m.start()]:
      mat,i=mat+per(pat[i+m.end()-1:],*res[1:]),i+m.start()+1
    return mat
L,r = [[y.split(',') for y in x.split()] for x in open('input.txt')],'[.?][#?]{%s}[.?]'
[print(sum(per(f'.{"?".join(x*p)}.',*[re(r%z)for z in y*p])for x,y in L))for p in[1,5]]

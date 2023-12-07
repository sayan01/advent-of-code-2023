from sys import argv
input = argv[1] if len(argv) > 1 else 'input.txt'

with open(input) as ff:
    data = ff.read()

sections = data.split('\n\n')
seeds = sections[0].split(':')[-1].strip().split()
seeds = [int(x) for x in seeds]
sections = sections[1:]

for section in sections:
    section = [_.strip() for _ in section.split('\n') if ':' not in _ and _]
    newseeds = seeds.copy()
    for line in section:
        ds, ss, rl = [int(x) for x in line.split()]
        for i,seed in enumerate(seeds):
            if seed in range(ss, ss+rl):
                newseeds[i] = ds + seed - ss
    seeds = newseeds.copy()
print(min(seeds))


# Part 2
# seeds is actually pair of ranges (start, len)

with open(input) as ff:
    data = ff.read()

sections = data.split('\n\n')
seeds = sections[0].split(':')[-1].strip().split()
seeds = [int(x) for x in seeds]
sections = sections[1:]

srs = []
for i in range(0, len(seeds), 2):
    srs.append(range(seeds[i], seeds[i]+seeds[i+1]))

for section in sections:
    section = [_.strip() for _ in section.split('\n') if ':' not in _ and _]
    nsr = []
    for line in section:
        ds, ss, rl = [int(x) for x in line.split()]
        tsrs = srs.copy()
        for sr in tsrs:
            sourcerange = range(ss, ss+rl)
            # if sr totally outside sourcerange, continue
            if sr.stop < sourcerange.start or sr.start > sourcerange.stop:
                continue
            # if sr totally inside sourcerange, transform sr
            if sr.start >= sourcerange.start and sr.stop <= sourcerange.stop:
                nsr.append(range(ds + sr.start - ss, ds + sr.stop - ss))
                srs.remove(sr)
            # if sr partially inside sourcerange, split sr
            if sr.start < sourcerange.start and sr.stop > sourcerange.stop:
                nsr.append(range(ds, ds + rl))
                srs.remove(sr)
                srs.append(range(sr.start, ss))
                srs.append(range(sourcerange.stop, sr.stop))
            # if sr starts inside sourcerange, split sr
            if sr.start >= sourcerange.start and sr.stop > sourcerange.stop:
                nsr.append(range(ds + sr.start - ss, ds + rl))
                srs.remove(sr)
                srs.append(range(sourcerange.stop, sr.stop))
            # if sr ends inside sourcerange, split sr
            if sr.start < sourcerange.start and sr.stop <= sourcerange.stop:
                nsr.append(range(ds, ds + sr.stop - ss))
                srs.remove(sr)
                srs.append(range(sr.start, ss))
    srs.extend(nsr) # add the untransformed srs also

print(min(srs, key=lambda x: x.start).start)

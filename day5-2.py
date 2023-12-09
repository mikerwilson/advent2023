#!/usr/bin/env python3
from pprint import pprint
from collections import OrderedDict

# filename = "day5-test.txt"
filename = "day5-input.txt"

rawdata = open(filename, 'r').read()
rawchunks = rawdata.split("\n\n")
chunks = OrderedDict()
matchcache = {}

def translate(val, mapparts):
    result = None
    matched = False
    # pprint("mapparts: %s" % mapparts)
    for m in mapparts:
        # mapparts: d, s, l
        #   d-start s-start len
        d, s, l = m
        key = "%s-%s-%s-%s" % (d,s,l,val)
        if key in matchcache.keys():
            result = matchcache[key]
            matched = True
            pprint("hit!")
            break
        else:
            # too low for this map part
            # pprint("d: %s, s: %s, l: %s, val: %s" % (d,s,l,val))
            if val < s:
                continue
            # too high for this map part
            elif s + l < val:
                continue

            matched = True
            diff = d - s
            matchcache[key] = val + diff
            result = val + diff
            break

    if matched == False:
        result = val

    return result

# Parse the input file into a dict for easier processing
for chunk in rawchunks:
    key = chunk.split(":")[0].strip()
    valuestrings = [x.split(" ") for x in chunk.split(":")[1].strip().split('\n')]

    # convert everything to ints for later
    chunks[key] = [list(map(int, lst)) for lst in valuestrings]


locations = []
keys = [x for x in chunks.keys()]
keys.pop(0)
pprint("keys: %s" % keys)
seedlist = chunks['seeds'][0]
rangecache = {}
pprint("de-duping ranges...")
oldlens = 0
for i in range(0,len(seedlist),2):
    s = int(seedlist[i])
    l = int(seedlist[i+1])
    oldlens += l
    if s in rangecache.keys():
        rangecache[s] = max(rangecache[s],l)
    else:
        rangecache[s] = l
pprint("went from %s ranges to %s ranges" % (len(seedlist),len(rangecache)))
newlens = 0
for key in rangecache.keys():
    newlens += rangecache[key]

pprint("low number: %s" % min(rangecache.keys()))
pprint("total iterations went from %s to %s" % (oldlens,newlens))
pprint("processing iterations...")
for i in rangecache.keys():
    s = i
    l = rangecache[s]
    # pprint("s: %s, l: %s" % (s, l))
    for seed in range(s, s + l + 1):
        # print("seed: %s" % seed)
        value = seed
        for key in keys:
            mapbits = chunks[key]
            value = translate(value, mapbits)

        locations += [int(value)]
    lowest = min(locations)
    locations = [lowest]


# pprint("locations: %s" % locations)
lowest = min(locations)
print("lowest location: %s" % lowest)
#!/usr/bin/env python3
from pprint import pprint
from collections import OrderedDict

# filename = "day5-test.txt"
filename = "day5-input.txt"

rawdata = open(filename, 'r').read()
rawchunks = rawdata.split("\n\n")
chunks = OrderedDict()

def translate(val, mapparts):
    matched = False
    # pprint("mapparts: %s" % mapparts)
    for m in mapparts:
        # mapparts: d, s, l
        #   d-start s-start len
        d, s, l = m
        # too low for this map part
        # pprint("d: %s, s: %s, l: %s, val: %s" % (d,s,l,val))
        if val < s:
            continue
        # too high for this map part
        elif s + l < val:
            continue

        matched = True
        diff = d - s
        return val + diff

    if matched == False:
        return val


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
for seed in chunks['seeds'][0]:
    value = seed
    for key in keys:
        mapbits = chunks[key]
        value = translate(value, mapbits)

    locations += [int(value)]

pprint("locations: %s" % locations)
lowest = min(locations)
print("lowest location: %s" % lowest)
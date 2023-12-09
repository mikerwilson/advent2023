#!/usr/bin/env python3
from pprint import pprint
from collections import OrderedDict

# filename = "day6-test.txt"
filename = "day6-input.txt"

rawfile = open(filename, 'r').read()
rawdata = rawfile.split("\n")
rawtime = rawdata[0]
rawrecords = rawdata[1]
times = [y for y in [x for x in rawtime.split(':')[1].strip().split(" ")] if not y == '']
records = [y for y in [x for x in rawrecords.split(':')[1].strip().split(" ")] if not y == '']
pprint("times: %s, records: %s" % (times,records))

wincounts = []
# iterate through races
for i in range(0,len(times)):
    # pprint("Time: %s -> records: %s" % (times[i],records[i]))
    time = int(times[i])
    record = int(records[i])
    wins = []
    for hold in range(0,time):
        speed = hold
        dist = speed * (time - hold)
        if dist > record:
            wins += [dist]

    pprint("Race %s can be won %s different ways." % (i,len(wins)))
    wincounts += [len(wins)]

pprint("wins: %s" % wins)
total = 1
for win in wincounts:
    total = total * win

pprint("total: %s" % total)
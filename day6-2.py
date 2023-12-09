#!/usr/bin/env python3
from pprint import pprint

# filename = "day6-test.txt"
filename = "day6-input.txt"

rawfile = open(filename, 'r').read()
rawdata = rawfile.split("\n")
rawtime = rawdata[0]
rawrecords = rawdata[1]
time = "".join([y for y in [x for x in rawtime.split(':')[1].strip().split(" ")] if not y == ''])
record = "".join([y for y in [x for x in rawrecords.split(':')[1].strip().split(" ")] if not y == ''])
pprint("times: %s, records: %s" % (time,record))

wincounts = []
# iterate through races
time = int(time)
record = int(record)
wins = []
for hold in range(0,time):
    speed = hold
    dist = speed * (time - hold)
    if dist > record:
        wins += [dist]

pprint("Race can be won %s different ways." % (len(wins)))
wincounts += [len(wins)]

# pprint("wins: %s" % wins)
pprint("calculating wins...")
total = 1
for win in wincounts:
    total = total * win

pprint("total: %s" % total)
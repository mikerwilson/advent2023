#!/usr/bin/env python3
from pprint import pprint

# filename = "day4-test.txt"
filename = "day4-input.txt"
pointtable = {
    0:0,
    1:1,
    2:2,
    3:4,
    4:8,
    5:16,
    6:32,
    7:64,
    8:128,
    9:256,
    10:512
}
rawdata = open(filename, 'r').read()
cards = rawdata.split("\n")
total = 0

for card in cards:
    name = card.split(":")[0]
    winningraw = card.split("|")[0].split(":")[1].strip().split(" ")
    playsraw = card.split("|")[1].strip().split(" ")
    winning = [n for n in winningraw if not n == '']
    plays = [n for n in playsraw if not n == '']
    matches = [x for x in plays if x in winning]
    if len(matches) in pointtable.keys():
        points = pointtable[len(matches)]
    else:
        points = 0

    total += points
    print("card: '%s', winning: '%s', plays: '%s', matches: %s, points: %s" % (name, winning, plays, len(matches), points))
    # pprint("card: '%s', matches: %s, points: %s" % (name, matches, points))

pprint("Total: %s" % (total))
#!/usr/bin/env python3
from pprint import pprint

# filename = "day2-test.txt"
filename = "day2-input.txt"

rawdata = open(filename, 'r').read()
games = rawdata.split("\n")

powervalues = []

for game in games:

    if game.strip() == '':
        continue

    maxcubes = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    gameid = game.split(':')[0].split(' ')[-1]
    plays = game.split(':')[1].strip().split(';')
    for play in plays:
        # print("plays: '%s'" % plays)
        parts = play.split(",")
        for part in parts:
            part = part.strip()
            number, color = part.split(' ')
            number = int(number)
            if color in maxcubes.keys():
                maxcubes[color] = max(maxcubes[color], number)

    power = 1
    for i in maxcubes:
        power = power * maxcubes[i]

    powervalues += [power]
    print('maxcubes: %s, power: %s' % (maxcubes,power))

total = 0
for value in powervalues:
    total += int(value)

print("Total: %s" % total)
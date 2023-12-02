#!/usr/bin/env python3
from pprint import pprint

# filename = "day2-test.txt"
filename = "day2-input.txt"

rawdata = open(filename, 'r').read()
games = rawdata.split("\n")

# 12 red cubes, 13 green cubes, and 14 blue cubes?
maxred = 12
maxgreen = 13
maxblue = 14

maxcubes = {
    "red": 12,
    "green": 13,
    "blue": 14
}
possiblegames = []
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red

for game in games:
    if game.strip() == '':
        continue
    gameid = game.split(':')[0].split(' ')[-1]
    plays = game.split(':')[1].strip().split(';')
    possible = True
    for play in plays:
        # print("plays: '%s'" % plays)
        parts = play.split(",")
        for part in parts:
            part = part.strip()
            number, color = part.split(' ')
            number = int(number)
            if color in maxcubes.keys():
                if number > maxcubes[color]:
                    possible = False
                    continue
    if possible:
        possiblegames += [gameid]

print(possiblegames)
total = 0
for value in possiblegames:
    total += int(value)

print("Total: %s" % total)
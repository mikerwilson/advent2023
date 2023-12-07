#!/usr/bin/env python3
from pprint import pprint
import copy

# filename = "day4-test.txt"
filename = "day4-input.txt"
pointtable = {
    0: 0,
    1: 1,
    2: 2,
    3: 4,
    4: 8,
    5: 16,
    6: 32,
    7: 64,
    8: 128,
    9: 256,
    10: 512
}
rawdata = open(filename, 'r').read()
rawcards = rawdata.split("\n")
total = 0

cardstack = []
cardcounts = {}

class Card(object):
    def __init__(self, card):
        self.rawcard = card
        self.name = card.split(":")[0]
        self.number = self.name.split(" ")[-1]
        self.count = 1
        self._getWins()

    def _getWins(self):
        winningraw = self.rawcard.split("|")[0].split(":")[1].strip().split(" ")
        playsraw = self.rawcard.split("|")[1].strip().split(" ")
        winning = [n for n in winningraw if not n == '']
        plays = [n for n in playsraw if not n == '']
        self.matches = [x for x in plays if x in winning]
        self.points = len(self.matches)

    def add(self):
        self.count += 1

# Generate our cardstack
for line in rawcards:
    thiscard = Card(line)
    cardcounts[int(thiscard.number)] = 1
    cardstack += [Card(line)]

for card in cardstack:
    if card.points > 0:
        number = card.number
        pprint("Card number: %s, Count: %s" % (number,len(cardstack)))
        i = int(card.number) - 1
        points = card.points
        name = card.name
        # pprint("%s has %s points.  Making copies of the next %s cards." % (name, points, points))
        for p in range(i + 1, i + points + 1):
            copyname = cardstack[p].name
            # pprint("Copying %s, current card count: %s" % (copyname, len(cardstack)))
            cardcopy = copy.copy(cardstack[p])
            cardstack += [cardcopy]
            # pprint("New card count: %s" % (len(cardstack)))

total = 0
total += len(cardstack)
# for card in cardstack:
#     total += card.count

pprint("Total: %s" % (total))

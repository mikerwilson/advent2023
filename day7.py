#!/usr/bin/env python3
from pprint import pprint

filename = "day7-test.txt"
# filename = "day7-input.txt"

rawfile = open(filename, 'r').read()
rawhands = [x.split(" ") for x in rawfile.split("\n")]
hands = []
# Added joker as a 0-point card since I will use index position as card point value.
cardlist = ['','2','3','4','5','6','7','8','9','T','J','Q','K','A']

# Value order:
# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456

class Hand(object):
    def __init__(self,data):
        self.score = 0
        self.type = None
        self.cardvalues = 0
        self.cards = data[0]
        self.bet = data[1]
        self.cardcounts = {}
        for c in cardlist:
            self.cardcounts[c] = 0

        self._calculatescore()

    def _calculatescore(self):
        #  100000
        #  TTTVVV
        pprint("cards: %s" % self.cards)

        # Add up raw values
        for i in range(len(self.cards)):
            cardname = self.cards[i]
            if cardname in self.cardcounts.keys():
                self.cardcounts[cardname] += 1
            self.cardvalues += cardlist.index(cardname)
        self.score = self.cardvalues

        # pprint("card counts: %s" % self.cardcounts)
        # Test for 4 or 5 of a kind
        for card in self.cardcounts.keys():
            if self.cardcounts[card] == 5:
                self.score += 10000000
            elif self.cardcounts[card] == 4:
                self.score += 1000000
            elif self.cardcounts[card] == 3:
                # test for full house, or it's 3 of a kind
                fullhouse = False
                for others in self.cardcounts.keys():
                    if self.cardcounts[others] == 2:
                        fullhouse = True
                if fullhouse:
                    self.score += 100000
                else:
                    self.score += 10000
            elif self.cardcounts[card] == 2:
                pprint("found a pair in hand %s" % self.cards)
                self.score += 1000

def bubblesort(elements):
    swapped = False
    for n in range(len(elements) - 1, 0, -1):
        for i in range(n):
            a = int(elements[i].score)
            b = int(elements[i + 1].score)
            if a > b:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            return

pprint('hands: %s' % rawhands)

for play in rawhands:
    hands += [Hand(play)]
pprint("----> pre sort:")
for hand in hands:
    pprint('hand: %s, score: %s' % (hand.cards,hand.score))

pprint("----> post sort:")
bubblesort(hands)
for hand in hands:
    pprint('hand: %s, score: %s, bet: %s' % (hand.cards,hand.score,hand.bet))

globalwinnings = 0
for i in range(len(hands)):
    globalwinnings += int(hands[i].bet) * (i + 1)

pprint("global winnings: %s" % globalwinnings)
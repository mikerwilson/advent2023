#!/usr/bin/env python3
from pprint import pprint

# filename = "day7-test.txt"
filename = "day7-input.txt"

rawfile = open(filename, 'r').read()
rawhands = [x.split(" ") for x in rawfile.split("\n")]

def handtype(hand: str) -> int:
    ordered_types = [
        [5],        # Five of a kind
        [4,1],      # Four of a kind
        [3,2],      # Full house
        [3,1,1],    # Three of a kind
        [2,2,1],    # Two pair
        [2,1,1,1],  # One pair
        [1,1,1,1,1] # High card
    ]
    label_counts = [hand.count(card) for card in set(hand)]
    label_counts.sort(reverse=True)
    return ordered_types.index(label_counts)

def cards_as_int(hand: str) -> tuple:
    ordered_labels = 'AKQJT98765432'
    return (ordered_labels.index(card) for card in hand)

hands = []
for hand, bid in rawhands:
    encoded_hand = (
        handtype(hand),
        *cards_as_int(hand),
        int(bid)
    )
    hands.append(encoded_hand)

hands.sort(reverse=True)
winnings = sum(rank * hand[-1] for rank, hand in enumerate(hands, start=1))

print(winnings)
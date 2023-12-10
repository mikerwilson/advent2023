#!/usr/bin/env python3
from pprint import pprint

# filename = "day9-test.txt"
filename = "day9-input.txt"

rawfile = open(filename, 'r').read()
rawsequences = [n.split() for n in rawfile.split("\n")]

sequences = []
for sequence in rawsequences:
    sequences += [[int(x) for x in sequence]]


def getdifferences(elements) -> list:
    diffs = []
    for s in range(0, len(elements) - 1):
        left = int(elements[s])
        right = int(elements[s + 1])
        diffs += [right - left]
    return diffs

newvalues = 0
for sequence in sequences:
    stack = []
    stack += [0] # this is a hack for an off by one error.  TODO: make this not a thing.
    stack += [sequence]
    # Create our inverse pyramid
    while True:
        stack += [getdifferences(stack[-1])]
        # pprint("last set: %s" % (set(stack[-1])))
        if str(set(stack[-1])) == "{0}":
            pprint("stack: %s, setlen: %s" % (stack, len(set(stack[-1]))))
            break

    for i in range(len(stack) - 2,0,-1):
        last = stack[i + 1]
        this = stack[i]
        this += [this[-1] + last[-1]]
        # pprint("stackitem %s: %s" % (i, stack[i]))

    for i in range(len(stack) - 1,0,-1):
        pprint("stackitem %s: %s" % (i, stack[i]))

    pprint("-" * 80)
    pprint("newest value: %s" % stack[1][-1])
    newvalues += stack[1][-1]

pprint(newvalues)
#!/usr/bin/env python3
from pprint import pprint

# filename = "day3-test.txt"
filename = "day3-input.txt"

rawdata = open(filename, 'r').read()
grid = rawdata.split("\n")

# symbols are anything except '.'
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

pprint(grid)

max_x = len(grid) - 1
max_y = len(grid[0])

pprint("max_x: %s, max_y: %s" % (max_x, max_y))
cursor = [0, 0]
# cursor = [2, 9]


def readcursor ():
    # pprint("attempting to read: %s" % cursor)
    return grid[cursor[0]][cursor[1]]

def isSymbol (char):
    # pprint("isSymbol -> '%s'" % (char))
    return char not in numbers and not char == '.'

def isNumber (char):
    # pprint("isNumber -> '%s'" % (char))
    return char in numbers

def nextpos ():
    global cursor, max_x, max_y
    result = True
    # advance the cursor to the next position
    # cursor [x, y]
    # pprint("Old cursor: %s" % cursor)
    x = cursor[0]
    y = cursor[1]
    # if we've reached the end of the line, then go to the start of the next line
    y += 1

    if y > max_y - 1:
        x += 1
        y = 0

    if x > max_x:
        x = 0
        y = 0
        result = False

    # pprint("New cursor: %s" % cursor)
    cursor = [x, y]
    return result

def getTouching (pos):
    # checks to see if this digit is touching a symbol
    global cursor, max_x, max_y
    result = []
    cx = pos[0]
    cy = pos[1]
    low_x = max(0, cx - 1)
    high_x = min(max_x + 1, cx + 2)
    low_y = max(0, cy - 1)
    high_y = min(max_y, cy + 2)
    # pprint("cx: %s, cy: %s ; low_x: %s, high_x: %s ; low_y: %s, high_y: %s" % (cx, cy, low_x, high_x, low_y, high_y))
    for x in range(low_x, high_x):
        for y in range(low_y, high_y):
            result += [[x, y]]

    return result

pprint("Cursor: %s -> %s" % (cursor, readcursor()))
pprint("isSymbol: %s, isNumber: %s" % (isSymbol(readcursor()), isNumber(readcursor())))

inNumber = False

# collect all symbol coords
symbols = []
while True:
    if isSymbol(readcursor()):
        # pprint("found symbol!")
        x = cursor[0]
        y = cursor[1]
        symbols += [[x, y]]

    if not nextpos():
        break


pprint("Symbol coords: %s" % symbols)
# Expand our list of positions to include all adjacent gridpoints

keeplist = []
# expand our list of symbol locations to include all adjacent touching ones
for pos in symbols:
    keeplist += getTouching(pos)

# pprint("keeplist: %s" % keeplist)

keep = False
assembler = ''
keepers = []
cursor = [0, 0]
wasnumber = False
notdone = True
while notdone:
    if isNumber(readcursor()):
        wasnumber = True
        assembler += readcursor()
        if cursor in keeplist:
            keep = True

    else:
        if wasnumber and keep:
            keepers += [str(assembler)]
        assembler = ''
        keep = False
        wasnumber = False

    notdone = nextpos()


pprint("keepers: %s" % keepers)
total = 0
for item in keepers:
    total += int(item)

pprint("Total: %s" % total)
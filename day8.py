#!/usr/bin/env python3
from pprint import pprint

# filename = "day8-test.txt"
filename = "day8-input.txt"
step = 0
stepcount = 0
dirs = {
    'R':1,
    'L':0
}
def nextstep():
    global step
    step += 1
    if step >= len(steps):
        step = 0
    return step

start = 'AAA'
end = 'ZZZ'
rawfile = open(filename, 'r').read()
steps = list(rawfile.split("\n\n")[0])
rawnetwork = [n.split(" = ") for n in rawfile.split("\n\n")[1].split("\n")]
network = {}
pprint("steps: %s" % steps)
for node, elements in rawnetwork:
    network[node] = elements.split("(")[1].split(")")[0].split(", ")
    pprint("node: %s, elements: %s" % (node,network[node]))

loc = start
while loc != end:
    node = network[loc]
    dir = steps[step]
    pprint("node: %s, step %s: dir:%s" % (loc,step,dir))
    loc = node[dirs[dir]]
    stepcount += 1
    nextstep()

pprint("stepcount: %s" % stepcount)


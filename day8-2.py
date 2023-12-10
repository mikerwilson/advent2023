#!/usr/bin/env python3
from pprint import pprint
import math

# filename = "day8-2-test.txt"
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

def notdone():
    global locs
    result = False
    for loc in locs:
        if not loc.endswith('Z'):
            result = True
    return result

start = 'A'
end = 'Z'
rawfile = open(filename, 'r').read()
steps = list(rawfile.split("\n\n")[0])
rawnetwork = [n.split(" = ") for n in rawfile.split("\n\n")[1].split("\n")]
network = {}
pprint("steps: %s" % steps)
for node, elements in rawnetwork:
    network[node] = elements.split("(")[1].split(")")[0].split(", ")
    pprint("node: %s, elements: %s" % (node,network[node]))

locs = []
for key in network.keys():
    if key.endswith('A'):
        locs += [key]

pprint("starting locs: %s" % locs)

counters = []
for loc in locs:
    stepcount = 0
    while not loc.endswith("Z"):
        node = network[loc]
        dir = steps[step]
        # pprint("node: %s, step %s: dir:%s" % (loc, step, dir))
        loc = node[dirs[dir]]
        stepcount += 1
        nextstep()
    counters.append(stepcount)

answer = math.lcm(*counters)
pprint("stepcount: %s" % answer)


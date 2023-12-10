#!/usr/bin/env python3
from pprint import pprint

filename = "day8-test.txt"
# filename = "day8-input.txt"

rawfile = open(filename, 'r').read()
steps = set(rawfile.split("\n\n")[0])
rawnetwork = [n.split(" = ") for n in rawfile.split("\n\n")[1].split("\n")]

pprint(rawnetwork)
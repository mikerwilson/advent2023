#!/usr/bin/env python3
from pprint import pprint

# filename = "day9-test.txt"
filename = "day9-input.txt"

rawfile = open(filename, 'r').read()
rawsequences = [n.split() for n in rawfile.split("\n")]
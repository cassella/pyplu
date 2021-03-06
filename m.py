#!/usr/bin/env python

import argparse

import mylib

class testobj:
    def __init__(self, a_str, a_strtwo, an_int, an_inttwo):
        self.a_str = a_str
        self.a_strtwo = a_strtwo
        self.an_int = an_int
        self.an_inttwo = an_inttwo

testobjs = [
    testobj("flumpf", "whimper", 42, 4242),
    testobj("MIMSY", "GIMBLE", 77, 7777),
]

parser = argparse.ArgumentParser(description="oh hi")

mylib.add_args(parser)

args = parser.parse_args()

hdr = ""
for ro in args.report:
    hdr += ro.header()
print(hdr)

for o in testobjs:
    s = ""
    for ro in args.report:
        s += ro.show(o)
    print(s)

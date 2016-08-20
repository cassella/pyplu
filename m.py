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

for o in testobjs:
    for ro in args.report:
        ro.show(o)

#!/usr/bin/env python

import argparse

import mylib


parser = argparse.ArgumentParser(description="oh hi")

mylib.add_args(parser)

args = parser.parse_args()

for (r,f) in args.report:
    r("singleton", f)

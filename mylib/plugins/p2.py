#!/usr/bin/env python

from mylib import Plugin

def add_p2_args(parser):
    parser.add_argument("--p2")


Plugin("p2", add_p2_args)

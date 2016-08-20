#!/usr/bin/env python

from mylib import Plugin

def add_p1_args(parser):
    parser.add_argument("--p1")

Plugin("p1", add_p1_args)

#!/usr/bin/env python

myplugins = {}

class Plugin:
    def __init__(self, name, add_args):
        self.name = name
        self.add_args = add_args
        myplugins[name] = self

def add_args(parser):
    for p in myplugins.values():
        p.add_args(parser)

from mylib.plugins import *

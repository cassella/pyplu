#!/usr/bin/env python

from mylib import Plugin
from mylib.objects import *

default_p1_fielddescs = ["a_str", "an_int"]

p1 = reportobj("p1", default_p1_fielddescs)

field(p1, "a_str", "a_str", "STR", 8, get_a_str)
field(p1, "a_strtwo", "a_strtwo", "STR2", 8, get_a_str)
field(p1, "an_int", "an_int", "I", 2, get_an_int)
field(p1, "an_inttwo", "an_inttwo", "INT2", 4, get_an_int)
field(p1, "an_inttwo-hex", "an_inttwo", "INT2", 4, get_an_int_hex)

def add_p1_args(parser):
    return p1.add_args(parser)

Plugin("p1", add_p1_args)

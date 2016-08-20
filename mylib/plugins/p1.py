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

default_p1_fields = p1.descs_to_fields(default_p1_fielddescs)

def add_reportobj_args(parser, ro, default_fields):
    def add_ro_fields(arg):
        return ro.add_fields(arg)

    def replace_ro_fields(arg):
        return (ro, ro.descs_to_fields(arg.split(",")))

    parser.add_argument("--" + ro.name, action="append_const", dest="report",
                        help="show {ro} default fields".format(ro=ro.name),
                        const=(ro, default_p1_fields))
    parser.add_argument("--" + ro.name + "+", action="append", dest="report",
                        help="show {ro} with additional fields".format(ro=ro.name),
                        metavar="EXTRA",
                        type=add_ro_fields)
    parser.add_argument("--" + ro.name + "-", action="append", dest="report",
                        help="show {ro} with only these fields".format(ro=ro.name),
                        metavar="FIELDS",
                        type=replace_ro_fields)

def add_p1_args(parser):
    return add_reportobj_args(parser, p1, default_p1_fields)

Plugin("p1", add_p1_args)

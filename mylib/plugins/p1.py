#!/usr/bin/env python

from mylib import Plugin
from mylib.objects import *


default_p1_fielddescs = ["a_str", "an_int"]

class reportobj:
    def __init__(self, name):
        self.fields = {}
        self.name = name

    def desc_to_field(self, desc):
        return self.fields[desc]

    def descs_to_fields(self, descs):
        return map(self.desc_to_field, descs)

    def show(self, obj, fields):
        for f in fields:
            print f.getstr(obj, f.name),
        print

    def add_fields(self, arg):
        fieldnames = default_p1_fielddescs + arg.split(",")
        return (self, self.descs_to_fields(fieldnames))

p1 = reportobj("p1")

def add_p1_fields(arg):
    return p1.add_fields(arg)


field(p1.fields, "a_str", "a_str", "STR", 8, get_a_str)
field(p1.fields, "a_strtwo", "a_strtwo", "STR2", 8, get_a_str)
field(p1.fields, "an_int", "an_int", "I", 2, get_an_int)
field(p1.fields, "an_inttwo", "an_inttwo", "INT2", 4, get_an_int)
field(p1.fields, "an_inttwo-hex", "an_inttwo", "INT2", 4, get_an_int_hex)

default_p1_fields = p1.descs_to_fields(default_p1_fielddescs)

def replace_p1_fields(arg):
    return (p1, p1.descs_to_fields(arg.split(",")))

def add_p1_args(parser):
    parser.add_argument("--p1", action="append_const", dest="report",
                        help="show p1 default fields",
                        const=(p1, default_p1_fields))
    parser.add_argument("--p1+", action="append", dest="report",
                        help="show p1 with additional fields",
                        metavar="EXTRA",
                        type=add_p1_fields)
    parser.add_argument("--p1-", action="append", dest="report",
                        help="show p1 with only these fields",
                        metavar="FIELDS",
                        type=replace_p1_fields)

Plugin("p1", add_p1_args)

#!/usr/bin/env python

from mylib import Plugin

class field:
    def __init__(self, fields, desc, name, hdrname, width, getstr):
        self.name = name
        self.desc = desc
        self.hdrname = hdrname
        self.width = width
        self.getstr = getstr
        fields[desc] = self

def get_a_str(p1, name):
    return p1.__dict__[name]

def get_an_int(p1, name):
    return str(p1.__dict__[name])

def get_an_int_hex(p1, name):
    return "{:x}".format(p1.__dict__[name])

p1_fields = {}

field(p1_fields, "a_str", "a_str", "STR", 8, get_a_str)
field(p1_fields, "a_strtwo", "a_strtwo", "STR2", 8, get_a_str)
field(p1_fields, "an_int", "an_int", "I", 2, get_an_int)
field(p1_fields, "an_inttwo", "an_inttwo", "INT2", 4, get_an_int)
field(p1_fields, "an_inttwo-hex", "an_inttwo", "INT2", 4, get_an_int_hex)

def desc_to_field(desc):
    return p1_fields[desc]

def descs_to_fields(descs):
    return map(desc_to_field, descs)

def show_p1(p1, fields):
    for f in fields:
        print f.getstr(p1, f.name),
    print

default_p1_fielddescs = ["a_str", "an_int"]
default_p1_fields = descs_to_fields(default_p1_fielddescs)



def add_p1_fields(arg):
    fieldnames = default_p1_fielddescs + arg.split(",")
    return (show_p1, descs_to_fields(fieldnames))

def replace_p1_fields(arg):
    return (show_p1, descs_to_fields(arg.split(",")))

def add_p1_args(parser):
    parser.add_argument("--p1", action="append_const", dest="report",
                        help="show p1 default fields",
                        const=(show_p1, default_p1_fields))
    parser.add_argument("--p1+", action="append", dest="report",
                        help="show p1 with additional fields",
                        metavar="EXTRA",
                        type=add_p1_fields)
    parser.add_argument("--p1-", action="append", dest="report",
                        help="show p1 with only these fields",
                        metavar="FIELDS",
                        type=replace_p1_fields)

Plugin("p1", add_p1_args)

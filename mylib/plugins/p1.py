#!/usr/bin/env python

from mylib import Plugin

class field:
    def __init__(self, fields, name, hdrname, width, getstr):
        self.name = name
        self.hdrname = hdrname
        self.width = width
        self.getstr = getstr
        fields[name] = self

def get_a_str(p1, name):
    return p1.__dict__[name]

def get_an_int(p1, name):
    return str(p1.__dict__[name])

p1_fields = {}

field(p1_fields, "a_str", "STR", 8, get_a_str)
field(p1_fields, "a_strtwo", "STR2", 8, get_a_str)
field(p1_fields, "an_int", "I", 2, get_an_int)
field(p1_fields, "an_inttwo", "INT2", 4, get_an_int)

default_p1_fieldnames=["a_str", "an_int"]

def fieldname_to_field(fieldname):
    return p1_fields[fieldname]

def fieldnames_to_fields(fieldnames):
    return map(fieldname_to_field, fieldnames)

def show_p1(p1, fields):
    for f in fields:
        print f.getstr(p1, f.name),
    print


def add_p1_fields(arg):
    fieldnames = default_p1_fieldnames + arg.split(",")
    return (show_p1, fieldnames_to_fields(fieldnames))

def replace_p1_fields(arg):
    return (show_p1, fieldnames_to_fields(arg.split(",")))

def add_p1_args(parser):
    parser.add_argument("--p1", action="append_const", dest="report",
                        help="show p1 default fields",
                        const=(show_p1,fieldnames_to_fields(default_p1_fieldnames)))
    parser.add_argument("--p1+", action="append", dest="report",
                        help="show p1 with additional fields",
                        metavar="EXTRA",
                        type=add_p1_fields)
    parser.add_argument("--p1-", action="append", dest="report",
                        help="show p1 with only these fields",
                        metavar="FIELDS",
                        type=replace_p1_fields)

Plugin("p1", add_p1_args)

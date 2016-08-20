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

p1_fields = {}

field(p1_fields, "a_str", "STR", 8, get_a_str)


default_p1_fields=[p1_fields["a_str"]]

def show_p1(p1, fields):
    for f in fields:
        print f.getstr(p1, f.name)


def add_p1_args(parser):
    parser.add_argument("--p1", action="append_const", dest="report",
                        const=(show_p1,default_p1_fields))

Plugin("p1", add_p1_args)

#!/usr/bin/env python

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

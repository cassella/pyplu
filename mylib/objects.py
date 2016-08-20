#!/usr/bin/env python

class field:
    def __init__(self, reportobj, desc, name, hdrname, width, getstr):
        self.name = name
        self.desc = desc
        self.hdrname = hdrname
        self.width = width
        self.getstr = getstr
        reportobj.fields[desc] = self

def get_a_str(p1, name):
    return p1.__dict__[name]

def get_an_int(p1, name):
    return str(p1.__dict__[name])

def get_an_int_hex(p1, name):
    return "{:x}".format(p1.__dict__[name])


class reportobj:
    def __init__(self, name, default_fielddescs):
        self.fields = {}
        self.name = name
        self.default_fielddescs = default_fielddescs

    def desc_to_field(self, desc):
        return self.fields[desc]

    def descs_to_fields(self, descs):
        return map(self.desc_to_field, descs)

    def show(self, obj, fields):
        for f in fields:
            print f.getstr(obj, f.name),
        print

    def add_fields(self, arg):
        fieldnames = self.default_fielddescs + arg.split(",")
        return (self, self.descs_to_fields(fieldnames))

    def add_args(self, parser):
        # closures so we can pass these as type=<> params to argparse
        def add_ro_fields(arg):
            return self.add_fields(arg)

        def replace_ro_fields(self, arg):
            return (self, self.descs_to_fields(arg.split(",")))

        parser.add_argument("--" + self.name, action="append_const", dest="report",
                            help="show {ro} default fields".format(ro=self.name),
                            const=(self, self.default_fields))
        parser.add_argument("--" + self.name + "+", action="append", dest="report",
                            help="show {ro} with additional fields".format(ro=self.name),
                            metavar="EXTRA",
                            type=add_ro_fields)
        parser.add_argument("--" + self.name + "-", action="append", dest="report",
                            help="show {ro} with only these fields".format(ro=self.name),
                            metavar="FIELDS",
                            type=replace_ro_fields)

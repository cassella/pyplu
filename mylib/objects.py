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


class objreporter:
    def __init__(self, ro, fields):
        self.ro = ro
        self.fields = fields

    def show(self, obj):
        for f in self.fields:
            print f.getstr(obj, f.name),
        print

class reportobj:
    def __init__(self, name, default_fielddescs):
        self.fields = {}
        self.name = name
        self.default_fielddescs = default_fielddescs

    def desc_to_field(self, desc):
        return self.fields[desc]

    def descs_to_fields(self, descs):
        return map(self.desc_to_field, descs)

    def report_default_fielddescs(self):
        return objreporter(self, self.descs_to_fields(self.default_fielddescs))
    def report_extra_fielddescs(self, arg):
        fielddescs = self.default_fielddescs + arg.split(",")
        return objreporter(self, self.descs_to_fields(fielddescs))
    def report_specific_fielddescs(self, arg):
        fielddescs = arg.split(",")
        return objreporter(self, self.descs_to_fields(fielddescs))

    def add_args(self, parser):
        # closures so we can pass these as type=<> params to argparse
        def add_ro_fields(arg):
            return self.report_extra_fielddescs(arg)
        def replace_ro_fields(arg):
            return self.report_specific_fielddescs(arg.split(","))
        def report_default_fields():
            return self.report_default_fielddescs()

        parser.add_argument("--" + self.name, action="append_const", dest="report",
                            help="show {ro} default fields".format(ro=self.name),
                            const=report_default_fields())
        parser.add_argument("--" + self.name + "+", action="append", dest="report",
                            help="show {ro} with additional fields".format(ro=self.name),
                            metavar="EXTRA",
                            type=add_ro_fields)
        parser.add_argument("--" + self.name + "-", action="append", dest="report",
                            help="show {ro} with only these fields".format(ro=self.name),
                            metavar="FIELDS",
                            type=replace_ro_fields)

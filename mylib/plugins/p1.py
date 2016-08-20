#!/usr/bin/env python

from mylib import Plugin


def default_p1_formatter(p1):
    pass

def show_p1(addr, formatter):
    print "{addr} as a p1".format(addr=addr)


def add_p1_args(parser):
    parser.add_argument("--p1", action="append_const", dest="report",
                        const=(show_p1,default_p1_formatter))

Plugin("p1", add_p1_args)

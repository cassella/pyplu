#!/usr/bin/env python

from mylib import Plugin

def default_p2_formatter(p2):
    pass

def show_p2(addr, formatter):
    print "{addr} as a p2".format(addr=addr)


def add_p2_args(parser):
    parser.add_argument("--p2", action="append_const", dest="report",
                        const=(show_p2,default_p2_formatter))


Plugin("p2", add_p2_args)

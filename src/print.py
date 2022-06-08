# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdout

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)


def colorable(stream):
    if not (hasattr(stream, "isatty") and stream.isatty):
        return False
    try:
        from curses import setupterm, tigetnum
        setupterm()
        return tigetnum("colors") > 2
    except:
        return False


colorable = colorable(stdout)


def printf(text, colour=WHITE):
    if colorable:
        seq = "\x1b[1;%dm" % (30 + colour) + text + "\x1b[0m"
        stdout.write(seq)
    else:
        stdout.write(text)

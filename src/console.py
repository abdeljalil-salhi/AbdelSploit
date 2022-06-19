# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#    _____ ___.        .___     .__    _________      .__         .__  __
#   /  _  \\_ |__    __| _/____ |  |  /   _____/_____ |  |   ____ |__|/  |_
#  /  /_\  \| __ \  / __ |/ __ \|  |  \_____  \\____ \|  |  /  _ \|  \   __\
# /    |    \ \_\ \/ /_/ \  ___/|  |__/        \  |_> >  |_(  <_> )  ||  |
# \____|__  /___  /\____ |\___  >____/_______  /   __/|____/\____/|__||__|
#         \/    \/      \/    \/             \/|__|        © abdeeels 2022

from src.print import *
from src.utilities import banner, cls
from src.abdelsploit import __init__, _quit

from argparse import ArgumentParser

windows = False
try:
    from gnureadline import parse_and_bind, set_completer
except:
    windows = True
    from pyreadline import Readline


class Console:
    def __init__(self):
        self.commands = {
            "menu": __init__,
            "list": self.cmdlist,
            "help": self.cmdlist,
            "quit": _quit,
            "exit": _quit,
            "myip": self.__init__,
            "ip": self.__init__,
            "mydns": self.__init__,
            "dns": self.__init__
        }

        cls()
        banner()
        printf("Type 'list' to show all available commands.\n")
        self.main()

    def autocomplete(self, text, state):
        options = [i for i in self.commands if i.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None

    def cmdlist(self):
        cmdlist = {
            "myip": "Get your IP address infos\n",
            "ip": "Get target IP address infos\n",
            "mydns": "Get your DNS infos\n",
            "dns": "Get target DNS infos\n",
        }
        keys = cmdlist.keys()
        for key in keys:
            printf(f"{key}\t\t", BLUE)
            printf(f"{cmdlist[key]}\n")

    def main(self):
        if windows:
            Readline().parse_and_bind("tab: complete")
            Readline().set_completer(self.autocomplete)
        else:
            parse_and_bind("tab: complete")
            set_completer(self.autocomplete)

        parser = ArgumentParser(
            description="AbdelSploit is your new favorite hacking tool.")
        parser.add_argument("target", type=str, help="target")
        parser.add_argument(
            "-j", "--json", help="save commands output as JSON file", action="store_true")
        parser.add_argument(
            "-c", "--command", help="run in single command mode & execute provided command", action="store")

        args = parser.parse_args()

        while True:
            if args.command:
                cmd = args.command
                _cmd = self.commands.get(args.command)
            else:
                if windows:
                    Readline().parse_and_bind("tab: complete")
                    Readline().set_completer(self.autocomplete)
                else:
                    parse_and_bind("tab: complete")
                    set_completer(self.autocomplete)

                printf("$~> ")
                cmd = input("")
                _cmd = self.commands.get(cmd)

            if _cmd:
                _cmd()
            elif cmd == "":
                printf("")
            else:
                printf("Unknown command. type 'list' to get help.\n", RED)

            if args.command:
                break

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
from src.abdelsploit import __init__
from src.modules.igathering import *


class Console:
    def __init__(self):
        self.commands = {
            "menu": self.menu,
            "list": self.cmdlist,
            "help": self.cmdlist,
            "quit": self._quit,
            "exit": self._quit,
            "myip": MyIP(),
            "ip": self.__init__,
            "mydns": self.__init__,
            "dns": self.__init__
        }

        cls()
        banner()
        printf("Type 'list' to show all available commands.\n\n")
        self.main()

    def autocomplete(self, text, state):
        options = [i for i in self.commands if i.startswith(text)]
        if state < len(options):
            return options[state]
        else:
            return None

    def cmdlist(self):
        cmdlist = {
            "myip":     "Get your IP address infos",
            "ip":       "Get target IP address infos",
            "mydns":    "Get your DNS infos",
            "dns":      "Get target DNS infos",
        }
        keys = cmdlist.keys()
        for key in keys:
            printf(f"{key}\t\t", BLUE)
            printf(f"{cmdlist[key]}\n")

    def main(self):
        while True:
            printf("$~> ")
            x = str(input("")).lower()
            _cmd = self.commands.get(x.split(" ")[0])
            if _cmd:
                _cmd()
            else:
                printf("Unknown command\n")

    def menu(self):
        pass

    def _quit(self, text="See you soon!"):
        printf(f"\n{text}")
        exit(0)

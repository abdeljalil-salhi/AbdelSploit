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
from src.abdelsploit import AbdelSploit


class Console:
    def __init__(self):
        self.windows = False
        self.commands = {
            "menu": AbdelSploit.__init__,
            "list": self.cmdlist,
            "help": self.cmdlist,
            "quit": AbdelSploit._quit,
            "exit": AbdelSploit._quit,
            "myip": self.__init__,
            "ip": self.__init__,
            "mydns": self.__init__,
            "dns": self.__init__
        }

        try:
            import gnureadline
        except:
            self.windows = True
            import pyreadline

        cls()
        banner()
        printf("Type 'list' to show all available commands.\n")

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

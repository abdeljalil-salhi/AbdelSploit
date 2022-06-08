# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#    _____ ___.        .___     .__    _________      .__         .__  __
#   /  _  \\_ |__    __| _/____ |  |  /   _____/_____ |  |   ____ |__|/  |_
#  /  /_\  \| __ \  / __ |/ __ \|  |  \_____  \\____ \|  |  /  _ \|  \   __\
# /    |    \ \_\ \/ /_/ \  ___/|  |__/        \  |_> >  |_(  <_> )  ||  |
# \____|__  /___  /\____ |\___  >____/_______  /   __/|____/\____/|__||__|
#         \/    \/      \/    \/             \/|__|        © abdeeels 2022

from src.art import *
from src.print import *
from src.utilities import *
from src.igathering import *
from src.vanalysis import *

from sys import exit


class AbdelSploit:
    def __init__(self):
        self.choice = None
        self.menu()

    def menu(self):
        cls()
        banner()
        printf("[1] Information Gathering\t\t[A] YouTube\n")
        printf("[2] Vulnerability Analysis\n")
        printf("[3] Utilities\n\n")
        printf("[99] Exit AbdelSploit\n\n", BLUE)
        printf("$~> ")
        self.choice = str(input("")).lower()
        self.menuchoice(self.choice)

    def menuchoice(self, x):
        if x == "1":
            self.menu_igathering()
        elif x == "11":
            cls()
            MyIP()
            self.menu()
        elif x == "12":
            cls()
            TargetIP()
            self.menu()
        elif x == "13":
            cls()
            MyDNS()
            self.menu()
        elif x == "14":
            cls()
            TargetDNS()
            self.menu()
        elif x == "15":
            cls()
            PhoneNumber()
            self.menu()
        elif x == "2":
            self.menu_vanalysis()
        elif x == "99":
            self._quit()
        else:
            self.menu()

    def menu_igathering(self):
        cls()
        banner()
        printf("[*] INFORMATION GATHERING:\n", BLUE)
        printf("[1] My IP\t\t[2] Target IP\n")
        printf("[3] My DNS\t\t[4] Target DNS\n")
        printf("[5] Phone Number\n\n")
        printf("[99] BACK\n\n", BLUE)
        printf("$~> ")
        x = str(input("")).lower()
        cls()
        if x == "1":
            MyIP()
        elif x == "2":
            TargetIP()
        elif x == "3":
            MyDNS()
        elif x == "4":
            TargetDNS()
        elif x == "5":
            PhoneNumber()
        elif x == "99":
            self.menu()
        else:
            banner()
            printf("[!] COMMAND NOT FOUND.\n", RED)
            sep()
            pause()
            self.menu_igathering()
        self.menu()

    def menu_vanalysis(self):
        cls()
        banner()
        printf("[*] VULNERABILITY ANALYSIS:\n", BLUE)
        printf("[1] Port Mapper\n")
        printf("[2] XXXXX\n\n")
        printf("[99] BACK\n\n", BLUE)
        printf("$~> ")
        x = str(input("")).lower()
        cls()
        if x == "1":
            PortMapper()
        elif x == "99":
            self.menu()
        else:
            banner()
            printf("[!] COMMAND NOT FOUND.\n", RED)
            sep()
            pause()
            self.menu_vanalysis()
        self.menu()

    def _quit(self):
        from time import sleep
        from os import system

        cls()
        printf(ascii_art, YELLOW)
        printf("\nSee you soon!", RED)
        sleep(1.5)
        exit(0)

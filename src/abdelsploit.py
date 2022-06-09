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
from src.utools import *
from src.wexploit import *
from src.carding import *

from sys import exit


class AbdelSploit:
    def __init__(self):
        self.choice = None
        self.menu()

    def menu(self):
        cls()
        banner()
        printf("[1] Information Gathering\n")
        printf("[2] Vulnerability Analysis\n")
        printf("[3] Utility Tools\n")
        printf("[4] Wireless Attacks\n")
        printf("[5] Carding\n\n")
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
        elif x == "21":
            cls()
            PortMapper()
            self.menu()
        elif x == "3":
            self.menu_utools()
        elif x == "31":
            cls()
            PasswordGenerator()
            self.menu()
        elif x == "4":
            self.menu_wexploit()
        elif x == "41":
            cls()
            GetPwds()
            self.menu()
        elif x == "5":
            self.menu_carding()
        elif x == "51":
            cls()
            CCGenerator()
            self.menu()
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

    def menu_utools(self):
        cls()
        banner()
        printf("[*] UTILITY TOOLS:\n", BLUE)
        printf("[1] Password Generator\n")
        printf("[2] XXXXX\n\n")
        printf("[99] BACK\n\n", BLUE)
        printf("$~> ")
        x = str(input("")).lower()
        cls()
        if x == "1":
            PasswordGenerator()
        elif x == "1a":
            PasswordGenerator().easy()
        elif x == "1b":
            PasswordGenerator().medium()
        elif x == "1c":
            PasswordGenerator().hard()
        elif x == "1x":
            PasswordGenerator().show()
        elif x == "1z":
            PasswordGenerator().delete()
        elif x == "99":
            self.menu()
        else:
            banner()
            printf("[!] COMMAND NOT FOUND.\n", RED)
            sep()
            pause()
            self.menu_utools()
        self.menu()

    def menu_wexploit(self):
        cls()
        banner()
        printf("[*] WIRELESS EXPLOITATION:\n", BLUE)
        printf("[1] Get Passwords\n")
        printf("[2] XXXXX\n\n")
        printf("[99] BACK\n\n", BLUE)
        printf("$~> ")
        x = str(input("")).lower()
        cls()
        if x == "1":
            GetPwds()
        elif x == "99":
            self.menu()
        else:
            banner()
            printf("[!] COMMAND NOT FOUND.\n", RED)
            sep()
            pause()
            self.menu_wexploit()
        self.menu()

    def menu_carding(self):
        cls()
        banner()
        printf("[*] CARDING:\n", BLUE)
        printf("[1] CC Generator\n")
        printf("[2] VALID CC Generator (BETA)\n")
        printf("[3] Open CC Logs\n\n")
        printf("[99] BACK\n\n", BLUE)
        printf("$~> ")
        x = str(input("")).lower()
        cls()
        if x == "1":
            CCGenerator()
        elif x == "99":
            self.menu()
        else:
            banner()
            printf("[!] COMMAND NOT FOUND.\n", RED)
            sep()
            pause()
            self.menu_carding()
        self.menu()

    def _quit(self):
        from time import sleep

        cls()
        printf(ascii_art, YELLOW)
        printf("\nSee you soon!", RED)
        sleep(1.5)
        exit(0)

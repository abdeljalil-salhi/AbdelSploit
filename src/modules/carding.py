# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.art import *
from src.print import *
from src.utilities import *

from numpy.random import seed, randint
from os import path, makedirs
from sys import platform
from datetime import datetime


class CCGenerator:
    def __init__(self):
        self.time = None
        self.bin = None
        self.month = None
        self.year = None
        self.cvv = None
        self.type = None
        self.qty = None
        self.x = False
        self.length = 0

        self.folder = "./output/carding/"
        self.filename = f"cc_{randint(0, 100000)}.txt"
        self.filepath = path.join(self.folder, self.filename)
        if not path.isdir(self.folder):
            makedirs(self.folder)

        self.f = open(self.filepath, "w+")

        banner()
        self.main()

    def generator(self):
        from time import time

        binsplit = list(self.bin)
        if self.x == True:
            binsplitt = binsplit
            binsplitlen = {i: binsplit.count(i) for i in binsplit}
            xlen = binsplitlen["x"]
            seed(int(time()) + randint(0, 100000))
            values = list(randint(0, 9, xlen))
            xlist = [i for i, e in enumerate(binsplitt) if e == "x"]
            for i in range(len(values)):
                binsplitt[xlist[i]] = str(values[i])
            binstr = ""
            for el in binsplitt:
                binstr += el
        else:
            binlen = self.length - len(self.bin)
            seed(int(time()) + randint(0, 100000))
            values = list(randint(0, 10, binlen))
            binstr = self.bin
            for el in values:
                binstr += str(el)
        total = 0
        numreversed = binstr[::-1]
        for i, _ in enumerate(numreversed):
            digit = int(numreversed[i])
            if i % 2 == 1:
                digit *= 2
                if digit > 9:
                    digit -= 9
            total += digit
        if self.month == "RND":
            seed(int(time()) + randint(0, 100000))
            self.month = randint(1, 13)
            count = 0
            _ = self.month
            while _ > 0:
                count += 1
                _ = _ // 10
            if count == 1:
                self.month = f"0{str(self.month)}"
        if self.year == "RND":
            seed(int(time()) + randint(0, 100000))
            self.year = str(randint(2023, 2027))
        if self.cvv == "RND":
            values.clear()
            if not self.type == "american_express":
                seed(int(time()) + randint(0, 100000))
                values = list(randint(0, 10, 3))
                cvvstr = ""
                for el in values:
                    cvvstr += str(el)
            else:
                seed(int(time()) + randint(0, 100000))
                values = list(randint(0, 10, 4))
                cvvstr = ""
                for el in values:
                    cvvstr += str(el)
            self.cvv = cvvstr
        printf(f"{binstr}|{self.month}|{self.year}|{self.cvv} ")
        if total % 10 == 0:
            printf("[VALID]\n", GREEN)
        else:
            printf("[INVALID]\n", RED)
        self.f.write(f"{binstr}|{self.month}|{self.year}|{self.cvv}\n")

    def main(self):
        printf("[1] CC GENERATOR\n", BLUE)
        printf("BIN\~> ")
        self.bin = str(input("")).lower()
        binsplit = list(self.bin)
        if "x" in self.bin:
            self.x = True
        else:
            self.x = False
        if self.bin[:1] == "3":
            if self.bin[1:1] in ["4", "7"]:
                self.type = "american_express"
                self.length = 15
            elif self.bin[1:1] in ["0", "6", "8"]:
                self.type = "dinersclub"
                self.length = 14
            else:
                printf("[!] Invalid BIN.\n", RED)
                sep()
                pause()
                self.__init__()
        else:
            if self.bin[:1] == "4":
                self.type = "visa"
            elif self.bin[:1] == "5":
                self.type = "mastercard"
            elif self.bin[:1] == "6":
                self.type = "discover"
            else:
                printf("[!] Invalid BIN.\n", RED)
                sep()
                pause()
                self.__init__()
            self.length = 16

        while True:
            printf("MONTH\~> ")
            self.month = str(input("")).lower()
            if self.month == "":
                self.month = "RND"
                break
            elif int(self.month) >= 1 and int(self.month) <= 12:
                break
            printf("INVALID MONTH.\n", RED)

        while True:
            printf("YEAR\~> ")
            self.year = str(input("")).lower()
            if self.year == "":
                self.year = "RND"
                break
            yearsplit = list(self.year)
            if len(yearsplit) == 2:
                year = ["2", "0", yearsplit[0], yearsplit[1]]
                yearstr = ""
                for el in year:
                    yearstr += el
                self.year = yearstr
            if self.year.isdigit() and int(self.year) >= 2022 and int(self.year) <= 2030:
                break
            printf("INVALID YEAR.\n", RED)

        while True:
            printf("CVV\~> ")
            self.cvv = str(input("")).lower()
            if self.cvv == "":
                self.cvv = "RND"
                break
            cvvsplit = list(self.cvv)
            if len(cvvsplit) == 3 or len(cvvsplit) == 4:
                break
            printf("INVALID CVV.\n", RED)

        sep()
        while True:
            printf("QUANTITY\~> ")
            self.qty = str(input("")).lower()
            if self.qty == "":
                self.qty = 10
                break
            try:
                self.qty = int(self.qty)
                if self.qty > 0 and self.qty < 1000:
                    break
            except:
                continue
            printf("INVALID QUANTITY.\n", RED)

        self.time = datetime.now()

        sep()
        for _ in range(self.qty):
            self.generator()
        self.f.close()

        self.time = str(datetime.now() - self.time)

        sep()
        printf(f"[+] {self.qty} CC generated in {self.time}...\n", BLUE)

        sep()
        printf(f"[+] Saved to: {self.filepath}\n", BLUE)

        sep()
        printf("Open CC list in file ?\t[Y]es / [N]o\n")
        printf("$~> ")
        x = str(input("")).lower()

        if x == "y" or x == "ye" or x == "yes" or x == "oui":
            if platform == "win32":
                from os import startfile
                startfile(path.realpath(self.filepath))
            else:
                from subprocess import call
                opener = "open" if platform == "darwin" else "xdg-open"
                call([opener, path.realpath(self.filepath)])

            sep()
            printf("[+] Opening...\n", BLUE)

        sep()
        pause()

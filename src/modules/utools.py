# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.art import *
from src.print import *
from src.utilities import *

from os import path, makedirs


class PasswordGenerator:
    def __init__(self):
        self.folder = "./output/utools/"
        self.filename = "passwords.csv"
        self.filepath = path.join(self.folder, self.filename)

        banner()
        printf("[1] PASSWORD GENERATOR\n", BLUE)
        printf("[A] Easy\t\t[X] Show Passwords\n")
        printf("[B] Medium\t\t[Z] Delete Passwords\n")
        printf("[C] Hard\n\n")
        printf("[99] BACK\n\n", BLUE)
        printf("$~> ")
        x = str(input("")).lower()

        cls()
        banner()
        if x == "a":
            self.easy()
        elif x == "b":
            self.medium()
        elif x == "c":
            self.hard()
        elif x == "x":
            self.show()
        elif x == "z":
            self.delete()
        elif not x == "99":
            printf("[!] INVALID OPTION.\n", RED)
            sep()
            pause()
            cls()
            self.__init__()

    def generator(self, chars):
        from random import choice
        from pyperclip import copy

        while True:
            printf("LENGTH\~> ")
            length = input("")
            if length == "":
                length = 16
                printf("Set to default length: 16\n")
                break
            else:
                try:
                    length = int(length)
                    break
                except:
                    printf("INVALID LENGTH. (integers only)\n", RED)
                    continue
        password = ""

        sep()
        for _ in range(length):
            password += choice(chars)
        printf(f"PASSWORD: {password}\n")
        copy(password)
        printf("[+] Copied to clipboard...\n", BLUE)

        sep()
        printf("Save it?\t[Y]es / [N]o\n")
        printf("$~> ")
        x = str(input("")).lower()

        sep()
        if x == "y" or x == "ye" or x == "yes" or x == "oui":
            printf("Add notes?\t [Y]es / [N]o\n")
            printf("$~> ")
            y = str(input("")).lower()

            if y == "y" or y == "ye" or y == "yes" or y == "oui":
                sep()
                printf("NOTE\~> ")
                notes = str(input(""))
            else:
                notes = "No notes added"

            if not path.isdir(self.folder):
                makedirs(self.folder)
            if not path.isfile(self.filepath):
                f = open(self.filepath, "w+")
                f.write("Password, Notes\n")
                f.close()
            f = open(self.filepath, "a+")
            f.write(f"{password}, {notes}\n")
            f.close()

            sep()
            printf("[+] Password saved\n", BLUE)
            sep()
        pause()

    def easy(self):
        printf("[1] PASSWORD GENERATOR => ", BLUE)
        printf("EASY\n", GREEN)
        self.generator("abcdefghijklmnopqrstuvwxyz")

    def medium(self):
        printf("[1] PASSWORD GENERATOR => ", BLUE)
        printf("MEDIUM\n", GREEN)
        self.generator(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

    def hard(self):
        printf("[1] PASSWORD GENERATOR => ", BLUE)
        printf("HARD\n", GREEN)
        self.generator(
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{[|`@]}+%§/?!$*^.")

    def show(self):
        from pandas import read_csv

        printf("[1] PASSWORD GENERATOR => ", BLUE)
        printf("SHOW PWDS\n", GREEN)

        sep()
        try:
            df = read_csv(self.filepath, encoding="unicode_escape")
            printf(f"{df.head()}\n")
        except:
            printf("[!] No passwords found.\n", RED)

        sep()
        pause()

    def delete(self):
        from os import remove

        printf("[1] PASSWORD GENERATOR => ", BLUE)
        printf("DELETE PWDS\n", GREEN)
        printf("Are you sure?\t[Y]es / [N]o\n")
        printf("$~> ")
        x = str(input("")).lower()

        sep()
        if x == "y" or x == "ye" or x == "yes" or x == "oui":
            try:
                if path.exists(self.filepath):
                    remove(self.filepath)
                    printf("[+] Passwords deleted successfully.\n", BLUE)
                else:
                    printf("[!] No passwords found.\n", RED)
            except:
                printf("[!] Something went wrong. (permissions)\n", RED)
            sep()
        pause()

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.art import *
from src.print import printf, GREEN, YELLOW

from os import system, get_terminal_size, name


# clear the console
def cls():
    # for Windows
    if name == "nt":
        system("cls")
    # for other platforms
    else:
        system("clear")


# print a separator
def sep():
    try:
        (w, _) = get_terminal_size()
    except:
        w = 25
    printf("-" * w + "\n", GREEN)


# pause the console
def pause():
    printf("Done? Press ENTER to continue...")
    input("")


# print the banner
def banner():
    printf(ascii_art, YELLOW)
    printf(
        "\nVersion 0.1 - Developed by Abdeljalil Salhi (@itsabdeeels on Twitter)\n\n", YELLOW)

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


class EXIFReader:
    def __init__(self):
        self.folder = "./output/utools/"
        self.filename = "exif.txt"
        self.filepath = path.join(self.folder, self.filename)
        self.target = None
        self.saved = []

        banner()
        self.main()

    def maps(self, gps_coords):
        dec_deg_lat = self.deg(float(gps_coords["lat"][0]),  float(
            gps_coords["lat"][1]), float(gps_coords["lat"][2]), gps_coords["lat_ref"])
        dec_deg_lon = self.deg(float(gps_coords["lon"][0]),  float(
            gps_coords["lon"][1]), float(gps_coords["lon"][2]), gps_coords["lon_ref"])
        return f"https://maps.google.com/?q={dec_deg_lat},{dec_deg_lon}"

    def deg(self, degree, minutes, seconds, direction):
        decimal_degrees = degree + minutes / 60 + seconds / 3600
        if direction == "S" or direction == "W":
            decimal_degrees *= -1
        return decimal_degrees

    def saver(self):
        printf("Save it?\t[Y]es / [N]o\n")
        printf("$~> ")
        x = str(input("")).lower()

        sep()
        if x == "y" or x == "ye" or x == "yes" or x == "oui":
            from datetime import datetime

            f = open(self.filepath, "a+")
            f.write(f"--- {datetime.now()}\n")
            for line in self.saved:
                f.write(line)
            f.write("\n")
            f.close()
            printf(f"[+] Saved to: {self.filepath}\n", BLUE)
            sep()

    def reader(self, file):
        from PIL import Image
        from PIL.ExifTags import GPSTAGS, TAGS

        try:
            gps_coords = {}
            image = Image.open(file)
            printf(f"[{file}]\n", GREEN)
            self.saved.append(f"[{file}]\n")
            if image.getexif() == {} or image.getexif() == None:
                printf("No EXIF data found.\n", RED)
                self.saved.append("No EXIF data found.\n")
            else:
                for tag, value in image.getexif().items():
                    tag_ = TAGS.get(tag)
                    if tag_ == "GPSInfo":
                        for key, val in value.items():
                            printf(
                                f"GPS Info\t\t: {GPSTAGS.get(key)} - {val}\n")
                            self.saved.append(
                                f"GPS Info\t\t: {GPSTAGS.get(key)} - {val}\n")
                            if GPSTAGS.get(key) == "GPSLatitude":
                                gps_coords["lat"] = val
                            elif GPSTAGS.get(key) == "GPSLongitude":
                                gps_coords["lon"] = val
                            elif GPSTAGS.get(key) == "GPSLatitudeRef":
                                gps_coords["lat_ref"] = val
                            elif GPSTAGS.get(key) == "GPSLongitudeRef":
                                gps_coords["lon_ref"] = val
                    else:
                        printf(f"{tag_} - {value}\n")
                        self.saved.append(f"{tag_} - {value}\n")
                if gps_coords:
                    __ = self.maps(gps_coords)
                    printf(__)
                    self.saved.append(__)
        except IOError:
            printf(f"[!] Incorrect file format! [{file}]\n", RED)
            self.saved.append(f"[!] Incorrect file format! [{file}]\n")

    def main(self):
        printf("[2] EXIF READER\n", BLUE)
        printf("[A] Link\n")
        printf("[B] Folder\n")
        printf("[C] File Path\n\n")
        printf("[99] BACK\n\n", BLUE)
        printf("$~> ")
        x = str(input("")).lower()

        cls()
        banner()
        if x == "a":
            from requests import head
            from urllib.request import urlretrieve
            from numpy.random import randint

            while True:
                printf("URL\~> ")
                url = input("")
                formats = ("image/png", "image/jpeg", "image/jpg")
                try:
                    r = head(url)
                    if r.headers["content-type"] in formats:
                        break
                    printf("INVALID FORMAT. (<png/jpeg/jpg> only)\n", RED)
                    continue
                except:
                    printf("INVALID URL.\n")
                    continue

            sep()
            path_ = "./images/"
            if not path.isdir(path_):
                makedirs(path_)
            file_ = path.join(path_, f"{randint(0, 100000)}.png")
            urlretrieve(url, file_)
            self.reader(file_)

            sep()
            self.saver()
            pause()
        elif x == "b":
            from os import listdir

            while True:
                printf("PATH\~> ")
                path_ = input("")
                if path_ == "":
                    path_ = "./images/"
                    if not path.isdir(path_):
                        makedirs(path_)
                try:
                    if path.isdir(path_):
                        break
                    else:
                        printf("INVALID FOLDER PATH.\n", RED)
                        continue
                except:
                    printf("INVALID FOLDER PATH.\n", RED)
                    continue
            files = listdir(path_)
            if len(files) == 0:
                printf("[!] No files found.\n", RED)
                sep()
            else:
                sep()
                for file in files:
                    self.reader(f"{path.join(path_, file)}")
                    sep()
                self.saver()
            pause()
        elif x == "c":
            while True:
                printf("FILEPATH\~> ")
                filepath = input("")
                try:
                    if path.isfile(filepath):
                        break
                    else:
                        printf("INVALID FILE PATH.\n", RED)
                        continue
                except:
                    printf("INVALID FILE PATH.\n", RED)
                    continue

            sep()
            self.reader(filepath)

            sep()
            self.saver()
            pause()
        elif not x == "99":
            printf("[!] INVALID OPTION.\n", RED)
            sep()
            pause()
            cls()
            self.__init__()

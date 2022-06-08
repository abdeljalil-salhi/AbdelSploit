# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.art import *
from src.print import *
from src.utilities import *

from socket import gethostbyname, setdefaulttimeout, inet_aton, gaierror, error, socket, AF_INET, SOCK_STREAM
from os import path, makedirs
from datetime import datetime


class PortMapper:
    def __init__(self):
        self.time = None
        self.target = None
        self.openports = []
        banner()
        self.main()

    def scanner(self, port):
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.settimeout(0.5)
            s.connect((self.target, port))
            try:
                service = s.recv(1024).decode()
                printf(f"[{datetime.now() - self.time}] PORT ")
                printf(f"{port}", GREEN)
                printf(f": OPEN ({service})\n")
                self.openports.append(port)
            except:
                printf(f"[{datetime.now() - self.time}] PORT ")
                printf(f"{port}", GREEN)
                printf(": OPEN\n")
                self.openports.append(port)
        except KeyboardInterrupt:
            printf("[!] CTRL + C pressed.\n", RED)
        except gaierror:
            printf("[!] Invalid Host.\n", RED)
        except error:
            printf("[!] Server not responding...\n", RED)
        except:
            pass

    def main(self):
        from threading import Thread

        printf("[1] PORT MAPPER\n", BLUE)
        printf("Interrupt: ")
        printf("[CTRL + C]\n", BLUE)
        while True:
            printf("IP\~> ")
            self.target = input("")
            if self.target == "":
                printf("ENTER VALID IP.\n", RED)
                continue
            else:
                try:
                    inet_aton(self.target)
                    break
                except:
                    printf("INVALID IP.\n", RED)
                    continue
        self.target = gethostbyname(self.target)

        sep()
        printf("[+] RANGE:\n")
        while True:
            try:
                printf("Start PORT: (default 1) ")
                self.start = input("")
                if self.start == "":
                    self.start = 1
                    break
                self.start = int(self.start)
                break
            except:
                printf("INVALID PORT. (integers only)\n", RED)
                continue
        while True:
            try:
                printf("End PORT: (default 1025) ")
                self.end = input("")
                if self.end == "":
                    self.end = 1025
                    break
                self.end = int(self.end)
                break
            except:
                printf("INVALID PORT. (integers only)\n", RED)
                continue

        sep()
        printf(f"Scanning {self.target} {self.start}:{self.end}...\n")
        printf(f"Started at {datetime.now()}\n")
        self.time = datetime.now()

        sep()
        for port in range(self.start, self.end):
            thread = Thread(target=self.scanner, args=[port])
            thread.start()

        sep()
        self.time = str(datetime.now() - self.time)
        printf(f"[+] Scanning completed in {self.time}...\n", BLUE)

        sep()
        printf(f"{len(self.openports)} open ports found.\n", BLUE)

        sep()
        printf("Save it?\t[Y]es / [N]o\n")
        printf("$~> ")
        x = str(input("")).lower()

        sep()
        if x == "y" or x == "ye" or x == "yes" or x == "oui":
            folder = "./output/vanalysis/"
            filename = f"pmapper_{self.target}.txt"
            filepath = path.join(folder, filename)
            if not path.isdir(folder):
                makedirs(folder)
            f = open(filepath, "w+")
            f.write(f"[*] RESULTS FOR PORTS MAPPER {self.target}\n")
            for i in range(len(self.openports)):
                f.write(f"PORT {self.openports[i]}\n")
            f.close()
            printf(f"[+] Saved to: {filepath}\n", BLUE)
            sep()
        pause()

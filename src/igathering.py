# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.art import *
from src.print import *
from src.utilities import *

from os import path, makedirs
from requests import get
from datetime import datetime


class MyIP:
    def __init__(self):
        self.time = datetime.now()
        banner()
        self.main()

    def main(self):
        self.res = get("http://ip-api.com/json/?fields=17035263")
        self.data = self.res.json()

        ip = self.data["query"]
        lat = str(self.data["lat"])
        lon = str(self.data["lon"])
        countryCode = self.data["countryCode"]
        country = self.data["country"]
        region = self.data["region"]
        regionName = self.data["regionName"]
        city = self.data["city"]
        isp = self.data["isp"]
        as_ = self.data["as"]
        mobile = self.data["mobile"]
        proxy = self.data["proxy"]
        hosting = self.data["hosting"]
        zip_ = str(self.data["zip"])
        org = self.data["org"]

        self.time = str(datetime.now() - self.time)

        printf("[1] My IP\n", BLUE)
        printf(f"IP\t\t: {ip}\n")
        printf(f"Country\t\t: [{countryCode}] {country}\n")
        printf(f"Region\t\t: [{region}] {regionName}\n")
        printf(f"City\t\t: {city}\n")
        if zip_ != "":
            printf(f"ZIP\t\t: {zip_}\n")
        printf(f"Latitude\t: {lat}\n")
        printf(f"Longitude\t: {lon}\n")
        if org != "":
            printf(f"Org.\t\t: {org}\n")
        printf(f"Org. ISP\t: {isp}\n")
        printf(f"Org. AS\t\t: {as_}\n")
        if mobile == True:
            printf("Mobile 4G\t: TRUE\n")
        elif mobile == False:
            printf("Mobile 4G\t: FALSE\n")
        if proxy == True:
            printf("Proxy/VPN\t: TRUE\n")
        elif proxy == False:
            printf("Proxy/VPN\t: FALSE\n")
        if hosting == True:
            printf("Hosting\t\t: TRUE\n")
        elif hosting == False:
            printf("Hosting\t\t: FALSE\n")

        sep()
        printf(f"[+] Scanning completed in {self.time}...\n", BLUE)

        sep()
        printf("Save it?\t[Y]es / [N]o\n")
        printf("$~> ")
        x = str(input("")).lower()
        sep()
        if x == "y" or x == "ye" or x == "yes" or x == "oui":
            folder = "./output/igathering/"
            filename = "myip.txt"
            filepath = path.join(folder, filename)
            if not path.isdir(folder):
                makedirs(folder)
            f = open(filepath, "w+")
            f.write("[*] RESULTS FOR MY IP\n")
            f.write(f"IP        : {ip}\n")
            f.write(f"Country   : [{countryCode}] {country}\n")
            f.write(f"Region    : [{region}] {regionName}\n")
            f.write(f"City      : {city}\n")
            if zip_ != "":
                f.write(f"ZIP       : {zip_}\n")
            f.write(f"Latitude  : {lat}\n")
            f.write(f"Longitude : {lon}\n")
            if org != "":
                f.write(f"Org.      : {org}\n")
            f.write(f"Org. ISP  : {isp}\n")
            f.write(f"Org. AS   : {as_}\n")
            if mobile == True:
                f.write("Mobile 4G : TRUE\n")
            elif mobile == False:
                f.write("Mobile 4G : FALSE\n")
            if proxy == True:
                f.write("Proxy/VPN : TRUE\n")
            elif proxy == False:
                f.write("Proxy/VPN : FALSE\n")
            if hosting == True:
                f.write("Hosting   : TRUE\n")
            elif hosting == False:
                f.write("Hosting   : FALSE\n")
            f.close()
            printf(f"[+] Saved to: {filepath}\n", BLUE)
            sep()
        pause()


class TargetIP:
    def __init__(self):
        self.time = None
        banner()
        self.main()

    def main(self):
        printf("Enter Target IP: ")
        self.target = input("")
        sep()
        self.time = datetime.now()
        try:
            self.res = get(
                f"http://ip-api.com/json/{self.target}?fields=17035263")
            self.data = self.res.json()

            ip = self.data["query"]
            lat = str(self.data["lat"])
            lon = str(self.data["lon"])
            countryCode = self.data["countryCode"]
            country = self.data["country"]
            region = self.data["region"]
            regionName = self.data["regionName"]
            city = self.data["city"]
            isp = self.data["isp"]
            as_ = self.data["as"]
            mobile = self.data["mobile"]
            proxy = self.data["proxy"]
            hosting = self.data["hosting"]
            zip_ = str(self.data["zip"])
            org = self.data["org"]

            self.time = str(datetime.now() - self.time)

            printf("[2] Target IP\n", BLUE)
            printf(f"IP\t\t: {ip}\n")
            printf(f"Country\t\t: [{countryCode}] {country}\n")
            printf(f"Region\t\t: [{region}] {regionName}\n")
            printf(f"City\t\t: {city}\n")
            if zip_ != "":
                printf(f"ZIP\t\t: {zip_}\n")
            printf(f"Latitude\t: {lat}\n")
            printf(f"Longitude\t: {lon}\n")
            if org != "":
                printf(f"Org.\t\t: {org}\n")
            printf(f"Org. ISP\t: {isp}\n")
            printf(f"Org. AS\t\t: {as_}\n")
            if mobile == True:
                printf("Mobile 4G\t: TRUE\n")
            elif mobile == False:
                printf("Mobile 4G\t: FALSE\n")
            if proxy == True:
                printf("Proxy/VPN\t: TRUE\n")
            elif proxy == False:
                printf("Proxy/VPN\t: FALSE\n")
            if hosting == True:
                printf("Hosting\t\t: TRUE\n")
            elif hosting == False:
                printf("Hosting\t\t: FALSE\n")

            sep()
            printf(f"[+] Scanning completed in {self.time}...\n", BLUE)

            sep()
            printf("Save it?\t[Y]es / [N]o\n")
            printf("$~> ")
            x = str(input("")).lower()
            sep()
            if x == "y" or x == "ye" or x == "yes" or x == "oui":
                folder = "./output/igathering/"
                filename = f"targetip_{ip}.txt"
                filepath = path.join(folder, filename)
                if not path.isdir(folder):
                    makedirs(folder)
                f = open(filepath, "w+")
                f.write(f"[*] RESULTS FOR IP {ip}\n")
                f.write(f"IP        : {ip}\n")
                f.write(f"Country   : [{countryCode}] {country}\n")
                f.write(f"Region    : [{region}] {regionName}\n")
                f.write(f"City      : {city}\n")
                if zip_ != "":
                    f.write(f"ZIP       : {zip_}\n")
                f.write(f"Latitude  : {lat}\n")
                f.write(f"Longitude : {lon}\n")
                if org != "":
                    f.write(f"Org.      : {org}\n")
                f.write(f"Org. ISP  : {isp}\n")
                f.write(f"Org. AS   : {as_}\n")
                if mobile == True:
                    f.write("Mobile 4G : TRUE\n")
                elif mobile == False:
                    f.write("Mobile 4G : FALSE\n")
                if proxy == True:
                    f.write("Proxy/VPN : TRUE\n")
                elif proxy == False:
                    f.write("Proxy/VPN : FALSE\n")
                if hosting == True:
                    f.write("Hosting   : TRUE\n")
                elif hosting == False:
                    f.write("Hosting   : FALSE\n")
                f.close()
                printf(f"[+] Saved to: {filepath}\n", BLUE)
        except:
            printf("[2] Target IP\n", BLUE)
            printf("INVALID TARGET.", RED)
        sep()
        pause()


class MyDNS:
    def __init__(self):
        self.time = datetime.now()
        banner()
        self.main()

    def main(self):
        from string import ascii_letters
        from random import choice

        random_ = "".join(choice(ascii_letters) for _ in range(32))
        self.res = get(f"http://{random_}.edns.ip-api.com/json/")
        self.data = self.res.json()

        dns = self.data["dns"]
        ipdns = dns["ip"]
        geodns = dns["geo"]

        self.res = get(f"http://ip-api.com/json/{ipdns}")
        self.data = self.res.json()

        region = self.data["region"]
        regionName = self.data["regionName"]
        city = self.data["city"]
        isp = self.data["isp"]
        as_ = self.data["as"]

        self.time = str(datetime.now() - self.time)

        printf("[3] My DNS\n", BLUE)
        printf(f"DNS IP\t\t: {ipdns}\n")
        printf(f"DNS GEO\t\t: {geodns}\n")
        printf(f"DNS POS\t\t: [{region}] {regionName} / {city}\n")
        printf(f"DNS ISP\t\t: {isp}\n")
        printf(f"DNS AS\t\t: {as_}\n")

        sep()
        printf(f"[+] Scanning completed in {self.time}...\n", BLUE)

        sep()
        printf("Save it?\t[Y]es / [N]o\n")
        printf("$~> ")
        x = str(input("")).lower()
        sep()
        if x == "y" or x == "ye" or x == "yes" or x == "oui":
            folder = "./output/igathering/"
            filename = "mydns.txt"
            filepath = path.join(folder, filename)
            if not path.isdir(folder):
                makedirs(folder)
            f = open(filepath, "w+")
            f.write("[*] RESULTS FOR MY DNS\n")
            f.write(f"DNS IP     : {ipdns}\n")
            f.write(f"DNS GEO    : {geodns}\n")
            f.write(f"DNS POS    : [{region}] {regionName} / {city}\n")
            f.write(f"DNS ISP    : {isp}\n")
            f.write(f"DNS AS     : {as_}\n")
            f.close()
            printf(f"[+] Saved to: {filepath}\n", BLUE)
            sep()
        pause()


class TargetDNS:
    def __init__(self):
        self.time = None
        banner()
        self.main()

    def main(self):
        printf("Enter Target DNS: ")
        self.target = input("")
        sep()
        self.time = datetime.now()
        try:
            self.res = get(
                f"http://ip-api.com/json/{self.target}")
            self.data = self.res.json()

            ip = self.data["query"]
            countryCode = self.data["countryCode"]
            country = self.data["country"]
            region = self.data["region"]
            regionName = self.data["regionName"]
            city = self.data["city"]
            isp = self.data["isp"]
            as_ = self.data["as"]

            self.time = str(datetime.now() - self.time)

            printf("[4] Target DNS\n", BLUE)
            printf(f"DNS IP\t\t: {ip}\n")
            printf(f"DNS GEO\t\t: [{countryCode}] {country}\n")
            printf(f"DNS POS\t\t: [{region}] {regionName} / {city}\n")
            printf(f"DNS ISP\t\t: {isp}\n")
            printf(f"DNS AS\t\t: {as_}\n")

            sep()
            printf(f"[+] Scanning completed in {self.time}...\n", BLUE)

            sep()
            printf("Save it?\t[Y]es / [N]o\n")
            printf("$~> ")
            x = str(input("")).lower()
            sep()
            if x == "y" or x == "ye" or x == "yes" or x == "oui":
                folder = "./output/igathering/"
                filename = f"targetdns_{ip}.txt"
                filepath = path.join(folder, filename)
                if not path.isdir(folder):
                    makedirs(folder)
                f = open(filepath, "w+")
                f.write(f"[*] RESULTS FOR DNS {ip}\n")
                f.write(f"DNS IP     : {ip}\n")
                f.write(f"DNS GEO    : [{countryCode}] {country}\n")
                f.write(f"DNS POS    : [{region}] {regionName} / {city}\n")
                f.write(f"DNS ISP    : {isp}\n")
                f.write(f"DNS AS     : {as_}\n")
                f.close()
                printf(f"[+] Saved to: {filepath}\n", BLUE)
        except:
            printf("[4] Target DNS\n", BLUE)
            printf("INVALID TARGET.", RED)
        sep()
        pause()

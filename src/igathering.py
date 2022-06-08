# !/usr/bin/env python3
# -*- coding: utf-8 -*-

from src.art import *
from src.api import *
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

        printf("[1] MY IP\n", BLUE)
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
        printf("[2] TARGET IP\n", BLUE)
        printf("IP\~> ")
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
                sep()
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

        printf("[3] MY DNS\n", BLUE)
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
        printf("[4] TARGET DNS\n", BLUE)
        printf("DNS\~> ")
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
                sep()
        except:
            printf("[4] TARGET DNS\n", BLUE)
            printf("INVALID TARGET.", RED)
            sep()
        pause()


class PhoneNumber:
    def __init__(self):
        self.time = None
        banner()
        self.main()

    def main(self):
        printf("[5] PHONE NUMBER\n", BLUE)
        printf("[format: +(countryCode)(number)] [option --deep]\n")
        printf("PHONE\~> ")
        self.target = input("")
        self.targetsplit = self.target.split()

        sep()
        printf(f"Fetching infos for {self.targetsplit[0]}\n")

        sep()
        self.time = datetime.now()

        from phonenumbers import carrier, geocoder, timezone, PhoneNumberFormat, is_possible_number, parse, format_number, region_code_for_country_code

        try:
            if self.targetsplit[1]:
                if self.targetsplit[1] == "--deep" or self.targetsplit[1] == "-deep" or self.targetsplit[1] == "-d" or self.targetsplit[1] == "--d":
                    phoneNumber = parse(str(self.targetsplit[0]), None)
                    numberCC = format_number(
                        phoneNumber, PhoneNumberFormat.INTERNATIONAL).split(" ")[0]
                    numberLOCAL = format_number(
                        phoneNumber, PhoneNumberFormat.E164).replace(numberCC, "")
                    numberINTER = format_number(
                        phoneNumber, PhoneNumberFormat.INTERNATIONAL)
                    country = geocoder.country_name_for_number(
                        phoneNumber, "en")
                    location = geocoder.description_for_number(
                        phoneNumber, "en")
                    carrierName = carrier.name_for_number(phoneNumber, "en")

                    self.res = get(
                        f"http://apilayer.net/api/validate?access_key={APIKey}&number={self.targetsplit[0]}")
                    self.data = self.res.json()

                    status = self.data["valid"]
                    localFormat = self.data["local_format"]
                    internationalFormat = self.data["international_format"]
                    countryPrefix = self.data["country_prefix"]
                    countryCode = self.data["country_code"]
                    countryName = self.data["country_name"]
                    location_ = self.data["location"]
                    carrier_ = self.data["carrier"]
                    lineType = self.data["line_type"]

                    self.time = str(datetime.now() - self.time)

                    printf(f"International format\t: {numberINTER}\n")
                    printf(f"Local format\t\t: {numberLOCAL}\n")
                    printf(f"Country\t\t\t: {country} ({numberCC})\n")
                    printf(f"City/Area\t\t: {location} / {location_}\n")
                    printf(f"Carrirer\t\t: {carrierName}\n")
                    for timezoneResult in timezone.time_zones_for_number(phoneNumber):
                        printf(f"Timezone\t\t: {timezoneResult}\n")
                    if is_possible_number(phoneNumber):
                        printf("Status\t\t\t: VALID AND POSSIBLE\n")
                    else:
                        printf("Status\t\t\t: VALID AND NOT POSSIBLE\n")

                    sep()
                    printf(f"INTER\t\t\t: {internationalFormat}\n")
                    printf(f"LCOAL\t\t\t: {localFormat}\n")
                    printf(f"PREFIX\t\t\t: {countryPrefix}\n")
                    printf(f"COUNTRY\t\t\t: [{countryCode}] {countryName}\n")
                    if location != "":
                        printf(f"LOCATION\t\t\t: {location}\n")
                    printf(f"CARRIER\t\t\t: {carrier_}\n")
                    printf(f"LINE TYPE\t\t: {lineType}\n")
                    if status == True:
                        printf("=> VALID!\n")

                    sep()
                    printf(f"[+] Scanning completed in {self.time}...\n", BLUE)

                    sep()
                    printf("Save it?\t[Y]es / [N]o\n")
                    printf("$~> ")
                    x = str(input("")).lower()

                    sep()
                    if x == "y" or x == "ye" or x == "yes" or x == "oui":
                        folder = "./output/igathering/"
                        filename = f"phonenumber_{self.targetsplit[0]}.txt"
                        filepath = path.join(folder, filename)
                        if not path.isdir(folder):
                            makedirs(folder)
                        f = open(filepath, "w+")
                        f.write(
                            f"[*] RESULTS FOR NUMBER {self.targetsplit[0]}\n")
                        f.write(f"International format : {numberINTER}\n")
                        f.write(f"Local format         : {numberLOCAL}\n")
                        f.write(
                            f"Country              : {country} ({numberCC})\n")
                        f.write(
                            f"City/Area            : {location} / {location_}\n")
                        f.write(f"Carrirer             : {carrierName}\n")
                        for timezoneResult in timezone.time_zones_for_number(phoneNumber):
                            f.write(
                                f"Timezone             : {timezoneResult}\n")
                        if is_possible_number(phoneNumber):
                            f.write(
                                "Status               : VALID AND POSSIBLE\n\n")
                        else:
                            f.write(
                                "Status               : VALID AND NOT POSSIBLE\n\n")
                        f.write(
                            f"INTER                : {internationalFormat}\n")
                        f.write(f"LCOAL                : {localFormat}\n")
                        f.write(f"PREFIX               : {countryPrefix}\n")
                        f.write(
                            f"COUNTRY              : [{countryCode}] {countryName}\n")
                        if location != "":
                            f.write(f"LOCATION             : {location}\n")
                        f.write(f"CARRIER              : {carrier_}\n")
                        f.write(f"LINE TYPE            : {lineType}\n")
                        if status == True:
                            f.write("=> VALID!\n")
                        f.close()
                        printf(f"[+] Saved to: {filepath}\n", BLUE)
                    sep()
        except:
            phoneNumber = parse(self.targetsplit[0], None)
            numberCC = format_number(
                phoneNumber, PhoneNumberFormat.INTERNATIONAL).split(" ")[0]
            numberLOCAL = format_number(
                phoneNumber, PhoneNumberFormat.E164).replace(numberCC, "")
            numberINTER = format_number(
                phoneNumber, PhoneNumberFormat.INTERNATIONAL)
            country = geocoder.country_name_for_number(phoneNumber, "en")
            location = geocoder.description_for_number(phoneNumber, "en")
            carrierName = carrier.name_for_number(phoneNumber, "en")

            self.time = str(datetime.now() - self.time)

            printf(f"International format\t: {numberINTER}\n")
            printf(f"Local format\t\t: {numberLOCAL}\n")
            printf(f"Country\t\t\t: {country} ({numberCC})\n")
            printf(f"City/Area\t\t: {location}\n")
            printf(f"Carrirer\t\t: {carrierName}\n")
            for timezoneResult in timezone.time_zones_for_number(phoneNumber):
                printf(f"Timezone\t\t: {timezoneResult}\n")
            if is_possible_number(phoneNumber):
                printf("Status\t\t\t: VALID AND POSSIBLE\n")
            else:
                printf("Status\t\t\t: VALID AND NOT POSSIBLE\n")

            sep()
            printf(f"[+] Scanning completed in {self.time}...\n", BLUE)

            sep()
            printf("Save it?\t[Y]es / [N]o\n")
            printf("$~> ")
            x = str(input("")).lower()

            sep()
            if x == "y" or x == "ye" or x == "yes" or x == "oui":
                folder = "./output/igathering/"
                filename = f"phonenumber_{self.targetsplit[0]}.txt"
                filepath = path.join(folder, filename)
                if not path.isdir(folder):
                    makedirs(folder)
                f = open(filepath, "w+")
                f.write(
                    f"[*] RESULTS FOR NUMBER {self.targetsplit[0]}\n")
                f.write(f"International format : {numberINTER}\n")
                f.write(f"Local format         : {numberLOCAL}\n")
                f.write(
                    f"Country              : {country} ({numberCC})\n")
                f.write(
                    f"City/Area            : {location}\n")
                f.write(f"Carrirer             : {carrierName}\n")
                for timezoneResult in timezone.time_zones_for_number(phoneNumber):
                    f.write(
                        f"Timezone             : {timezoneResult}\n")
                if is_possible_number(phoneNumber):
                    f.write(
                        "Status               : VALID AND POSSIBLE\n")
                else:
                    f.write(
                        "Status               : VALID AND NOT POSSIBLE\n")
                f.close()
                printf(f"[+] Saved to: {filepath}\n", BLUE)
                sep()
        pause()

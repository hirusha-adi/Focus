__AUTHOR__ = "@hirusha-adi"
__VERSION__ = "v1.0"
__LICENSE__ = "MIT LICENSE"

import os

__LOGO__ = r"""
 _____                    
|  ___|__   ___ _   _ ___ 
| |_ / _ \ / __| | | / __|
|  _| (_) | (__| |_| \__ \
|_|  \___/ \___|\__,_|___/
         Creator
"""

__CODE__ = r'''
import os
import time
from datetime import datetime as dt


def startFocus(HOSTS: str, WEBSITES, REDIRECT: str = "127.0.0.1", START_TIME: int = 7, END_TIME: int = 14):
    while True:
        if dt(
            dt.now().year,
            dt.now().month,
            dt.now().day, START_TIME
            ) < dt.now() < dt(
            dt.now().year,
            dt.now().month,
            dt.now().day, END_TIME
        ):
            print("WORK TIME")

            with open(HOSTS, 'w+') as file:
                content = file.read()
                for website in WEBSITES:
                    if website in content:
                        pass
                    else:
                        file.write(REDIRECT + " " + website + "\n")

        else:
            print("PARTY TIME")
            with open(HOSTS, 'r+') as file:
                content = file.readlines()
                file.seek(0)
                for line in content:
                    if not any(website in line for website in WEBSITES):
                        file.write(line)
                    file.truncate()

        time.sleep(15)


def start(HOSTS_FILE: str, REDIRECT_URL: str = "127.0.0.1", START_TIME: int = 7, END_TIME: int = 14):
    if "blacklist.txt" in os.listdir():
        with open(os.path.join(os.getcwd(), "blacklist.txt"), "r", encoding="utf-8") as file:
            WEBSITES_LIST = file.readlines()
    else:
        # default to this list
        WEBSITES_LIST = [
            "www.facebook.com", "facebook.com", "instragram.com", "www.instragram.com",
            "www.google.com", "google.com", "youtube.com", "www.youtube.com",
            "pornhub.com", "www.pornhub.com", "sex.com", "www.sex.com", "xnxx.com",
            "www.xnxx.com", "discord.com", "www.discord.com", "wwwi.discordapp.com",
            "www.discordapp.com", "www.photos.google.com", "photos.google.com",
            "mail.google.com", "www.mail.google.com", "gmail.com", "www.gmail.com",
            "abc.xyz", "www.abc.xyz", "www.github.com", "github.com", "github.io",
            "www.github.io", "www.daraz.lk", "daraz.lk", "aliexpress.com",
            "www.aliexpress.com", "alibaba.com", "www.alibaba.com", "teachable.com",
            "www.teachable.com", "gov.lk", "www.gov.lk", "health.gov.lk",
            "www.health.gov.lk", "paypal.com", "www.paypal.com", "spotify.com",
            "www.spotify.com", "netlix.com", "www.netflix.com", "amazon.com",
            "www.amazon.com", "wikiepedia.org", "www.wikiepedia.org", "yahoo.com",
            "www.yahoo.com", "reddit.com", "www.reddit.com", "twitter.com",
            "www.twitter.com", "ebay.com", "www.ebay.com", "xvideos.com",
            "www.xvideos.com", "cnn.com", "www.cnn.com", "fandom.com",
            "www.fandom.com", "zoon.us", "www.zoom.us", "walmart.com",
            "www.walmart.com", "craigslist.org", "www.craiglist.org", "weather.com",
            "www.weather.com", "espn.com", "www.espn.com", "imbd.com", "www.imbd.com",
            "foxnew.com", "www.foxnews.com", "linkedin.com", "www.linkedin.com",
            "microsoft.com", "www.microsoft.com", "live.com", "www.live.com",
            "being.com", "www.being.com", "usps.com", "www.usps.com", "msn.com",
            "www.msn.com", "xhamster.com", "www.xhamster.com", "quora.com",
            "www.quora.com", "linustechtips.com", "www.linustechtips.com",
            "lttstore.com", "www.lttstore.com", "apple.com", "www.apple.com",
            "yelp.com", "www.yelp.com", "www.webmd.com", "www.webmd.com", "fedex.com",
            "www.fedex.com", "stackoverflow.com", "www.stackoverflow.com", "nulled.to",
            "www.nulled.to", "weather.gov", "www.weather.gov", "tripadvisor.com",
            "www.tripadvisor.com", "ikman.lk", "www.ikman.lk", "hirufm.lk",
            "www.hirufm.lk", "google.lk", "www.google.lk", "kaymu.lk", "www.kaymu.lk",
            "hirunew.lk", "www.hirunews.lk", "yamu.lk", "www.yamu.lk", "topjobs.lk",
            "www.topjobs.lk", "wix.com", "www.wix.com", "espncricinfo.com",
            "www.espncricinfo.com", "pinterest.com", "www.pinterest.com",
            "gossiplankanews.com", "www.gossiplankanews.com", "lankacnews.com",
            "www.lankacnews.com", "yts.mx", "www.ytx.mx", "yts.am", "www.ytx.am",
            "lankacnews.com", "www.lankacnews.com", "slt.lk", "www.slt.lk",
            "office.com", "www.office.com", "dialog.lk", "www.dialog.lk", "mobitel.lk",
            "www.mobitel.lk", "whatsapp.com", "www.whatsapp.com", "newsfirst.lk",
            "www.newsfirst.lk", "cmb.ac.lk", "www.amb.ac.lk", "elakiri.com",
            "www.elakiri.com", "riyasewana.com", "www.riyasewana.com", "jvpnews.com",
            "www.jvpnews.com", "myshopify.com", "www.myshopify.com",
            "microsoftonline.com", "www.microsoftonline.com", "fiver.com",
            "www.fiver.com"
        ]

    startFocus(HOSTS=HOSTS_FILE,
               REDIRECT=REDIRECT_URL,
               WEBSITES=WEBSITES_LIST,
               START_TIME=START_TIME,
               END_TIME=END_TIME)
'''

__CODE_MID__ = """
HOSTS_FILE = "{HOSTS_FILE}"
REDIRECT_URL = "{REDIRECT_URL}"
START_TIME = {START_TIME}
END_TIME = {END_TIME}
"""

__CODE_END__ = r"""
start(HOSTS_FILE=HOSTS_FILE, REDIRECT_URL=REDIRECT_URL,
      START_TIME=START_TIME, END_TIME=END_TIME)
"""


def clearScreen():
    os.system("cls" if os.name == 'nt' else "clear")


def main():
    clearScreen()
    print(__LOGO__)

    # Getting the should blacklist URLs
    print("[*] Enter the websites you need to blacklist below: ")
    blacklist = []
    cur = ""
    count = 1
    while True:
        cur = input(f"{count}: ")
        count += 1
        if cur.lower().strip() == 'done':
            break

        if "." in cur:
            if cur.strip().startswith("http://"):
                if cur.strip().endswith("/"):
                    to_add = cur.strip().split("http://")[1][:-1]
                else:
                    to_add = cur.strip().split("http://")[1]

                if to_add.startswith("www."):
                    blacklist.append(to_add)
                    blacklist.append(to_add.split("www.")[1])
                else:
                    blacklist.append("www." + to_add)
                    blacklist.append(to_add)

            if cur.strip().startswith("https://"):
                if cur.strip().endswith("/"):
                    to_add = cur.strip().split("https://")[1][:-1]
                else:
                    to_add = cur.strip().split("https://")[1]

                if to_add.startswith("www."):
                    blacklist.append(to_add)
                    blacklist.append(to_add.split("www.")[1])
                else:
                    blacklist.append("www." + to_add)
                    blacklist.append(to_add)

            if cur.strip().startswith("www."):
                if cur.strip().endswith("/"):
                    to_add = cur.strip().split("www.")[1][:-1]
                    blacklist.append(to_add)
                else:
                    to_add = cur.strip().split("www.")[1]
                    blacklist.append(to_add)

            if cur.strip().endswith("/"):
                to_add = cur.strip()[:-1]
                blacklist.append(to_add)
            else:
                to_add = cur.strip()
                blacklist.append(to_add)

    print(blacklist)

    # Getting start and end time
    start_time = int(input("[?] Enter Start Time: ").strip())
    end_time = int(input("[?] Enter End Time: ").strip())

    # Getting other data
    HOSTS_FILE = r"C:\Windows\System32\drivers\etc\hosts" if os.name == 'nt' else r"/etc/hosts"
    REDIRECT_URL = "127.0.0.1"
    # HOSTS_FILE = r"hosts"

    # Creating the blacklist file
    with open(os.path.join(os.getcwd(), "blacklist.txt"), "w", encoding="utf-8") as blacklistfile:
        for oneline in blacklist:
            blacklistfile.write(oneline.strip() + "\n")

    # Creating the script
    FINAL = __CODE__ + \
        __CODE_MID__.format(HOSTS_FILE=HOSTS_FILE, REDIRECT_URL=REDIRECT_URL,
                            START_TIME=start_time, END_TIME=end_time) + __CODE_END__

    with open(os.path.join(os.getcwd(), "focus.pyw"), "w", encoding="utf-8") as codefile:
        codefile.write(FINAL)

    print("Made file 'blacklist.txt' and 'focus.pyw'")
    input("Press Enter to Exit...")


main()

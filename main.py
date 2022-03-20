
import os

import requests
import random
import string
from colorama import Fore
from pyfiglet import Figlet
import webbrowser

webbrowser.open('https://discord.gg/nc9NMZYKRC')

os.system('cls')


def render(text, style):
    f = Figlet(font=style)
    print('\n' * 10)
    print(f.renderText(text))


render("Silly's Proxy Scraper", "banner3-D")

readym = input(f"{Fore.RED} This program will autoscrape (HTTP, SOCK4, SOCKS5) proxies into a file")

url = 'https://api.openproxylist.xyz/http.txt'
r = requests.get(url)
result = r.text
with open("http.txt", "w") as file:
    file.write(result)

url = 'https://api.openproxylist.xyz/socks4.txt'
r = requests.get(url)
result = r.text
with open("socks4.txt", "w") as file:
    file.write(result)

url = 'https://api.openproxylist.xyz/socks5.txt'
r = requests.get(url)
result = r.text
with open("socks5.txt", "w") as file:
    file.write(result)

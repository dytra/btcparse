#!/usr/bin/python3.4
import requests
import json
from colorama import *

BLUE  = Fore.BLUE+Style.BRIGHT
GREEN = Fore.GREEN+Style.BRIGHT
RESET = Style.RESET_ALL

def info(str):
	print("{}[-]{}{}".format(BLUE,RESET," " + str))

def success(str):
	print("{}[+]{}{}".format(GREEN,RESET," " + str))


info("Parsing information from server...")
url = "https://bitpay.com/api/rates"
r	  = requests.get(url).text
result = json.loads(r)

parse = [i for i in result if i['code'] == "IDR"]
rate  = int(parse[0]['rate'])
code  = parse[0]['code']
success("Information parsed successfully!")
print("1 BTC = {} {}".format(rate,code))


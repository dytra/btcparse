#!/usr/bin/python3.4
import requests
import json
from sys import argv
from colorama import *

BLUE  = Fore.BLUE+Style.BRIGHT
GREEN = Fore.GREEN+Style.BRIGHT
RED   = Fore.RED+Style.BRIGHT
RESET = Style.RESET_ALL
def info(str):
	print("{}[-]{}{}".format(BLUE,RESET," " + str))

def success(str):
	print("{}[+]{}{}".format(GREEN,RESET," " + str))

def error(str):
	print("{}[+]{}{}".format(RED,RESET," " + str))


def usage():
	print("Usage: ")
	print("{} <currency>".format(argv[0]))
	print("Ex: {} {}".format(argv[0],"usd"))

def connect():
	global result
	url = "https://bitpay.com/api/rates"
	try:
		r	  = requests.get(url).text
	except:
		error("There was an error during connecting to the server")
		exit()
	result = json.loads(r)

try:
	inputuser = argv[1].upper() 
except IndexError:
	print("Syntax Error!")
	usage()
	exit()
info("Parsing information from server...")
connect()
parse = [i for i in result if i['code'] == inputuser]
try:
	rate  = int(parse[0]['rate'])
except:
	error("ERROR: {} is not exist!".format(inputuser))
	exit()
	
code  = parse[0]['code']
success("Information parsed successfully!")
print("1 BTC = {} {}".format(rate,code))


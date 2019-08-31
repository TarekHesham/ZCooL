#ZeroCooL_Nmap
import os
import sys
from time import sleep
green = "\033[92m"
color = "\033[96m"
red = "\033[91m"
yellow = "\033[93m"

def cl():
	os.system("clear")

#logo
def logo():
	cl(),os.system("figlet -f slant 'Zero.CooL' | lolcat")

def install():
	print (green,"LODING •••••")
	sleep(1)
	cl(),os.system("pkg install nmap"),cl()
	print (red,"|||||===============[25%]")
	sleep(0.3),cl()
	print (yellow,"||||||||||==========[50%]")
	sleep(0.3),cl()
	print (color,"|||||||||||||||=====[75%]")
	sleep(0.3),cl()
	print (green,"||||||||||||||||||||[100%]")
	sleep(1)
	print (green,"FINISH!")
	sleep(1)
	reset()

def reset():
	sleep(1),logo(),zcool()

#The_Script_Zero_CooL
def zcool():
	print (red,"Welcome To Nmap Tool's")
	print (yellow,"[~!~] (1) Scan Ports   [Z~CooL]")
	print (" [~!~] (2) Scan All IP  [Z~CooL]")
	print (" [~!~] (3) Scan CIDR    [Z~CooL]")
	print (color,"[~!~] (4) Scan File    [Z~CooL]")
	print (" [~!~] (5) Scan 3sho2e  [Z~CooL]")
	print (" [~!~] (6) Scan Dinger  [Z~CooL]")
	print (green,"[~!~] (7) Scan IPV6    [Z~CooL]")
	print (" [~!~] (8) SKIP FireWall[Z~CooL]")
	print (" [~!~] (9) TCP SYN Ping [Z~CooL]")
	print (red,"[~!~] (i) Install Nmap [Z~CooL]")
	print (" [~!~] (x) Exit |•|")
	zcool = input ("#~: ")
	if zcool == "1":
		IP = input ("Enter IP : ")
		os.system("nmap {}".format(IP))

	elif zcool == "2":
		os.system ("nmap 192.168.10.1-255")

	elif zcool == "3":
		os.system ("nmap 192.168.10.1/24")

	elif zcool == "4":
		file = input ("local File : ")
		os.system ("nmap -iL {}".format(file))

	elif zcool == "5":
		number = input ("Enter Number Host's Scan : ")
		os.system ("nmap -iR {}".format(number))

	elif zcool == "6":
		IP = input ("Enter IP : ")
		os.system ("nmap -A {}".format(IP))

	elif zcool == "7":
		IPV6 = input ("Enter IPV6 : ")
		os.system ("nmap -6 {}".format(IPV6))

	elif zcool == "8":
		IP = input ("Enter IP : ")
		os.system ("nmap -PN {}".format(IP))

	elif zcool == "9":
		print ("*~ Enter IP (127.0.0.1) OR Port and IP (80,443,22,...)")
		IP = input ("Enter IP or PORTS AND IP : ")
		os.system ("nmap -PS {}".format(IP))

	elif zcool == "i":
		install()
	elif zcool == "x":
		print ("Good Luck :)")
	else:
		print ("ERROR 404"),reset()




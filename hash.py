import hashlib,os,sys
green = "\033[92m"
color = "\033[96m"
red = "\033[91m"
yellow = "\033[93m"
Z = os.system
def logo():
	Z("clear"),Z("figlet -f slant 'Zero.CooL' | lolcat")
def hash_lib():
	print (green,"Hello Sir in New Tool Hashing")
	h = hashlib.algorithms_guaranteed
	print (red,"Select Hash :\n",h)
	Shash = str(input("#~: "))
	hash = hashlib.new(Shash)
	print (yellow," Enter Data")
	data = input("#~: ")
	dataa = data.encode("utf-8")
	hash.update(dataa)
	print (color,"Data after hash using (",Shash,")\n",hash.hexdigest())


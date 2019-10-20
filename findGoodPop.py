#!/usr/bin/env python2
# this script read addrs for pop pop ret (file with addrs in separate lines)
# read bad chars for one env. (list of \x style string like "\xEF\xDD")
# gives an output wether an address is suitable for use.

def main():
	# take a list of address (pop pop ret) and check if one of clean from bad characters
	addrs = []
	with open('poppoprets.txt', 'r') as file:
		addrs = file.readlines()
		for addr in addrs:
			addr=addr.lower()			
			l=0
			strb=""
			isAddrOk=False
			while l<len(addr):
				strb+=addr[l]
				if(l%2==1):					
					if  ifBadChar(strb)==False:
						isAddrOk=True
					else:
						isAddrOk=False
						print "Addr: " + addr.replace("\n","") +" is bad!"
						break	
					strb=""				
				l+=1
			if isAddrOk==True:
				print "Addr: " + addr.replace("\n","") +" is good!"
				



def ifBadChar(bytechar):
	bad_chars = []
	with open('badchar_result.txt', 'r') as file:
		data = file.read().replace("\\x"," " ).lower()
		if bytechar in data:
			return True
		else:
			return False


main()

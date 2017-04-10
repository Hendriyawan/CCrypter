#! /usr/bin/python
#vim : set fileencoding=utf-8: ^[\t\v]*#.*?coding[:=] [\t]* ([-_.a-zA-Z0-9)+]
# Copyright(c) <2017> <hendriyawan
# github : https://github.com/mrSilent0598
# fb : m.facebook.com/hendri.glanex
# This program free software software, you can redistribute it and/or modify
# GD (glanex dev)
# created by hendri(mr_silent)

import os
import sys
import Caesar
import pycolor
color = pycolor.pyColor()
#banner
def banner():
	os.system('clear')
	print """
   _________________
   /   ____//   ____/
  /   /___ /   /___
  \______/ \______/"""+color.cyan+"RYPTER"+color.reset+" (c)2017"
	print("\t"+color.blue+"created by :"+color.yellow+" hendriyawan"+color.reset)
	print("\t"+color.blue+"code name :"+color.yellow+" mr_silent"+color.reset)
	print("\t@___Glanex Dev___")
	print ""
#helps
def helps():
	print(color.error(" Missing argument !"))
	print("    Usage : ./ccrypter.py [-fe/-fd/-e/-d]")
	print("    -fe : to encryption with txt file")
	print("    -fd : to decryption with txt file")
	print("    -e : to encryption without txt file")
	print("    -d : to decryptiom withput txt file")
	print ""
# set window title
def setWindowTitle(title):
	setTitle = 'echo -ne "\033]0;%s\007"' % str(title)
	os.system(setTitle)
#main
def main(argv):
	if(len(sys.argv) != 2):
		helps()
		sys.exit(1)
	options = str(sys.argv[1])
	#encryption
	if options == "-e":
		setWindowTitle("CCrypter")
		banner()
		plaintext = raw_input(color.proc(" Enter messages : "))
		key = raw_input(color.proc(" Enter key : "))
		try:
			Caesar.encrypt(str(plaintext), key)
		except:
			print(color.error(" Failed to encrypt ! "))
	#decryption
	if options == "-d":
		setWindowTitle("CCrypter")
		banner()
		ciphertext = raw_input(color.proc(" Enter ciphertext : "))
		key = raw_input(color.proc(" Enter key : "))
		try:
			Caesar.decrypt(str(ciphertext), key)
		except:
			print(color.error(" Failed to decrypt ! "))
	
	if options == "-fe":
		setWindowTitle("CCrypter")
		banner()
		file = raw_input(color.proc(" Enter file to encrypt : "))
		key = raw_input(color.proc(" Enter key : "))
		try:
			print(color.proc(" Encrypting ..."))
			Caesar.encryptFile(file, key)
		except:
			print(color.error(" Encrypting failed !"))
			print ""
			
	if options == "-fd":
		setWindowTitle("CCrypter")
		banner()
		file = raw_input(color.proc(" Enter file to decrypt : "))
		key = raw_input(color.proc(" Enter key : "))
		try:
		    print(color.proc(" Decrypting ..."))
		    Caesar.decryptFile(file, key)
		except:
			print(color.error(" Decrypting failed !"))
			print ""
	if not options in ["-e","-d","-fe","-fd"]:
		helps()
    
if __name__ == "__main__":
	main(sys.argv[1:])
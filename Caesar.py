# vim : set fileencoding=utf-8 : ^[\t\v]*#.*?coding[:=] [\t]* ([-_.a-zA-Z0-9]+)
# Copyright(c) <2017> <hendriyawan
# github : https://github.com/mrSilent0598
# fb : m.facebook.com/hendri.glanex
# This program free software software, you can redistribute it and/or modify
# GD (glanex dev)
# created by hendri(mr_silent)

import pycolor
import time
color = pycolor.pyColor()

#saveFileEncrypted
def saveFileEncrypted(content):
	filename = time.strftime("ccrypter_encrypted_%H_%M_%S.txt")
	f = open("encrypted/"+filename, "ar+")
	ciphertext = ""
	for c in content:
		ciphertext += c
	f.write(ciphertext)
	f.close()
	print(color.proc(" File saved on "+color.result(filename)))
		
#saveFileDecrypted
def saveFileDecrypted(content):
	filename = time.strftime("ccrypted_decrypted_%H_%M_%S.txt")
	f = open("decrypted/"+filename, "ar+")
	plaintext = ""
	for p in content:
		plaintext += p
	f.write(plaintext)
	f.close()
	print(color.proc(" File saved on "+color.result(filename)))
	
#encrypt
def encrypt(texts, keys):
	plaintext = list(texts)
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	symbol = list("_,.\"@#$%&-+()*':;!?/\<>^={}[]|~")
	key = int(keys)
	ciphertext = ''
	
	for c in plaintext:
		if c in alphabet:
			ciphertext += alphabet[(alphabet.index(c)+key) %26]
		if c in Alphabet:
			ciphertext += Alphabet[(Alphabet.index(c)+key) %26]
		if c in symbol:
			ciphertext += symbol[(symbol.index(c)+key) % (len(symbol))]
		if c == " ":
			ciphertext = ciphertext + c
		if c == "\n":
			ciphertext = ciphertext + c
	print(color.resulte(" Ciphertext is : "+color.result(ciphertext)))
	print ""
	return ciphertext
	
#decrypt
def decrypt(texts, keys):
	ciphertext = list(texts)
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	symbol = list("_,.\"@#$%&-+()*':;!?/\<>^={}[]|~")
	key = int(keys)
	plaintext = ''
	
	for p in ciphertext:
		if p in alphabet:
			plaintext += alphabet[(alphabet.index(p)-key) %26]
		if p in Alphabet:
			plaintext += Alphabet[(Alphabet.index(p)-key) %26]
		if p in symbol:
			plaintext += symbol[(symbol.index(p)-key) % (len(symbol))]
		if p == " ":
			plaintext = plaintext + p
		if p == "\n":
			plaintext = plaintext + p
	print(color.resultp(" Plaintext is : "+color.result(plaintext)))
	print ""
	return plaintext

#encrypt file
def encryptFile(file, keys):
	try:
		f = open(file, "r")
		for lines in f.readlines():
			plaintext = list(lines)
			alphabet = list('abcdefghijklmnopqrstuvwxyz')
			Alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
			symbol = list("_,.\"@#$%&-+()*':;!?/\<>^={}[]|~")
			key = int(keys)
			ciphertext = ''
			
			for c in plaintext:
				if c in alphabet:
					ciphertext += alphabet[(alphabet.index(c)+key) %26]
				if c in Alphabet:
					ciphertext += Alphabet[(Alphabet.index(c)+key) %26]
				if c in symbol:
					ciphertext += symbol[(symbol.index(c)+key) % (len(symbol))]
				if c == " ":
					ciphertext = ciphertext + c
				if c == "\n":
					ciphertext = ciphertext + c
			saveFileEncrypted(ciphertext)
		print(color.proc(" Encrypting done !"))
		print ""
	except IOError:
		print(color.error(" Encrypting failed !"))
		print(color.error(" File %s not found !" %file))
		print ""

#decrypt file
def decryptFile(file, keys):
	try:
		f = open(file, "r")
		for lines in f.readlines():
			ciphertext = list(lines)
			alphabet = list('abcdefghijklmnopqrstuvwxyz')
			Alphabet = list('ABCDEFGHIJKLMMOPQRSTUVWXYZ')
			symbol = list("_,.\"@#$%&-+()*':;!?/\<>^={}[]|~")
			key = int(keys)
			plaintext = ''
			
			for p in ciphertext:
				if p in alphabet:
					plaintext += alphabet[(alphabet.index(p)-key) %26]
				if p in Alphabet:
					plaintext += Alphabet[(Alphabet.index(p)-key) %26]
				if p in symbol:
					plaintext += symbol[(symbol.index(p)-key) % (len(symbol))]
				if p == " ":
					plaintext = plaintext + p
				if p == "\n":
					plaintext = plaintext + p
			saveFileDecrypted(plaintext)
		print(color.proc(" Decrypting done !"))
		print ""
	except IOError:
		print(color.error(" Decrypting failed !"))
		print(color.error(" File %s not found !" %file))
		print ""
#! /usr/bin/python3
# -*- coding:utf-8 -*-
from secure import Clear
from desgui import DESGUI
from rsagui import RSAGUI
from aesgui import AESGUI

#Secure()

def Menu():
	print('Press 0 or exit to quit !')
	print('\t 1.- AES\n\t 2.- RSA\n\t 3.- DES3\n\t 0.- Menu\n')

	try:
		choice = input('Select your Crypt... : ')
	except EOFError:
		choice = "exit"
	#Choice for AES Encryption
	if choice == '1':
		aes = AESGUI()
		Clear()
		print('\t   1.- AES')
		print("\t\t1.- Message\n\t\t2.-File\n\t\t0.- Menu")
		ch2 = input('\t\t')
		if ch2 == "0":
			Menu()
		elif ch2 == '1':
			aes.Message()
			Clear()
			Menu()
		elif ch2 == "2":
			aes.File()
			Clear()
			Menu()
		else:
			Clear()
			Menu()
	#Choice for RSA Encryption
	elif choice == '2':
		Clear()
		rsa = RSAGUI()
		print('\t   2.-RSA')
		print("\t\t1.- Message\n\t\t2.-Generate Keys\n\t\t0.- Menu")
		ch2 = input('\t\t')
		if ch2 == "0":
			Clear()
			Menu()
		elif ch2 == "1":
			rsa.Message()
			Clear()
			Menu()
		elif ch2 == "2":
			rsa.Generates()
			Clear()
			Menu()
		else:
			Clear()
			Menu()
	#Choice for DES Encryption
	elif choice == '3':
		Clear()
		des = DESGUI()
		Clear()
		print('\t   4.-DES3')
		print("\t\t1.- Message\n\t\t2.-File\n\t\t0.- Menu")
		ch2 = input('\t\t')
		if ch2 == "0":
			Clear()
			Menu()
		elif ch2 == '1':
			des.Message()
			Clear()
			Menu()
		elif ch2 == "2":
			des.File()
			Clear()
			Menu()
		else:
			Clear()
			Menu()
	elif choice == '0' or choice == 'exit':
		exit()
	else:
		Clear()
		Menu()

Menu()

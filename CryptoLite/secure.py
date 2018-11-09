#! /usr/bin/python3
# -*- coding:utf-8 -*-
import os
from uuid import getnode as get_mac
import platform as plt

theMC = "good"

def Secure():
	#mac = get_mac()
	#macString = ':'.join(("%012X" % mac)[i:i+2] for i in range(0,12,2))
	#print('MAC String : ',macString)
	macString = input('PassWord : ')
	if macString != theMC:
		exit()
	else:
		print('')# Security Verified !

def Clear(): #Function to Clear de Command prompt detect the platform before
	syst = plt.system()
	if syst == 'Linux':
		os.system('clear')
	elif syst == 'Windows':
		os.system('cls')
	print('+=+\t CrytoGramm \t+=+')

# from uuid import getnode as get_mac
# mac = get_mac()

# print('mac : ',hex(mac))

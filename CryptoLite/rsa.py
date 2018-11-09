#! /usr/bin/python3
# -*- coding:utf-8 -*-

from Crypto.PublicKey import RSA
from Crypto import Random
import os
from base64 import *
from pathlib import Path

class RSACipher(object):

	def __init__(self):
		print('RSA')
		self.home = str(Path.home())

	def GenerateKeys(self,name):
		print('\t\t == PRIVATE AND PUBLIC KEY GENERATION ==')

		from Crypto.PublicKey import RSA
		key = RSA.generate(2048)

		namePriv = self.home+"\\Desktop\\"+name+'_Private.pem'
		namePub = self.home+"\\Desktop\\"+name+'_Public.pem'

		#generate private key
		fpri = open(namePriv,'wb')
		fpri.write(key.exportKey('PEM'))
		fpri.close()
		#generate public key
		fpub = open(namePub,'wb')
		fpub.write(key.publickey().exportKey('PEM'))
		fpub.close()
		return "\nPUBLIC KEY : "+namePub+"\nPRIVATE KEY : "+namePriv

	def EncryptMessage(self,filename,msj):
		from Crypto.PublicKey import RSA
		k = Random.new().read(8)


		if(os.path.isfile(filename) == True):
			#Get the public key to encrypt the message
			f = open(filename,'r')
			RSAkey = RSA.importKey(f.read())
			f.close()
			try:
				encryptMsj = RSAkey.encrypt(msj.encode(),k)
			except TypeError:
				print("No Public Key !")
			except Exception:
				print ('Error !')
			print('\nEncrypted Message :\n')

			return b64encode(encryptMsj[0]) 
		else:
			return 'Select a valid File !'

	def DecryptMessage(self,filename,cph):
		from Crypto.PublicKey import RSA

		if(os.path.isfile(filename) == True):

			f = open(filename,'r')
			print('filename : ',filename)

			RSAkey = RSA.importKey(f.read())	
			f.close()
			
			#print('\n Encode : ',msj)
			try:
				decrypted_msg = RSAkey.decrypt(b64decode(cph))
				print("DEC : ",decrypted_msg)
				return decrypted_msg
			except TypeError:
				print("No Public Key !")
			except Exception:
				print ('Error !')
			

		else:
			return 'Select a valid File !'

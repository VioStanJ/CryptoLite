#! /usr/bin/python3
# -*- coding:utf-8 -*-

import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from secure import *
from string import *
from base64 import *
import getpass
import tkinter as tk  
from tkinter import filedialog

class AESCipher(object):

    def __init__(self):
        print('AES')
    
    def EncryptFile(self,key,fileName):
        key = self.getKey(key) #to remove if you dont use the gui cause in console this method has already called
        chunkSize = 64*1024
        outputFile = os.path.dirname(fileName)+"/(encrypted)"+os.path.basename(fileName)
        print('OUTPUT : '+outputFile) #Generate an encrypted file save in the output acces file 
        fileSize = str(os.path.getsize(fileName)).zfill(16)
        IV = Random.new().read(16)
        encryptor = AES.new(key,AES.MODE_CBC,IV)
        
        with open(fileName,'rb') as inFile:
            with open(outputFile,'wb') as outFile:
                outFile.write(fileSize.encode('utf-8'))
                outFile.write(IV)
                
                while True:
                    chunk = inFile.read(chunkSize)
        
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' '*(16-(len(chunk)%16)) 
                        
                    outFile.write(encryptor.encrypt(chunk))
        return outputFile

    def DecryptFile(self,key,fileName):
        key = self.getKey(key) #to remove if you dont use the gui cause in console this method has already called
        chunksize = 64*1024
        base = os.path.basename(fileName)
        if "(encrypted)" in fileName:
            outputFile = os.path.dirname(fileName)+'/'+base[11:]
        else:
            from random import randint
            outputFile = os.path.dirname(fileName)+'/'+str(randint(1,1000000))+base

        print('OUTPUT : '+outputFile) #Generate an encrypted file save in the output acces file
        with open(fileName,'rb') as inFile:
            filesize = int(inFile.read(16))
            IV = inFile.read(16)
            decryptor = AES.new(key,AES.MODE_CBC,IV)

            with open(outputFile,'wb') as outfile:
                while True:
                    chunk = inFile.read(chunksize)
	        
                    if len(chunk) == 0:
                        break

                    outfile.write(decryptor.decrypt(chunk))
                outfile.truncate(filesize)
        return outputFile
                

    def getKey(self,password):
        hasher = SHA256.new(password.encode('utf-8')) 
        return hasher.digest()

    def File(self):
        choice = input("would you like to (E)ncrypt ou (D)ecrypt File? : ")
        print(choice)
        if choice == 'E' or choice == 'e':
            #filename = input("File Encrypt : ")
            root = tk.Tk()
            root.filename = filedialog.askopenfilename(initialdir = "/home/",title="Select your FILE to ENCRYPT :",filetypes=(('Files files','*.*'),("all files","*.*")))
            root.destroy()
            print("File : ",root.filename)
            if not root.filename :
                Clear()
                return
            if(os.path.isfile(root.filename) == True):
                password = getpass.getpass("Enter the key :")
                self.EncryptFile(self.getKey(password), root.filename)
            else:
                print('The file is not valid !')
            print('Done')
        elif choice == 'D' or choice == 'd':
            root = tk.Tk()
            root.filename = filedialog.askopenfilename(initialdir = "/home/",title="Select your FILE to DECRYPT :",filetypes=(('Files files','*.*'),("all files","*.*")))
            root.destroy()
            print("File : ",root.filename)
            if not root.filename :
                Clear()
                return
            if(os.path.isfile(root.filename) == True):
            	password = getpass.getpass("Enter the key :")
            	self.DecryptFile(self.getKey(password), root.filename)
            else:
                print('The file is not valid !')
            print('Done')
        else:
            print('No option selected, closinng...')

    def pad(self,text):
        while len(text) % 16 != 0:
            text += ' '
        return text

    def EncryptMessage(self,msj,pas):
        msjPad = self.pad(msj)

        enPas = self.getKey(pas)

        aes = AES.new(enPas,AES.MODE_ECB)
        msjEnc = aes.encrypt(msjPad)
        return b64encode(msjEnc)


    def DecryptMessage(self,msj,pas):
        msj = self.pad(msj)
        enPas = self.getKey(pas)

        aes = AES.new(enPas,AES.MODE_ECB)
        msjDec = aes.decrypt(b64decode(msj))
        return msjDec
            

    def Message(self):
        choice = input("would you like to (E)ncrypt ou (D)ecrypt Message ? : ")
        if('E' in choice or 'e' in choice):
            self.EncryptMessage()
        elif('D' in choice or 'd' in choice):
        	try:
        		self.DecryptMessage()
        	except ValueError:
        		print('The encrypted message is not valid !')
        	except :
        		print('An error has been detected !')

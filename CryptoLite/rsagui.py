#! /usr/bin/python3
# -*- coding:utf-8 -*-

from tkinter import *
from tkinter import filedialog
import tkinter as tk                    # imports
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from rsa import RSACipher
import os

class RSAGUI(object):

	def __init__(self):
		print('RSA GUI')
		self.fichier = ""
		self.ab = False

	def Message(self):
		self.win = tk.Tk()                           # Create instance      
		self.win.title("RSA Message GUI")                 # Add a title 
		self.win.resizable(False, False)
		self.win.iconbitmap(r'key.ico')
		
		#Image
		image1 = PhotoImage(file="attente.gif")
		self.w = image1.width()
		self.h = image1.height()
		self.win.geometry("%dx%d+0+0" % (self.w, self.h))
		panel1 = tk.Label(self.win, image=image1)
		panel1.pack(side='top', fill='both', expand='yes')
		#Images

		welcome = Label(panel1,text="ENCRYPT : DECRYPT : RSA MESSAGE",fg="blue")
		self.msj = ScrolledText(panel1,height=8,width=45)
		welcome.pack()
		self.msj.pack()
		
		#Key
		pasFr = Frame(panel1)
		self.sk = Button(pasFr,text="Select a PUBLIC or PRIVATE KEY ",fg='green')
		self.sk.bind("<Button-1>",self.FileEnter)
		self.sk.pack(side="left")
		self.kch = Label(pasFr,text="key Choose : ")
		self.kch.pack(side="right")
		pasFr.pack()	

		fr = Frame(panel1)
		self.butEnc = Button(fr,text="ENCRYPT")
		self.butEnc.bind("<Button-1>",self.EncryptMsj)
		v1 = Label(fr,text="       ")
		
		self.butDec = Button(fr,text="DECRYPT")
		self.butDec.bind("<Button-1>",self.DecryptMsj)
		self.butEnc.pack(side="left")
		v1.pack(side="left")
		self.butDec.pack(side='right')
		fr.pack()
		self.cph = ScrolledText(panel1,height=10,width=45)
		self.cph.pack()
		rs = Button(self.win,text="RESET",fg='red')
		rs.bind("<Button-1>",self.Reset)
		rs.pack()
		self.win.mainloop()

	def FileEnter(self,event):
		filename = filedialog.askopenfilename(initialdir = "/home/",title="Select a PUBLIC KEY file to ENCRYPT :",filetypes=(('RSA files','*.pem'),("all files","*.*")))
		self.fichier = filename
		self.kch.config(text=self.fichier)
		self.Updates()


	def EncryptMsj(self,event):
		rsa = RSACipher()
		encM = rsa.EncryptMessage(self.fichier,self.msj.get(1.0, END))
		self.cph.delete('1.0', END)
		self.cph.insert(tk.INSERT,encM)
		print("FICH : ",self.fichier)

	def DecryptMsj(self,event):
		rsa = RSACipher()
		try:
			print("FICH : ",self.fichier)
			encM = rsa.DecryptMessage(self.fichier,self.msj.get(1.0, END))
			self.cph.delete('1.0', END)
			self.cph.insert(tk.INSERT,encM)
		except Exception:
			messagebox.showinfo(message="binascii Error \n Enter an encrypted message\n\t Or Verify your RSA KEY !")
		
	def Reset(self,event):
		self.cph.delete('1.0', END)
		self.msj.delete('1.0', END)
		self.kch.config(text="Key Choose :")

	def KeyEnter(self,event):
		filename = filedialog.askopenfilename(initialdir = "/home/",title="Select a PUBLIC or PRIVATE KEY file :",filetypes=(('RSA files','*.pem'),("all files","*.*")))
		self.cle = filename
		self.ks.config(text=self.fichier)
		self.Updates()

	def Updates(self):
		if(self.ab == False):
			self.win.geometry("%dx%d+0+0" % (self.w+1, self.h+1))
			self.ab = True
		else:
			self.win.geometry("%dx%d+0+0" % (self.w-1, self.h-1))
			self.ab = False

	def Reset2(self,event):
		self.fs.config(text="File Selected :")
		self.ks.config(text="Key Selected :")
		self.fin.delete('1.0', END)
		self.Updates()

	def Generates(self):
		self.win = tk.Tk()                           # Create instance      
		self.win.title("RSA Key Genrator")                 # Add a title 
		self.win.resizable(False, False)
		self.win.iconbitmap(r'key.ico')
		
		#Image
		image1 = PhotoImage(file="attente.gif")
		self.w = image1.width()
		self.h = image1.height()
		self.win.geometry("%dx%d+0+0" % (self.w, self.h))
		panel1 = tk.Label(self.win, image=image1)
		panel1.pack(side='top', fill='both', expand='yes')
		#Images

		l = Label(panel1,text="RSA KEY Generator",fg="red")
		l.pack()

		f = Frame(panel1)
		l2 = Label(f,text="Enter a name for the rsa key name :")
		l2.pack(side="left")
		self.fich = StringVar()
		ent = Entry(f,textvariable=self.fich)
		ent.pack(side="right")
		f.pack()

		f0 = Label(panel1,text="")
		f0.pack()

		bgen = Button(panel1,text="Generate keys",fg='green')
		bgen.bind("<Button-1>",self.PutKey)
		bgen.pack()

		f0 = Label(panel1,text="")
		f0.pack()

		self.term = ScrolledText(panel1,height=8,width=45)
		self.term.pack()
		self.win.mainloop()

	def PutKey(self,event):
		if(self.fich.get() != ""):
			self.term.delete('1.0', END)
			self.term.insert(tk.INSERT,"Generating keys .......\n")
			rsa = RSACipher()
			out = rsa.GenerateKeys(self.fich.get())
			self.term.insert(tk.INSERT,out+"\nDone !")
		else:
			messagebox.showinfo(message="Name Required \n Enter a name !")


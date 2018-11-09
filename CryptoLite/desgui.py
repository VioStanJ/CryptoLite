from tkinter import *
from tkinter import filedialog
import tkinter as tk                    # imports
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from des import DESCipher
from tkinter import messagebox
import os

class DESGUI(object):
	"""docstring for AESGUI_MSJ"""
	def __init__(self):
		print('DES GUI')
		self.ab = False

	def Updates(self):
		if(self.ab == False):
			self.win.geometry("%dx%d+0+0" % (self.w+1, self.h+1))
			self.ab = True
		else:
			self.win.geometry("%dx%d+0+0" % (self.w-1, self.h-1))
			self.ab = False

	def Message(self):
		self.win = tk.Tk()                           # Create instance      
		self.win.title("DES Message GUI")                 # Add a title 
		self.win.geometry('500x400')
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

		welcome = Label(panel1,text="ENCRYPT : DECRYPT : DES MESSAGE",fg="blue")
		self.msj = ScrolledText(panel1,height=8,width=45)
		welcome.pack()
		self.msj.pack()
		
		f0 = Label(panel1,text=" ")
		f0.pack()
		#Key
		pasFr = Frame(panel1)
		lk = Label(pasFr,text="Enter your key :",fg='green')
		lk.pack(side="left")
		self.passKey = StringVar()
		self.key = Entry(pasFr,textvariable=self.passKey,show="*")
		self.key.pack(side="right")
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

		f0 = Label(panel1,text=" ")
		f0.pack()
		
		self.cph = ScrolledText(panel1,height=8,width=45)
		self.cph.pack()
		rs = Button(panel1,text="RESET",fg='red')
		rs.bind("<Button-1>",self.Reset)
		rs.pack()
		self.win.mainloop()

	def EncryptMsj(self,event):
		des = DESCipher()
		encM = des.EncryptMessage(self.msj.get(1.0, END),self.passKey.get())
		self.cph.delete('1.0', END)
		self.cph.insert(tk.INSERT,encM)

	def DecryptMsj(self,event):
		des = DESCipher()
		try:
			encM = des.DecryptMessage(self.msj.get(1.0, END),self.passKey.get())
			self.cph.delete('1.0', END)
			self.cph.insert(tk.INSERT,encM)
		except Exception:
			messagebox.showinfo(message="binascii Error \n Enter an encrypted message")

	def Reset(self,event):
		self.cph.delete('1.0', END)
		self.msj.delete('1.0', END)
		self.key.delete('0',"end")

	#File AES MEthod
	def File(self):
		self.win = tk.Tk()                           # Create instance      
		self.win.title("DES File GUI")                 # Add a title 
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
		self.fichier = "No Choose"

		wel = Label(panel1,text="DES File ENCRYPTION",fg="orange")
		wel.pack()

		f0 = Label(panel1,text=" ")
		
		f0.pack()

		fr = Frame(panel1)
		la = Label(fr,text="Select Your File :")
		slc = Button(fr,text="Choose...",fg='brown')
		slc.bind("<Button-1>",self.FileEnter)
		la.pack(side="left")
		slc.pack(side="right")
		fr.pack()

		f0 = Label(panel1,text=" ")
		f0.pack()

		self.fs = Label(panel1,text="File Selected : ")
		self.fs.pack()

		f0 = Label(panel1,text=" ")
		f0.pack()

		fr2 = Frame(panel1)
		l2 = Label(fr2,text="Select your key : ")
		self.theKey = StringVar()
		self.pas = Entry(fr2,show="*",textvariable=self.theKey)
		l2.pack(side="left")
		self.pas.pack(side="right")
		fr2.pack()

		f0 = Label(panel1,text=" ")
		f0.pack()

		fr3 = Frame(panel1)
		be = Button(fr3,text="ENCRYPT",fg="blue")
		be.bind("<Button-1>",self.EncryptFiles)
		bd = Button(fr3,text="DECRYPT",fg="green")
		bd.bind("<Button-1>",self.DecryptFiles)
		be.pack(side="left")
		l3 = Label(fr3,text="           ")
		l3.pack(side="left")
		bd.pack(side="right")
		fr3.pack()

		f0 = Label(panel1,text=" ")
		f0.pack()

		self.fin = ScrolledText(panel1,height=6,width=45)
		self.fin.pack()

		rs = Button(panel1,text="Reset",fg="red")
		rs.bind("<Button-1>",self.ResetFile)
		rs.pack(side="right")

		self.win.mainloop()

	def FileEnter(self,event):
		filename = filedialog.askopenfilename(initialdir = "/home/",title="Select a PUBLIC or PRIVATE KEY file :",filetypes=(('Files','*.*'),("all files","*.*")))
		if filename == "":
			filename = "No Choose"
		else:
			self.fichier = filename
		self.fs.config(text=self.fichier)
		self.Updates()

	def ResetFile(self,event):
		self.pas.delete('0',"end")
		self.fin.delete('1.0', END)
		self.fs.config(text="File Selected :")
		self.Updates()

	def EncryptFiles(self,event):
		des = DESCipher()

		if(os.path.isfile(self.fichier) == True):
			if(self.theKey.get() != ""):
				out = des.EncryptFile(self.theKey.get(),self.fichier)
				self.fin.delete('1.0', END)
				self.fin.insert(tk.INSERT,"File encryption .....\n")
				os.remove(self.fichier)
				self.fin.insert(tk.INSERT,"File encrypted.\n")
				self.fin.insert(tk.INSERT,"Close !\n OUTPUT : "+out)
				self.pas.delete('0',"end")
				self.fs.config(text="File Selected :")
				self.Updates()
			else:
				messagebox.showinfo(message="Key required \n Enter a key !")
		else:
			messagebox.showinfo(message="File Error \n This path is not valid !")


	def DecryptFiles(self,event):
		des = DESCipher()
		if(os.path.isfile(self.fichier) == True):
			if(self.theKey.get() != ""):
				try:
					out = des.DecryptFile(self.theKey.get(),self.fichier)
					self.fin.delete('1.0', END)
					self.fin.insert(tk.INSERT,"File encryption .....\n")
					os.remove(self.fichier) 
					self.fin.insert(tk.INSERT,"File encrypted.\n")
					self.fin.insert(tk.INSERT,"Close !\n OUTPUT : "+out)
					self.pas.delete('0',"end")
					self.fs.config(text="File Selected :")
					self.Updates()
				except ValueError :
					messagebox.showinfo(message="Encode Error \n This file can't be decrypt !")
				except Exception :
					messagebox.showinfo(message="Error \n Contact the devs !")

			else:
				messagebox.showinfo(message="Key required \n Enter a key !")
		else:
			messagebox.showinfo(message="File Error \n This path is not valid !")

		
		


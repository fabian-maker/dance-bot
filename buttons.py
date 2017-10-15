from tkinter import *
import os

class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.button = Button(frame, 
							 text="nehmen", fg="red",
							 command=self.write_programm)
		self.button.pack(side=LEFT)
	def write_programm(self):
		os.system("python nehmen.py")	
		self.slogan = Button(frame,
							 text="richtung",
							 command=self.write_slogan)
		self.slogan.pack(side=LEFT)
	def write_slogan(self):
		print("Tkinter is easy to use!")
		os.system("python richtung.py")

root = Tk()
app = App(root)
root.mainloop()

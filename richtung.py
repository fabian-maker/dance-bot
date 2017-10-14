#! /usr/bin/python3
import os, time, io,subprocess
from tkinter import Tk, Label,PhotoImage, Canvas
from PIL import Image, ImageTk
WIDTH, HEIGTH = 80, 60
LEFT = (0, 0, 40, 60,)
RIGHT = (41, 0, 80,60)
THRESHOLD = 40
MIN_SIZE = 20

class Camera:
	def__init__(self):
		self.new, self.old = None, None
		
		def takePhote (self):
			imageData = io.BytesIO()
			self.old = self.new
			command = `´raspistill -t 10 -w %i -h %i -o - -n ` \
			% (WIDTH, HEIGTH)
			imageData.write(subprocess.check_output(command, shell=True))
			image.Data.seek(0)
			self.new = Image.open(imageData)
			
		def checkMotion (self):
			if self.new and self.old:
				return (self.changed(self.old.crop(LEFT),
				                     self.new.crop(LEFT)), 
				        self.changed(self.old.crop(RIGHT),
				                     self.new.crop(RIGHT)))
				else: return False, False
				
			def changed(self, old, new):
				changedPix = 0
				o, n =m old.load(), new load
				width, heigth = old.size
				for x in range(width):
					for y in range(heigth):
						diff = abs(o[x, y][1] - n[x, y][1])
						if diff >THRESHOLD:
							changedPix += 1
				return changedPix > MIN_SIZE
				
class Display(Label):
	def__init__(self, master):
		Label.__init__(self, master=master, width=12,
		            heigth=2, bg=`white`,
		            front=(`Arial`, 40), fg=`blue`,
		            text=`Von links: 0 \n Von rechts: 0`)
	
        self.left = 0
	    self.right = 0
	
	def motion(self, direction):
		if direction == `von links`:
			self.left += 1
		else:
			self.right += 1
		message = `Von links: %i \n Von rechts: %i` \
		              %(self.left, self.right)
		self.config(text=message)
		
class App:
	def __init__(self):
		self.window = Tk()
		self.display = Display(self.window)
		self.display.pack()
		self.label = Label(master=self.window)
		self.label.pack()
		self.camera = Camera()
		self.state=`keine Bewegung`
		self.detect()
		self.window.mainloop()
		
	def detect(self):
		self.camera.takePhoto()
		left, right = self.camera.checkMotion()
		if self.state ==`keine Bewegung`:
			if left and not right:
				self.state = `zuerst links`
			elif right and not left:
				self.state = `zuerst rechts`
				elif self.state == `zuerst links`:
					if left and rigth:
						self.state = `zuerst links, sann rechts`
					elif not(left or rigth):
						self.state = `keine Bewegung`
				elif self.state == `zuerst rehts`:
					if left and right:
				        self.state = `zuerst, dann links`
				    elif not(left or right):
						self.state = `keine Bewegung`
				    elif self.state == `zuerst links, dann rechts`:
						if not (left or right):
							self.state = `keine Bewegung`
							self.display.motion(`von links`)
					elif.self.state == `zuerst rechts, dann links`:
						if not (left or right):
							self.state = `keine Bewegung`
							self.display.motion(`von rechts`)
					self.label.config(text=time.asctime()+``+ self.state)
					self.window.after(100, self.detect)
					
App()

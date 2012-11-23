#!/bin/env python
import gtk,os,gobject
import sys
class spy(gtk.Window):
	def __init__(self):
		super(spy,self).__init__()
		self.set_title("Spydroid")
		self.set_position(gtk.WIN_POS_CENTER)
		self.set_border_width(2)

		self.image=gtk.Image()
		os.system("chmod +x screenshot.jar")

		self.connect("destroy",gtk.main_quit)
		self.add(self.image)
		os.system("adb start-server")
		self.image.set_from_file("1.png")
		self.show_all()
		gobject.timeout_add(10,self.update)
	def update(self):
		#os.system("./screenshot.jar -l -d spy.png>/dev/null")
		os.system("./screenshot.jar -d spy.png>/dev/null")
		self.image.set_from_file("spy.png")
		gobject.timeout_add(10,self.update)
spy()
gtk.main()

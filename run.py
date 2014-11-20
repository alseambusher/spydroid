#!/bin/env python
import gtk,os,gobject
import sys

# timeout in seconds
TIMEOUT = 10
class spy(gtk.Window):
	def __init__(self):
		super(spy,self).__init__()
		self.set_title("Spydroid")
		self.set_position(gtk.WIN_POS_CENTER)
		self.set_border_width(2)

		self.image=gtk.Image()
		self.connect("destroy",gtk.main_quit)
		self.add(self.image)
		os.system("adb start-server")
		self.image.set_from_file("1.png")
		self.show_all()
		gobject.timeout_add(TIMEOUT,self.update)
	def update(self):
		#os.system("java -jar screenshot.jar -d spy.png>/dev/null")
		os.system("adb shell screencap -p /sdcard/spy.png")
		os.system("adb pull /sdcard/spy.png")
		os.system("adb shell rm /sdcard/spy.png")
		# TODO scale image
		self.image.set_from_file("spy.png")
		gobject.timeout_add(TIMEOUT,self.update)
spy()
gtk.main()

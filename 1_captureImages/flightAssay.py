#! /usr/bin/python

## Written Feb 15, 2018 by Adam Spierer
## Updated July 20, 2021 by Adam Spierer
##
## The purpose of this script is to snap a photograph of flies final landing heights
##    following the flight performance assay. This program could easily be co-opted
##    to capture a photograph of any experiment and use the GUI to name the image.
##
## NOTE: This program is written in Python 2, and is no longer supported.
##

## Specify the home folder
homeFolder = '/home/pi/Desktop/deficiency_screen/batch_21_07_15/'
print "Saving files to:",homeFolder

## Specify the default preview button display time
previewTime = 10

## Specify field labels
field_label=['mtDNA','nDNA','sex']

## Load modules
import io
import time
import os.path
import picamera 
import numpy as np
from Tkinter import *
from datetime import datetime, timedelta

## Initialize PiCamera
camera = picamera.PiCamera()

## Centers the image capture window
def center_window(w, h):
	ws = root.winfo_screenwidth()
	hs = root.winfo_screenheight()
	x = 1515 #(ws/2) -100
	y = 35 # (hs/2) - 0 
	root.geometry('%dx%d+%d+%d' % (w, h, x, y))

## Preview the capture window
def preview():
	camera.rotation = 180
	camera.resolution = (960,1280)
	camera.video_stabilization = True
	camera.start_preview()
	time.sleep(previewTime)
	camera.stop_preview()
	return

## Names of the entry fields
def show_entry_fields():
    mito = e1.get()
    geno = e2.get()
    sex = e3.get()
    fileName = mito + '_' + geno + '_' + sex + '.jpg'
    return mito,geno,fileName

## Capture a still image and name it using the specified naming variables
def still():
	mito = e1.get()
	geno = e2.get()
   	sex = e3.get()
	fileName = mito + '_' + geno + '_' + sex + '.jpg'

	## Create a list of files in folder
	fileList = set(os.listdir(homeFolder))
	_fileName = set([fileName])

	## Check to make sure the new file name is not in use, then capture image
	if _fileName.issubset(fileList):
		print 'ERROR!! File already exists'
	else:
	   	camera.preview_fullscreen = False
		camera.brightness = 60
		camera.rotation = 180
		camera.preview_window = (0, 0, 960, 1280)
		camera.resolution = (960,1280)
		print '  Capturing: ', fileName
		fileName = homeFolder + show_entry_fields()[2]
		camera.start_preview()
		camera.capture(fileName)
		time.sleep(1)
		camera.stop_preview()
		

## Create GUI instance
root = Tk()
root.title("flightCamera")
center_window(380, 150)

## Button: QUIT
quitButton = Button(root, bg="pink", text="       Quit      ", command=exit)
quitButton.grid(row=0, column=0)

## Button: PREVIEW
previewButton = Button(root, text="    Preview    ", command=preview)
previewButton.grid(row=0, column=1)

## Button: CAPTURE
takeStillButton = Button(root, bg="#66ff99", text="   Capture  ", command=still)
takeStillButton.grid(row=6, column = 1)

## Specifying homeFolder s
pathButton = Label(root, text = 'Main Directory:', ).grid(row=2, column=0)
pathButton = Label(root, text = homeFolder).grid(row=2, column=1)

## Specify Mito label
Label(root, text=field_label[0]).grid(row=3)
e1 = Entry(root)
e1.grid(row=3, column=1)

## Specify Geno label
Label(root, text=field_label[1]).grid(row=4)
e2 = Entry(root)
e2.grid(row=4, column=1)

## Specify Sex label
Label(root, text=field_label[2]).grid(row=5)
e3 = Entry(root)
e3.grid(row=5, column=1)


## Run the main GUI loop
root.mainloop()
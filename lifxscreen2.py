# Author: Frak Al-Nuaimy 
# email: frakman@hotmail.com
from threading import Thread
import threading
import lazylights
import time
from PIL import ImageGrab
from PIL import Image
import os
from colour import Color
import sys
import math
import binascii
from colorific.palette import extract_colors, rgb_to_hex

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
# GLOBAL DEFINES
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#HEIGHT         = 1920   #now using image.size[1] dynamically
#WIDTH          = 1200   #now using image.size[0] dynamically
LOOP_INTERVAL  = 1    # how often we calculate screen colour (in seconds)
DURATION       = 500    # how long it takes bulb to switch colours (in seconds)
KELVIN         = 0
DECIMATE       = 10   # skip every DECIMATE number of pixels to speed up calculation
#get your unit-unique token from http://developer.lifx.com/ and use it here
TOKEN          = "c590be9f9c544d4418437b774b3a5ab1df1966cd52c9dc3aa0d08f5f5f5b4fa7" 
BULB_NAME      = "all"  # you can use any label you've assigned your bulb here
BLACK_THRESHOLD  = 0.08 # Black Screen Detection Threshold
BLACK_BRIGHTNESS = 0.03 # Black Screen case's brightness setting
BLACK_KELVIN     = 5000 # Black Screen case's Kelvin setting
paletteL=0
paletteR=0
bulbsL = []
bulbsR = []

lock = threading.Lock()
run_once = 0

def runL():
	global bulbsL
	global bulbsR
	global lock
	
	while True:
		global paletteL
		with lock:
			#print 'Left\n'
			if paletteL.bgcolor:
				#print (type(paletteL.bgcolor))
				print("BackgroundL: ", rgb_to_hex(paletteL.bgcolor.value))
				#print("BackgroundL: ", (paletteL.bgcolor.value[0]))
				#print("BackgroundL: ", (paletteL.bgcolor.value[1]))
				#print("BackgroundL: ", (paletteL.bgcolor.value[2]))
				cB= Color(rgb=(paletteL.bgcolor.value[0]/255.0,paletteL.bgcolor.value[1]/255.0,paletteL.bgcolor.value[2]/255.0))
				lazylights.set_state(bulbsL,cB.hue*360.0,cB.saturation,cB.luminance/3.0,BLACK_KELVIN,(DURATION),False)
				time.sleep(0)
				continue
			
			if paletteL.colors[0].prominence <0.001:
				print("prominenceL: ", str(paletteL.colors[0].prominence))
				lazylights.set_state(bulbsL,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(DURATION),False)
				time.sleep(0)
				continue


			cL= Color(rgb=(paletteL.colors[0].value[0]/255.0,paletteL.colors[0].value[1]/255.0,paletteL.colors[0].value[2]/255.0))
			#print cL
			lazylights.set_state(bulbsL,cL.hue*360.0,(cL.saturation),cL.luminance,KELVIN,(DURATION),False)
			time.sleep(0)
			'''
			#print('colorsL: ' + str(cL))
			if paletteL.bgcolor:
				#print (type(paletteL.bgcolor))
				#print("BackgroundL: ", rgb_to_hex(paletteL.bgcolor.value))
				#print("BackgroundL: ", (paletteL.bgcolor.value[0]))
				#print("BackgroundL: ", (paletteL.bgcolor.value[1]))
				#print("BackgroundL: ", (paletteL.bgcolor.value[2]))
				cB= Color(rgb=(paletteL.bgcolor.value[0]/255.0,paletteL.bgcolor.value[1]/255.0,paletteL.bgcolor.value[2]/255.0))
				lazylights.set_state(bulbsL,cB.hue*360.0,cB.saturation,cB.luminance/2.0,BLACK_KELVIN,(DURATION),False)
				continue
			if paletteL.colors[0].prominence <0.001:
				print("prominenceL: ", str(paletteL.colors[0].prominence))
				lazylights.set_state(bulbsL,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(DURATION),False)
				continue
			if (cL.red < BLACK_THRESHOLD)  and (cL.green < BLACK_THRESHOLD) and (cL.blue < BLACK_THRESHOLD): 
				#print "black1 detected"
				lazylights.set_state(bulbsL,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(DURATION),False)
			else:
				lazylights.set_state(bulbsL,cL.hue*360.0,(cL.saturation),cL.luminance+0.2,KELVIN,(DURATION),False)
			'''
			

def runR():
	global bulbsL
	global bulbsR
	global lock
	while True:
		global paletteR
		with lock:
			#print 'Right\n'
			if paletteR.bgcolor:
				#print (type(paletteL.bgcolor))
				print("BackgroundR: ", rgb_to_hex(paletteR.bgcolor.value))
				#print("BackgroundR: ", (paletteR.bgcolor.value[0]))
				#print("BackgroundR: ", (paletteR.bgcolor.value[1]))
				#print("BackgroundR: ", (paletteR.bgcolor.value[2]))
				cB= Color(rgb=(paletteR.bgcolor.value[0]/255.0,paletteR.bgcolor.value[1]/255.0,paletteR.bgcolor.value[2]/255.0))
				lazylights.set_state(bulbsR,cB.hue*360.0,cB.saturation,cB.luminance/3.0,BLACK_KELVIN,(DURATION),False)
				time.sleep(0)
				continue
			
			if paletteR.colors[0].prominence <0.001:
				print("prominenceR: ", str(paletteR.colors[0].prominence))
				lazylights.set_state(bulbsR,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(DURATION),False)
				time.sleep(0)
				continue
			
			cR= Color(rgb=(paletteR.colors[0].value[0]/255.0,paletteR.colors[0].value[1]/255.0,paletteR.colors[0].value[2]/255.0))
			#print cR
			#print paletteR.colors[0].value[0]
			#print paletteR.colors[0].value[1]
			#print paletteR.colors[0].value[2]
			
			lazylights.set_state(bulbsR,cR.hue*360.0,(cR.saturation),cR.luminance,KELVIN,(DURATION),False)
			time.sleep(0)
			'''
			#print((cR))
			if paletteR.bgcolor:
				print("BackgroundR: ", rgb_to_hex(paletteR.bgcolor.value))
				cB= Color(rgb=(paletteR.bgcolor.value[0]/255.0,paletteR.bgcolor.value[1]/255.0,paletteR.bgcolor.value[2]/255.0))
				lazylights.set_state(bulbsR,cB.hue*360.0,cB.saturation,cB.luminance/2.0,BLACK_KELVIN,(DURATION),False)
				continue
			if paletteR.colors[0].prominence <0.001:
				print("prominenceR: ", str(paletteR.colors[0].prominence))
				lazylights.set_state(bulbsR,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(DURATION),False)
				continue
			if (cR.red < BLACK_THRESHOLD)  and (cR.green < BLACK_THRESHOLD) and (cR.blue < BLACK_THRESHOLD): 
				#print "black1 detected"
				lazylights.set_state(bulbsR,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(DURATION),False)
			else:
				#print cR.hue
				#rgb2hsl()
				lazylights.set_state(bulbsR,cR.hue*360.0,(cR.saturation),cR.luminance+0.2,KELVIN,(DURATION),False)
			'''
			
			
def runCap():
	global paletteL 
	global paletteR
	global lock
	global run_once
	while True:
		#lock.acquire()
		with lock:
			#print '************************** CAPTURE THREAD ************************** '
			image = ImageGrab.grab()  # take a screenshot
			left   = 50
			top    = 150
			width  = 500
			height = 350
			box    = (left, top, left+width, top+height)
			area   = image.crop(box)
			#area.show()
			#sys.exit(1)
			thumb = area.resize((128,128),Image.ANTIALIAS)

			#thumb = image.resize((128,128),Image.ANTIALIAS)
			#thumb.show()
			#sys.exit(1)
			
			w, h = thumb.size
			left  = thumb.crop((0, 0, w/2, h))
			right = thumb.crop((w/2, 0, w, h))
			
			#print image.size
			#right.show()
			#sys.exit(1)

			
			paletteL = extract_colors(left)
			paletteR = extract_colors(right)
			
			#print paletteL
			#print paletteR
			
			if run_once == 0:
				print ("Running once")
				tl = Thread(target = runL)
				tr = Thread(target = runR)
				tl.setDaemon(True)
				tr.setDaemon(True)
				tl.start()
				tr.start()
				run_once = 1
	#		lock.release()
			#print '************************** END CAPTURE THREAD ************************** '
			time.sleep(0)
def createBulb(ip, macString, port = 56700):        
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
	
if __name__ == "__main__":
	myBulb1 = createBulb('x.x.x.x','xx:xx:xx:xx:xx:xx')
	myBulb2 = createBulb('x.x.x.x','xx:xx:xx:xx:xx:xx')
	myBulb3 = createBulb('x.x.x.x','xx:xx:xx:xx:xx:xx')
	
	bulbsL=[myBulb1]
	bulbsR=[myBulb2,myBulb3]

	tCap = Thread(target = runCap)

	tCap.setDaemon(True)

	tCap.start()
	while True:
		pass
	

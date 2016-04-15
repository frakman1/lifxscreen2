# Author: Frak Al-Nuaimy 
# email: frakman@hotmail.com
import lazylights
import time
from PIL import ImageGrab
from PIL import Image
import os
from colour import Color
import sys
#import numpy
#import pyaudio
#import analyse
import math
import binascii
#from colorific import config
#from colorific.palette import (
#    extract_colors, print_colors, save_palette_as_image, color_stream_mt,
#    color_stream_st)
from colorific.palette import extract_colors, rgb_to_hex

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
# GLOBAL DEFINES
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
#HEIGHT         = 1920   #now using image.size[1] dynamically
#WIDTH          = 1200   #now using image.size[0] dynamically
LOOP_INTERVAL  = 1    # how often we calculate screen colour (in seconds)
DURATION       = 2    # how long it takes bulb to switch colours (in seconds)
KELVIN         = 0
DECIMATE       = 10   # skip every DECIMATE number of pixels to speed up calculation
#get your unit-unique token from http://developer.lifx.com/ and use it here
TOKEN          = "c590be9f9c544d4418437b774b3a5ab1df1966cd52c9dc3aa0d08f5f5f5b4fa7" 
BULB_NAME      = "all"  # you can use any label you've assigned your bulb here
BLACK_THRESHOLD  = 0.08 # Black Screen Detection Threshold
BLACK_BRIGHTNESS = 0.03 # Black Screen case's brightness setting
BLACK_KELVIN     = 5000 # Black Screen case's Kelvin setting

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
'''
# Initialize PyAudio
pyaud = pyaudio.PyAudio()

# Open input stream, 16-bit mono at 44100 Hz
# On my system, device 2 is a USB microphone, your number may differ.
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input = True)
'''
	
def createBulb(ip, macString, port = 56700):        
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
	
	
#bulbs = lazylights.find_bulbs(expected_bulbs=2,timeout=5)
#print bulbs
#print len(bulbs)
#bulb1 = bulbs.pop()
#bulbs1 = [bulb1]
#bulb2 = bulbs.pop()
#bulbs2 = [bulb2]

#myBulb1 = createBulb('10.10.10.1','xx:xx:xx:xx:xx:xx')
#myBulb2 = createBulb('10.10.10.2','xx:xx:xx:xx:xx:xx')
myBulb3L = createBulb('10.10.10.3','xx:xx:xx:xx:xx:xx')
#myBulb4 = createBulb('10.10.10.4','xx:xx:xx:xx:xx:xx')
myBulb5R = createBulb('10.10.10.5','xx:xx:xx:xx:xx:xx')
#myBulb6 = createBulb('10.10.10.6','xx:xx:xx:xx:xx:xx')
#myBulb7 = createBulb('10.10.10.7','xx:xx:xx:xx:xx:xx')


#print('MyBulb1: ' + str(myBulb1))
#print('MyBulb2: ' + str(myBulb2))
#bulbs=[myBulb1,myBulb2,myBulb3,myBulb4,myBulb5,myBulb6,myBulb7]
bulbsL=[myBulb3L]
bulbsR=[myBulb5R]

#sys.exit(1)

#print bulb1
#print bulb2
#print bulbs1
#print bulbs2

    


# run loop
while True:
	
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# CALCULATE AVERAGE SCREEN COLOUR
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	image = ImageGrab.grab()  # take a screenshot
	thumb = image.resize((128,128),Image.ANTIALIAS)
	

	w, h = thumb.size
	left  = thumb.crop((0, 0, w/2, h))
	right = thumb.crop((w/2, 0, w, h))

	#print image.size

	paletteL = extract_colors(left)
	paletteR = extract_colors(right)
    #''':type : colorific.palette.Palette'''

	#print("Colors: ", ', '.join(rgb_to_hex(c.value) for c in palette.colors))
	for c1L in paletteL.colors:
		#c = Color(c1)
		#print('colorsL: ' + str(c1L))
		cL= Color(rgb=(c1L.value[0]/255.0,c1L.value[1]/255.0,c1L.value[2]/255.0))

	if (cL.red < BLACK_THRESHOLD)  and (cL.green < BLACK_THRESHOLD) and (cL.blue < BLACK_THRESHOLD): 
		#print "black1 detected"
		lazylights.set_state(bulbsL,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(750),False)
	else:
		lazylights.set_state(bulbsL,cL.hue*360,(cL.saturation),cL.luminance,KELVIN,(750),False)

########################################################################################################################	
########################################################################################################################	

	#print("Colors: ", ', '.join(rgb_to_hex(c.value) for c in palette.colors))
	for c1R in paletteR.colors:
		#c = Color(c1)
		print('colorsR: ' + str(c1R))
		cR= Color(rgb=(c1R.value[0]/255.0,c1R.value[1]/255.0,c1R.value[2]/255.0))

	if (cR.red < BLACK_THRESHOLD)  and (cR.green < BLACK_THRESHOLD) and (cR.blue < BLACK_THRESHOLD): 
		#print "black1 detected"
		lazylights.set_state(bulbsR,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(750),False)
	else:
		lazylights.set_state(bulbsR,cR.hue*360,(cR.saturation),cR.luminance,KELVIN,(750),False)



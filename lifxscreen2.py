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

def createBulb(ip, macString, port = 56700):        
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
	
	
#bulbs = lazylights.find_bulbs(expected_bulbs=2,timeout=5)

myBulb1 = createBulb('10.10.10.1','xx:xx:xx:xx:xx:xx')
myBulb2 = createBulb('10.10.10.2','xx:xx:xx:xx:xx:xx'')
myBulb3 = createBulb('10.10.10.3','xx:xx:xx:xx:xx:xx')
myBulb4 = createBulb('10.10.10.4','xx:xx:xx:xx:xx:xx')
myBulb5 = createBulb('10.10.10.5','xx:xx:xx:xx:xx:xx')
myBulb6 = createBulb('10.10.10.6','xx:xx:xx:xx:xx:xx')
myBulb7 = createBulb('10.10.10.7','xx:xx:xx:xx:xx:xx')

bulbs=[myBulb1,myBulb2,myBulb3,myBulb4,myBulb5,myBulb6,myBulb7]

# run loop
while True:
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# CALCULATE SCREEN COLOUR
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	image = ImageGrab.grab()  # take a screenshot
	thumb = image.resize((128,128),Image.ANTIALIAS)
	#print image.size
	palette = extract_colors(thumb)
	#print("Colors: ", ', '.join(rgb_to_hex(c.value) for c in palette.colors))
	for c1 in palette.colors:
		#c = Color(c1)
		print('colors: ' + str(c1))
		c= Color(rgb=(c1.value[0]/255.0,c1.value[1]/255.0,c1.value[2]/255.0))


	
#	palette = extract_colors(area,min_saturation=config.MIN_SATURATION,min_prominence=config.MIN_PROMINENCE,min_distance=config.MIN_DISTANCE,max_colors=config.MAX_COLORS,n_quantized=config.N_QUANTIZED)
#	print_colors(palette)
#	lazylights.set_state(bulbs,c.hue*360,(c.saturation),c.luminance,KELVIN,(750),False)

	if (c.red < BLACK_THRESHOLD)  and (c.green < BLACK_THRESHOLD) and (c.blue < BLACK_THRESHOLD): 
		#print "black1 detected"
		lazylights.set_state(bulbs,0,0,BLACK_BRIGHTNESS,BLACK_KELVIN,(750),False)
	else:
		lazylights.set_state(bulbs,c.hue*360,(c.saturation),c.luminance,KELVIN,(750),False)

	



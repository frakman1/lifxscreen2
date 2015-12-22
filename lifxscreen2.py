# Author: Frak Al-Nuaimy 
# email: frakman@hotmail.com
import lazylights
import time
from PIL import ImageGrab
import os
from colour import Color
import sys
import analyse
import math
import binascii

#//////////////////////////////////////////////////////////////////////////////////////////////////////////
# GLOBAL DEFINES
#//////////////////////////////////////////////////////////////////////////////////////////////////////////
KELVIN         = 0    # 2000 to 8000, where 2000 is the warmest and 8000 is the coolest
DECIMATE       = 10   # skip every DECIMATE number of pixels to speed up calculation
#//////////////////////////////////////////////////////////////////////////////////////////////////////////

#------------------------------------------------------------------------------------------------------------
# I use this to manually create a bulb using IP and MAC address. 
def createBulb(ip, macString, port = 56700):        
    return lazylights.Bulb(b'LIFXV2', binascii.unhexlify(macString.replace(':', '')), (ip,port))
#------------------------------------------------------------------------------------------------------------	

#Scan for bulbs 	
bulbs = lazylights.find_bulbs(expected_bulbs=2,timeout=5)
print bulbs
print len(bulbs)

if (len(bulbs)==0):
    print "No LIFX bulbs found. Make sure you're on the same WiFi network and try again"
    sys.exit(1)


#These are my two bulbs. I get the values ahead of time from my router info page
myBulb1 = createBulb('10.10.10.2','XX:XX:XX:XX:XX:XX')  #Bulb for left  side of screen
myBulb2 = createBulb('10.10.10.1','XX:XX:XX:XX:XX:XX')  #Bulb for right side of screen
#print('MyBulb1: ' + str(myBulb1))
#print('MyBulb2: ' + str(myBulb2))

#lazylights requires a 'set' of bulbs as input so I put each one in its own set
bulbs1=[myBulb1]
bulbs2=[myBulb2]


# This is the Main loop
while True:
	#init counters/accumulators
	red   = 0
	green = 0
	blue  = 0
	
	# take a screenshot
	image = ImageGrab.grab()  
	#print image.size
	
	# Crop a chunk of the screen out
	# This is hacky and is currently screen and movie-size specific. 
	# To get these values, I take a screenshot and use Paint.Net to easily find the coordinates
	# TODO: clean this up and make it dynamically detect size and crop the black bits out automagically
	left   = 0      # The x-offset of where your crop box starts
	top    = 140    # The y-offset of where your crop box starts
	width  = 1920   # The width  of crop box
	height = 800    # The height of crop box
	box    = (left, top, left+width, top+height)
	area   = image.crop(box)
	#print area.size
	
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# Left Side of Screen
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	for y in range(0, area.size[1], DECIMATE):  #loop over the height
		for x in range(0, area.size[0]/2, DECIMATE):  #loop over the width (half the width in this case)
			#print "\n coordinates   x:%d y:%d \n" % (x,y)
			color = area.getpixel((x, y))  #grab a pixel
			# calculate sum of each component (RGB)
			red = red + color[0]
			green = green + color[1]
			blue = blue + color[2]
			#print red + " " +  green + " " + blue
			#print "\n totals   red:%s green:%s blue:%s\n" % (red,green,blue)
			#print color
	#print(time.clock())
	
	# calculate the averages
	red = (( red / ( (area.size[1]/DECIMATE) * (area.size[0]/DECIMATE) ) ) )/255.0
	green = ((green / ( (area.size[1]/DECIMATE) * (area.size[0]/DECIMATE) ) ) )/255.0
	blue = ((blue / ( (area.size[1]/DECIMATE) * (area.size[0]/DECIMATE) ) ) )/255.0
	
	# generate a composite colour from these averages
	c = Color(rgb=(red, green, blue))  
	#print c
	
	#print "\naverage1  red:%s green:%s blue:%s" % (red,green,blue)
	#print "average1   hue:%f saturation:%f luminance:%f" % (c.hue,c.saturation,c.luminance)
	#print "average1  (hex) "+  (c.hex)
	
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# PROGRAM LIFX BULBS (LEFT)
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	if (c.red < 0.08)  and (c.green< 0.08) and (c.blue < 0.08): 
		#print "black1 detected"
		lazylights.set_state(bulbs1,0,0,0.03,5000,(500),False)
	else:
		lazylights.set_state(bulbs1,c.hue*360,(c.saturation),c.luminance,KELVIN,(500),False)
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	
	# Clear colour accumulators in preperation for going over the second half of the screen
	red   = 0
	green = 0
	blue  = 0

	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# Right Side of Screen
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	for y in range(0, area.size[1], DECIMATE):  #loop over the height
		for x in range(area.size[0]/2, area.size[0], DECIMATE):  #loop over the width (the second half of the width)
			#print "\n coordinates   x:%d y:%d \n" % (x,y)
			color = area.getpixel((x, y))  #grab a pixel
			# calculate sum of each component (RGB)
			red = red + color[0]
			green = green + color[1]
			blue = blue + color[2]
	
	red = (( red / ( (area.size[1]/DECIMATE) * (area.size[0]/DECIMATE) ) ) )/255.0
	green = ((green / ( (area.size[1]/DECIMATE) * (area.size[0]/DECIMATE) ) ) )/255.0
	blue = ((blue / ( (area.size[1]/DECIMATE) * (area.size[0]/DECIMATE) ) ) )/255.0
	c = Color(rgb=(red, green, blue))  
	#print c
	
	#print "\naverage   red:%s green:%s blue:%s" % (red,green,blue)
	#print "average2   hue:%f saturation:%f luminance:%f" % (c.hue,c.saturation,c.luminance)
	#print "average  (hex) "+  (c.hex)
	
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	# PROGRAM LIFX BULBS (RIGHT)
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////
	if (c.red < 0.08)  and (c.green< 0.08) and (c.blue < 0.08): 
		#print "black2 detected"
		lazylights.set_state(bulbs2,0,0,0.03,5000,(500),False)
	else:
		lazylights.set_state(bulbs2,c.hue*360,(c.saturation),c.luminance,KELVIN,(500),False)
	#//////////////////////////////////////////////////////////////////////////////////////////////////////////

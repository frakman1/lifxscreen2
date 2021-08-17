<img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg">

# lifxscreen2
LIFX Movie experience. 
Continuously calculates the average colour of your screen and sets your LIFX bulb(s) to that color.

Watch movies *(or anything you want on your screen)* in style. Like [THIS!](https://youtu.be/WHCtUvEJXq0)

![image](https://user-images.githubusercontent.com/5826484/129788092-e4969cd2-8238-430c-a69d-73ffbd7870a3.png)


(*seeks to improve over the original lifxscreen at https://github.com/frakman1/lifxscreen*)

- This version uses the much faster LAN protocol (vs the slower HTTP API).
- Splits the screen into left and right segments and allows you to control two sets of bulbs independently. 
- Crops the screen so as not to take the black portion into account when calculating the average colour. 
- Better black screen colour handling. 


Tested on a Windows-7, 64bit machine. Python version 2.7.5. 

##Prerequisites:

* [PIL](http://effbot.org/downloads) - Screen Grabber which relies on [VCForPython27](http://www.microsoft.com/en-us/download/details.aspx?id=44266)

* colour - Colour Convertions and Manipulations  (https://pypi.python.org/pypi/colour/)

* lazylights - The actual LIFX driver.  https://github.com/mpapi/lazylights/tree/2.0

(Be sure to install the 2.0 branch of lazylights)
```pip install git+https://github.com/mpapi/lazylights@2.0```


* Around line 41 *(createBulb('10.10.10.2','XX:XX:XX:XX:XX:XX'))* , Replace both the IP address and **'XX:XX:XX:XX:XX:XX'** with the MAC addresses of your bulbs. You should be able to find the MAC Address on the bulb itself, or on your router page, or by using my iOS app [LIFX Ambience](https://apps.apple.com/au/app/lifx-ambience/id1012474625#?platform=iphone)

![image](https://user-images.githubusercontent.com/5826484/129788952-ddad1de1-9379-4bfb-a2d7-b4e6a784d3ad.png)


##Syntax:

```
python lifxscreen2.py
```

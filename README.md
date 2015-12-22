# lifxscreen2
LIFX Movie experience. 
Continuously calculates the average colour of your screen and sets your LIFX bulb(s) to that color

(*seeks to improve over the original lifxscreen at https://github.com/frakman1/lifxscreen2*)

- This version uses the much faster LAN protocol (vs the slower HTTP API).
- Splits the screen into left and right segments and allows you to control two sets of bulbs independently. 
- Crops the screen so as not to take the black portion into account when calculating the average colour. 
- Better black screen colour handling. 


Tested on a Windows-7, 64bit machine. Python version 2.7.5. 

##Prerequisites:

PIL - Screen Grabber (which relies on VCForPython27: http://www.microsoft.com/en-us/download/details.aspx?id=44266)

colour - Colour Convertions and Manipulations  (https://pypi.python.org/pypi/colour/)

lazylights - The actual LIFX controller.  https://github.com/mpapi/lazylights/tree/2.0

##Syntax:

```
python lifxscreen2.py
```

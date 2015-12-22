# lifxscreen2
LIFX Movie experience 
Continuously calculates the average colour of your screen and sets your LIFX bulb(s) to that color


- This version uses the much faster LAN protocol (vs the slower HTTP API).
- Splits the screen into left and right segments and allows you to control two sets of bulbs independently. 
- Crops the screen so as not to take the black portion into account when calculating the average colour. 
- Better black colour handling. 


I use this on a windows 7 64bit machine. Python version 2.7.5. 

##Prerequisites:

PIL (which relies on VCForPython27: http://www.microsoft.com/en-us/download/details.aspx?id=44266)

colour (https://pypi.python.org/pypi/colour/)

lazylights - The actual LIFX controller.  https://github.com/mpapi/lazylights/tree/2.0

##Syntax:

```
python lifxscreen2.py
```

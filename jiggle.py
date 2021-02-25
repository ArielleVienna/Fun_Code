#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      bglybra
#
# Created:     17/01/2020
# Copyright:   (c) bglybra 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pyautogui,  sys, os, datetime
from time import sleep

pyautogui.FAILSAFE = False

screensize = pyautogui.size() # warning - this sees dual screens as one screen.
sizelist = list(screensize)
halfsize = list(map(lambda z: int(z/1.05), sizelist)) # get rid of /2 if you want the full screen effect.
halfsizeplus = list(map(lambda y: int(y+1), halfsize))
tuplehalfsize = tuple(halfsize)
tuplehalfsizeplus = tuple(halfsizeplus)

whereismouse = pyautogui.position() # returns tuple.
x = 0

print("\n\n\t\t\t*** JIGGLING ***\n\n\n")

while (whereismouse < tuplehalfsize): # top left quadrant of screen.
    currenttime = str(datetime.datetime.now()).split(' ')[1] # only show current time of day.
    print currenttime
    dropdeadtime = '16:15:00.000000' # set when you want to stop working.
    if currenttime < dropdeadtime:
        print 'stay on'
        for x in range(0,5): # jiggle 5 times.ome
            
            pyautogui.moveTo(whereismouse[0]-5,whereismouse[1]) # moves mouse to X of 100, Y of 200.
            pyautogui.moveTo(whereismouse[0]+5,whereismouse[1])
            pyautogui.press(['f15']) # press the left arrow key 4 times.
            x+=1
            pyautogui.moveTo(whereismouse)
        sleep(60)  # wait then start jiggling again.
        whereismouse = pyautogui.position()
    else:
        print 'shutdown'
        os.system('shutdown -s') # shuts down computer at time specified in dropdeadtime variable.
        quit()
if (whereismouse > tuplehalfsizeplus): # move away from  top left quadrant.
    sys.exit() # jiggling ends 
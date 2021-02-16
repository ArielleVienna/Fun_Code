import pyautogui, sys, os, datetime
from time import sleep

pyautogui.FAILSAFE = False

screensize = pyautogui.size()
sizelist = list(screensize)
halfsize = list(map(lambda z: int(z/1.05), sizelist))
halfsizeplus = list(map(lambda y: int(y+1), halfsize))
tuplehalfsize = tuple(halfsize)
tuplehalfsizeplus = tuple(halfsizeplus)

whereismouse = pyautogui.position()
x = 0

print("Jiggle Start")

while(whereismouse < tuplehalfsize):
  currenttime = str(datetime.datetime.now()).split(' ')[1] #show current time
  print(currenttime)
  stoptime = '16:00:00.000000'
  if currenttime < stoptime:
    print('Stay On')
    for x in range(0,5):
      pyautogui.moveTo(whereismouse[0]-5, whereismouse[1])
      pyautogui.moveTo(whereismouse[0]+5, whereismouse[1])
      pyautogui.press(['f15'])
      x+=1
      pyautogui.moveTo(whereismouse)
    sleep(180)
    whereismouse = pyautogui.position()
  else:
    print('Quitting')
    sys.exit()
if (whereismouse > tuplehalfsizeplus):
  sys.exit()

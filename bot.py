import pyautogui as pgui
import pydirectinput as pimp
from time import sleep
import keyboard as kb

lavas = ['imgs/lava1.png', 'imgs/lava2.png', 'imgs/lava3.png']

# danger, lava
def lavaSearcher():
  is_lava = []
  lava_i = 0
  while lava_i < len(lavas):
    lava_item = pgui.locateCenterOnScreen(lavas[lava_i], confidence = 0.42)
    print(lava_item)
    if lava_item is None:
      is_lava.append(False)
    else:
      is_lava.append(True)
    lava_i +=1

  if True in is_lava:
    return True
  else:
    return False
  
#move and dig
def moveAndDig():
  pimp.keyDown('shiftleft')
  pimp.keyDown('w')
  pimp.mouseDown()


#stop
def stop():
  pimp.keyUp('w')
  pimp.keyUp('s')
  pimp.keyUp('d')
  pimp.mouseUp()
  pimp.keyUp('shiftleft')


#go back:
def back():
  stop()
  pimp.keyDown('s')
  sleep(1.5)
  stop()

#go right:
def right():
  pimp.keyDown('d')
  sleep(0.42)
  stop()



#bot start:
sleep(3)
timer = 0
while timer < 50:
  if kb.is_pressed('tab'):
    stop()
    break
  if lavaSearcher() is True:
    print("LAVA HERE")
    back()
    right()
    moveAndDig()

  moveAndDig()
  
  sleep(0.5)
  timer+=1
else:
  stop()
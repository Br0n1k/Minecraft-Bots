import pyautogui as pgui
import pydirectinput as pimp
from time import sleep
import keyboard as kb

lavas = ['imgs/lava1.png', 'imgs/lava2.png', 'imgs/lava3.png', 'imgs/lava4.png']

# danger, lava
def lava_searcher():
  is_lava = []
  lava_i = 0
  while lava_i < len(lavas):
    lava_item = pgui.locateCenterOnScreen(lavas[lava_i], confidence = 0.42)
    # print(lava_item)
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
def move_and_dig():
  pimp.keyDown('shiftleft')
  pimp.keyDown('w')
  pimp.mouseDown()
  print('move and dig')

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

#pause loop
def pause():
  print("bot paused")
  p_timer = 0
  while p_timer < 125:
    if kb.is_pressed('v'):
      p_timer = 9999
      bot_loop()
    if kb.is_pressed('tab'):
      stop()
      p_timer = 9999
      break
    else:
      sleep(0.25)
      p_timer+=1


#bot mining loop:
def bot_loop():
  print("start mining")
  timer = 0
  while timer < 250:
    if kb.is_pressed('tab'):
      print("tab")
      stop()
      timer = 99999
      break
    if kb.is_pressed('c'):
      timer = 99999
      stop()
      pause()
      break
    if lava_searcher() is True:
      print("LAVA HERE")
      back()
      right()
      move_and_dig()
    else:
      move_and_dig()
      sleep(0.25)
      timer+=1
  else:
    stop()

#start program:
sleep(2)
pause()
import pyautogui as pgui
import pydirectinput as pimp
from time import sleep
import keyboard as kb
import cv2

# automove:

# move forward
def move_forward_and_mine():
  pimp.keyDown('shiftleft')
  pimp.keyDown('w')
  pimp.mouseDown()
  sleep(2)
  stop_moving()
  pimp.mouseUp()

# stop moving
def stop_moving():
  pimp.keyUp('w')
  pimp.keyUp('s')

# danger, lava
def lava_searcher():
  is_lava = pgui.locateCenterOnScreen('imgs/lava1.jpg', confidence = 0.35)

  if is_lava is None:
    return False
  else:
    pimp.keyUp('w')
    pimp.keyDown('s')
    sleep(2)
    pimp.keyUp('s')
    return True
  


# starting and going:
sleep(3)
timer = 0
while timer < 300:
  lava_check = lava_searcher()

  if kb.is_pressed('tab'):
    timer = 9999
    pimp.keyUp('shiftleft')
    break
  if lava_check is True:
    print('LAVAAAA!!11')
    timer = 9999
    pimp.keyUp('shiftleft')
    break
  move_forward_and_mine()
  timer += 1
else:
  pimp.keyUp('shiftleft')





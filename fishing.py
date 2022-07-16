import cv2
import pyautogui as pgui
import pydirectinput as pimp
from time import sleep
import keyboard as kb
import mss
import numpy as np


#fishing:

#masks:
sct = mss.mss()
low_red0 = np.array([170, 80, 80])
up_red0 = np.array([180, 255, 255])
low_red1 = np.array([0, 80, 80])
up_red1 = np.array([10, 255, 255])

def fishing():
    #scan window:
    my_pos = pgui.position()
    my_start_pos = (my_pos[0] - 100, my_pos[1] - 200)
    my_region = {"left": my_start_pos[0], "top": my_start_pos[1], "width": 200, "height": 200}

    #screenshots and HSV mask stuff:
    def checking():
        img = np.asarray(sct.grab(my_region))
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask0 = cv2.inRange(img_HSV, low_red0, up_red0)
        mask1 = cv2.inRange(img_HSV, low_red1, up_red1)
        mask = mask0 + mask1
        is_bobber = np.sum(mask)

        #to show what's going on (for debug):
        # img_m = cv2.bitwise_and(img, img, mask = mask)
        # cv2.imshow("look at me", img_m)
        # cv2.waitKey(1)

        return is_bobber

    #check:
    if checking() > 0:
        print('Bobber is still here')
    else:
        print('NOT bobber, biting!')
        sleep(0.2)
        print(checking())
        print('doublecheck')
        if checking() == 0:
            pimp.rightClick()
            sleep(0.5)
            pimp.rightClick()
            sleep(1)
    

#img check (bad results):
    # is_bobber = pgui.locateCenterOnScreen('imgs/bobber.png', region = my_region, confidence = 0.38)

# if is_bobber is None:
    #     print('no bobber here')
    # else:
    #     print('bobber IS HERE')


#bot fishing loop:
def bot_loop():
    print("start fishing")
    timer = 0
    while timer < 36000:
        if kb.is_pressed('tab'):
            print("exit")
            timer = 99999
            #to show what's going on (for debug) part 2:
            # cv2.destroyAllWindows()
            break
        else:
            fishing()
            sleep(0.1)
            timer+=1

#start program:
# pgui.FAILSAFE = False
sleep(3)
bot_loop()
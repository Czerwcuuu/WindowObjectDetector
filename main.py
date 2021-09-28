import numpy as np
import cv2 as cv
import os
from time import time
from vision import Vision
from PIL import ImageGrab
import win32gui
import win32ui
import win32con

import pyautogui
from windowcaputre import WindowCapture

os.chdir(os.path.dirname(os.path.abspath(__file__)))


wincap = WindowCapture('TimbermanVS')
pipe0 = Vision('test1.jpg')
pipe1 = Vision('test2.jpg')
head = Vision('head.jpg')

loop_time = time()
while (True):
    screenshot = wincap.window_capture()

    #cv.imshow('PCVision' , screenshot)
    pipe0.find(screenshot, 0.7,'rectangles')
    pipe1.find(screenshot, 0.7, 'rectangles')
    #head.find(screenshot , 0.7 , 'rectangles')

    #print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Koniec')

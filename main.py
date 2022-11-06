import cv2 as cv
import time 
import pyautogui
import win32gui,win32ui,win32con
from screen_camera import WindowCapture

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

wincap = WindowCapture('Task Manager') #<< Window name
loop_time = time.time()

f_m = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while(True):
    screenshot = wincap.get_screenshot()
    # screenshot = pyautogui.screenshot()
    # screenshot = np.array(screenshot)
    # screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)


    g_s = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)
    f = f_m.detectMultiScale(g_s)

    for (x,y,w,h) in f:
        cv.rectangle(screenshot,(x,y),(x+w,y+h),(15,223,0), 2)
    cv.imshow('Computer Vision',screenshot)
    print('FPS {}'.format(1/ (time.time()-loop_time)))
    loop_time = time.time()
    if cv.waitKey(1) == ord('q'):
        break
cv.destroyAllWindows()
print('Done.')

# f_m = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# time_start = time.time()
# img = cv.imread('image.jpg')
# g_s = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# f = f_m.detectMultiScale(g_s)

# for (x,y,w,h) in f:
#     cv.rectangle(img,(x,y),(x+w,y+h),(255,255,255), 2)

# time_end = time.time()
# print("time :",time_end-time_start)

# cv.imshow('image', img)
# cv.waitKey(0)



# time_end = time.time()
# print("time :",time_start - time_end)
# cv.destroyAllWindows()
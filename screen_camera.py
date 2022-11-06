from time import time
import cv2 as cv
import numpy as np
import os 
import pyautogui
import win32gui,win32ui,win32con

os.chdir(os.path.dirname(os.path.abspath(__file__)))
class WindowCapture:
    w = 0
    h = 0
    
    def __init__(self,window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        # self.hwnd = 132356
        # self.hwnd = win32gui.FindWindow(None, "Windows Explorer")
        print(self.hwnd)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        window_rect = win32gui.GetWindowRect(self.hwnd)
        border_pixels = 8
        titlebar_pixels = 30
        self.w = window_rect[2]-window_rect[0]
        self.h = window_rect[3]-window_rect[1]
        self.croppend_x = border_pixels
        self.croppend_y = titlebar_pixels

        self.offset_x = window_rect[0] + self.croppend_x
        self.offset_y = window_rect[1] + self.croppend_y
    def get_screenshot(self):
        # bmpfilenamename = "out.bmp" #set this
        w,h,hwnd = self.w,self.h,self.hwnd
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj=win32ui.CreateDCFromHandle(wDC)
        cDC=dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0,0),(w, h) , dcObj, (self.croppend_x,self.croppend_y), win32con.SRCCOPY)
        # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (h, w,4)
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        # img = img[...,:3]

        return img
    
    def get_screen_position(self,pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)
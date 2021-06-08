from selenium import webdriver
from pynput.keyboard import Key, Controller
import pyautogui
import time
import os

img_folder_path = 'C://Users//Abhay//Documents//abhay//'
dirListing = os.listdir(img_folder_path)

j=len(dirListing)    
i = 1
while i <= j:
    browser = webdriver.Chrome(executable_path=r'C:\\Selenium\chromedriver.exe')
    browser.maximize_window()

    browser.get('https://www.onlineocr.net/')

    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    time.sleep(1)

    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.typewrite('C:\\Users\\Abhay\\Documents\\abhay')
    time.sleep(1)

    pyautogui.press('enter')
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")          
    time.sleep(2)
    pyautogui.press("right",i)
    pyautogui.press("left")
    pyautogui.press('enter')#taking file
    time.sleep(2)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press('enter')#text ocr
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press("tab")
    pyautogui.press('enter')  
    time.sleep(5)
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press('enter')
    time.sleep(2)
    browser.quit()


    i += 1

import pyautogui
import time

def mouse_click():
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position()
    pyautogui.moveTo(540, 580)
    pyautogui.click()

#mouse_click()
# result = True
#
# while (result):
#     time.sleep(5)
#     mouse_click()
#     result = False
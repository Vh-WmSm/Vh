from pyautogui import *
from time import sleep
while True:
    location = locateOnScreen('c:\\users\\vh\\desktop\\desktop\\hongbao.png', confidence=0.97)
    sleep(2)
    if location:
        click(center(location))
        moveTo(2000, 300)
        print('find one')

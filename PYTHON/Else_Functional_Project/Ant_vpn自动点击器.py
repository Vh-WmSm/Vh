import pyautogui
import time


jud = input('1.点击后鼠标回到原位点击一下。2.点击后鼠标只回到原位：')
# 运行前暂停2秒时间，等待把鼠标移到click按钮上
time.sleep(2)

click_position = pyautogui.position()
while True:
    now_position = pyautogui.position()
    pyautogui.click(click_position)
    if jud == '1':
        pyautogui.click(now_position)
    else:
        pyautogui.moveTo(now_position)
    time.sleep(10)


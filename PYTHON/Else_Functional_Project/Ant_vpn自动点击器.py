import pyautogui
import time

# 运行前暂停2秒时间，等待把鼠标移到click按钮上
time.sleep(2)
click_position = pyautogui.position()
while True:
    now_position = pyautogui.position()
    pyautogui.click(click_position)
    pyautogui.moveTo(now_position)
    time.sleep(10)


import playsound
import time
from public_tools import PySimpleGUI_Tool

nz = PySimpleGUI_Tool(['时', '分'])
hour, min_ = nz.return_parameter_by_window()
while True:
    t = time.localtime()
    if t.tm_hour == int(hour) and t.tm_min == int(min_):
        playsound.playsound('E:\\tools\\music.mp3')
        break
    time.sleep(20)


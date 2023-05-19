import subprocess
import time
from pyautogui import *

def end(ti):
    time.sleep(ti)
    keyDown('win')
    press('D')
    keyUp('win')
    time.sleep(0.2)
    keyDown('alt')
    press('tab')
    press('tab')
    keyUp('alt')
    time.sleep(0.2)
    press('shift')
    time.sleep(0.2)
    press('q')

def rec(max):
    subprocess.Popen(
                'ffmpeg -f dshow -rtbufsize 1000M -i audio="virtual-audio-capturer"'
                ' -f gdigrab -i desktop -r 20 -b:v 150k -b:a 225k -ar 48000 -crf 30 rec{}.mp4'.format(max))

if __name__ == '__main__':
    fen, miao = map(int, input('结束时间(分 秒)：').split())
    ti = fen * 60 + miao
    address_0 = 'C:\\Users\\vh\\Desktop'
    os.chdir(address_0)
    if os.path.exists('rec'):
        os.chdir('rec')
    else:
        os.mkdir('rec')
        os.chdir('rec')
    address = '{}\\rec'.format(address_0)
    lis = os.listdir(address)
    lis_ = []
    max = 0
    for i in lis:
        if '.mp4' in i:
            lis_.append(i)
            num = i.split('.', 1)[0].split('rec')[1]
            if num.isdigit():
                if int(num) > max:
                    max = int(num)
    rec(max + 1)
    end(ti)

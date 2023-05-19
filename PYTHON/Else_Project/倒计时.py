import time
import playsound

time_ = input('请输入倒计时(分 秒)：').split()
min = int(time_[0])
sec = int(time_[1])
count = 1
if sec == 0:
    min -= 1
    sec = 60
for i in range(min, -1, -1):
    if count == 1:
        for j in range(sec - 1, -1, -1):
            print('{}:{}'.format(i, j))
            count += 1
            time.sleep(1)
    else:
        for j in range(59, -1, -1):
            print('{}:{}'.format(i, j))
            time.sleep(1)
for i in range(2):
    playsound.playsound('c:\\users\\vh\\desktop\\rec\\铃声.mp3')


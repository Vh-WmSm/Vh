import os
import sys


def rec(max, choice, name):
    if name == '':
        name = max
    if choice == '1':
        order = 'ffmpeg -f gdigrab -thread_queue_size 100 -i desktop -r 20 -b:v 150k -crf 30 {}.mp4'.format(name)
    elif choice == '2':
        order = 'ffmpeg -f dshow -rtbufsize 200M -thread_queue_size 500 -i audio="virtual-audio-capturer"' \
                ' -f gdigrab -thread_queue_size 300 -i desktop -r 20 -b:v 150k -b:a 225k -ar 48000 -crf 30 {}.mp4'.format(name)
    elif choice == '3':
        order = 'ffmpeg -f dshow -rtbufsize 200M -thread_queue_size 100 -i audio="麦克风阵列 (英特尔® 智音技术)"' \
                ' -f gdigrab -thread_queue_size 300 -i desktop -r 20 -b:v 150k -b:a 225k -ar 48000 -crf 30 {}.mp4'.format(name)
    elif choice == '4':
        order = 'ffmpeg -f dshow -rtbufsize 200M -thread_queue_size 500 -i audio="virtual-audio-capturer"' \
                ' -f dshow -rtbufsize 200M -thread_queue_size 100 -i audio="麦克风阵列 (英特尔® 智音技术)" ' \
                '-filter_complex amix=inputs=2 -f gdigrab -thread_queue_size 300 -i desktop -r 20 -b:v 150k ' \
                '-b:a 225k -ar 48000 -crf 30 {}.mp4'.format(name)
    else:
        print('输入错误，退出程序！')
        sys.exit()
    os.system(order)


if __name__ == '__main__':
    desktop_path = 'C:\\Users\\vh\\Desktop'
    name = input('文件名(不写默认1、2、3...)、(不用加.mp4后缀)：')
    choice = input('选择录屏模式：\n1.录屏。\n2.录屏+内声。\n3.录屏+外声。\n4.录屏+内声+外声。\n请输入：')
    os.chdir(desktop_path)
    if not os.path.exists('rec'):
        os.mkdir('rec')
    os.chdir('rec')
    rec_path = desktop_path + '\\rec'
    lis = os.listdir(rec_path)
    max = 0
    for i in lis:
        num = i[:i.rfind('.mp4')]
        if num.isdigit():
            if int(num) > max:
                max = int(num)
    rec(max + 1, choice, name)

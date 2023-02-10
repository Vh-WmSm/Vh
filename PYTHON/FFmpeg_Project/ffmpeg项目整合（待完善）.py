# coding=gbk
import os


def menu():
    print('请输入要完成的功能：')
    print('''1.剪切   2.转换成gif    3.截图    4.录屏''')
    choice = int(input('请输入：'))
    return choice


def local():
    local = input('请输入文件的所在目录：')
    os.chdir(local)
    file = input('你想操作的文件是：')
    return file


def To():
    to = input('请输入文件夹目录：')
    os.chdir(to)


# ffmpeg -in.mp4 -ss 00:00:10 -to 00:00:15 -vcodec copy out.mp4
def cut():
    file = local()
    suffix = file.split('.')[1]  # 得到文件的后缀名
    print('请设置剪切开始位置和终了位置：（格式：00:00:00）')
    start = input('开始：')
    end = input('终了：')
    name = input('输出文件名：')
    order = 'ffmpeg -i {} -ss {} -to {} {}.{}'.format(file, start, end, name, suffix)
    os.system(order)
    print('Successful!')


# ffmpeg -i in.mp4 -ss 7.5 -to 8.5 -s 640x320 -r 15 out.gif
def gif():
    file = local()
    start = input('转换开始时间：（格式：00:00:00）')
    end = input('转换终了时间：')
    name = input('输出文件名：')
    order = 'ffmpeg -i {} -ss {} -to {} -r 15 {}.gif'.format(file, start, end, name)
    os.system(order)
    print('Successful!')


# ffmpeg -i in.mp4 -ss 5 -vframes 1 img.jpg
def png():
    file = local()
    time = input('截图时间：（格式：00:00:00）')
    name = input('图片名：')
    order = 'ffmpeg -i {} -ss {} -vframes 1 {}.png'.format(file, time, name)
    os.system(order)
    print('Successful!')


def screen_recording():
    To()
    os.system('ffmpeg -f gdigrab -i desktop rec.mp4')


if __name__ == '__main__':
    choice = menu()
    if choice == 1:
        cut()
    if choice == 2:
        gif()
    if choice == 3:
        png()
    if choice == 4:
        screen_recording()

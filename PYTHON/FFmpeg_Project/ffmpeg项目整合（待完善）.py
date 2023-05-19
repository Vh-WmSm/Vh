# coding=gbk
import os


def menu():
    print('������Ҫ��ɵĹ��ܣ�')
    print('''1.����   2.ת����gif    3.��ͼ    4.¼��''')
    choice = int(input('�����룺'))
    return choice


def local():
    local = input('�������ļ�������Ŀ¼��')
    os.chdir(local)
    file = input('����������ļ��ǣ�')
    return file


def To():
    to = input('�������ļ���Ŀ¼��')
    os.chdir(to)


# ffmpeg -in.mp4 -ss 00:00:10 -to 00:00:15 -vcodec copy out.mp4
def cut():
    file = local()
    suffix = file.split('.')[1]  # �õ��ļ��ĺ�׺��
    print('�����ü��п�ʼλ�ú�����λ�ã�����ʽ��00:00:00��')
    start = input('��ʼ��')
    end = input('���ˣ�')
    name = input('����ļ�����')
    order = 'ffmpeg -i {} -ss {} -to {} {}.{}'.format(file, start, end, name, suffix)
    os.system(order)
    print('Successful!')


# ffmpeg -i in.mp4 -ss 7.5 -to 8.5 -s 640x320 -r 15 out.gif
def gif():
    file = local()
    start = input('ת����ʼʱ�䣺����ʽ��00:00:00��')
    end = input('ת������ʱ�䣺')
    name = input('����ļ�����')
    order = 'ffmpeg -i {} -ss {} -to {} -r 15 {}.gif'.format(file, start, end, name)
    os.system(order)
    print('Successful!')


# ffmpeg -i in.mp4 -ss 5 -vframes 1 img.jpg
def png():
    file = local()
    time = input('��ͼʱ�䣺����ʽ��00:00:00��')
    name = input('ͼƬ����')
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

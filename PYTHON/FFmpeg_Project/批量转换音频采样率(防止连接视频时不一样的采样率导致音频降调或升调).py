# coding=gbk
from os import chdir
from os import system

location = input('�ļ�������λ�ã�')
ar = input('Ҫת���Ĳ����ʣ�')
chdir(location)
file = input('������Ҫת����Ƶ�����ʵ�mp4�ļ�����������׺���ո�ָ�����').split(' ')
i = 0
for fi in file:
    file[i] = fi + '.mp4'
    i += 1
for fi in file:
    order = 'ffmpeg -i {} -ar {} -vcodec copy z{}'.format(fi, ar, fi)
    system(order)

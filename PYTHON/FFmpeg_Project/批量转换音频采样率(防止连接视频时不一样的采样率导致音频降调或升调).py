# coding=gbk
from os import chdir
from os import system

location = input('文件夹所在位置：')
ar = input('要转换的采样率：')
chdir(location)
file = input('请输入要转换音频采样率的mp4文件名（不带后缀，空格分隔）：').split(' ')
i = 0
for fi in file:
    file[i] = fi + '.mp4'
    i += 1
for fi in file:
    order = 'ffmpeg -i {} -ar {} -vcodec copy z{}'.format(fi, ar, fi)
    system(order)

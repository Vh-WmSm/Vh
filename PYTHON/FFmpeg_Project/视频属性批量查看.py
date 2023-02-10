# coding=gbk
import os

location = input('文件夹所在位置：')
os.chdir(location)
file = input('请输入要查看参数的mp4文件名（不带后缀，空格分隔）：').split(' ')
i = 0
for fi in file:
    file[i] = fi + '.mp4'
    i += 1
for fi in file:
    order = 'ffprobe {}'.format(fi)
    os.system(order)
input('输入任意以继续……')

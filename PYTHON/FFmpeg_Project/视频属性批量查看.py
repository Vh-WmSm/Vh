# coding=gbk
import os

location = input('�ļ�������λ�ã�')
os.chdir(location)
file = input('������Ҫ�鿴������mp4�ļ�����������׺���ո�ָ�����').split(' ')
i = 0
for fi in file:
    file[i] = fi + '.mp4'
    i += 1
for fi in file:
    order = 'ffprobe {}'.format(fi)
    os.system(order)
input('���������Լ�������')

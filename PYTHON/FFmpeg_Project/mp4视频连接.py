# coding=gbk
from os import chdir
from os import system

location = input('�ļ�������λ�ã�')
chdir(location)
file = input('������Ҫ���ӵ�mp4�ļ�����������׺���ո�ָ�����').split(' ')
name = input('����ļ�����������׺����')
li = open(location + '\\list.txt', 'w')
for fi in file:
    li.write('file ' + "'" + '{}'.format(fi) + '.mp4' + "'\n")
li.close()
order = 'ffmpeg -f concat -i list.txt -c copy {}.mp4'.format(name)
system(order)
system('@echo y|del list.txt')

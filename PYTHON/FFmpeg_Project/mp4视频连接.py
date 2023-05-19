# coding=gbk
from os import chdir
from os import system

location = input('文件夹所在位置：')
chdir(location)
file = input('请输入要连接的mp4文件名（不带后缀，空格分隔）：').split(' ')
name = input('输出文件名（不带后缀）：')
li = open(location + '\\list.txt', 'w')
for fi in file:
    li.write('file ' + "'" + '{}'.format(fi) + '.mp4' + "'\n")
li.close()
order = 'ffmpeg -f concat -i list.txt -c copy {}.mp4'.format(name)
system(order)
system('@echo y|del list.txt')

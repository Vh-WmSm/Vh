# coding=gbk
import os

path = input('请输入视频所在文件夹：')
os.chdir(path)
os.system('@echo y|del *.xml')
names = os.listdir(path)
names_ = ''.join(names).split('.mp4')
lenth = len(names_)-1
names__ = names_[0:lenth]
for name in names__:
    order = 'ffmpeg -i "{}.mp4" -vn -filter:a "volume=0.01" "{}.mp3"'.format(name,name)
    os.system(order)
os.system('@echo y|del *.mp4')

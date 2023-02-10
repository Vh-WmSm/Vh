import os

address = input('地址：')
name = input('文件名（直接空格默认out.mp3）：')
if name == '':
    name = 'out'

#name_index = address.rfind('\\')
#name = address[name_index + 1:]



os.chdir(address)
lis = os.listdir()
lis.sort(key=lambda x:int(x[:-4]))
str_ = 'concat:' + '|'.join(lis)
order = 'ffmpeg -i ' + '"{}"'.format(str_) + ' -acodec copy "{}".mp3'.format(name)
os.system(order)
#print(order)

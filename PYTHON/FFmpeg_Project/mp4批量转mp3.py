import os

address = input('位置：')
os.chdir(address)
lis = os.listdir()
for li in lis:
    spl = li.split('.')
    if spl[1] == 'mp4':
        name = spl[0]
        order = 'ffmpeg -i {} {}.mp3'.format(li, name)
        os.system(order)

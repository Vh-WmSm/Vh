import os
import public_tools



path = input('路径(直接空格默认桌面):')
if path == '':
    path = public_tools.My_Tool.get_desktop_path()
os.chdir(path)
lis = os.listdir()
s = ''
try:
    if 'temp' not in lis:
        os.mkdir('temp')
except:
    pass
for li in lis[:-1]:
    if '.mp4' in li:
        s += f'ffmpeg -i {li} -acodec copy -b:v 200k temp\\{li} && '
s += f'ffmpeg -i {li} -acodec copy -b:v 200k temp\\{li}'
os.system(s)

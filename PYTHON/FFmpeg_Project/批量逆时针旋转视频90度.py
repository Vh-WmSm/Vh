# 一次不能太多，因为会超过cmd输入内容上限，以后有必要就优化
import os

desktop_path = 'c:\\users\\vh\\desktop'
path = input('位置(直接回车默认桌面)：')
if path == '':
    path = desktop_path
os.chdir(path)
file_list = os.listdir()
order_str = ''
original_move_order = ''
for li in file_list:
    if '.mp4' in li:
        name = li.split('.mp4')[0]
        order_str += f'ffmpeg -i "{name}".mp4 -metadata:s:v rotate="90" -c copy "{name}_".mp4 & '
        original_move_order += f'move "{name}".mp4 original & '

os.system(order_str)

os.mkdir('original')

os.system(original_move_order)


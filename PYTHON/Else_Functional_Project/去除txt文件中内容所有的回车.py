# 此功能用在从网上复制下来一段话，或截图识字后粘贴到txt后由换行符的情况
# 要保持它还是一段话，则要去除所有换行符
import os

desktop_path = 'c:\\users\\vh\\desktop'
path = input('txt文件位置(直接回车默认桌面)：')
if path == '':
    path = desktop_path
os.chdir(path)
file_name = input("txt文件名(不加后缀)：")
f_r = open(desktop_path + '\\' + file_name + ".txt", 'r', encoding='utf-8')
content = f_r.read()
space_out = ''.join(content.split())
else_out = ''
for i in space_out:
    if i != '' and i != '':
        else_out += i
print(else_out)

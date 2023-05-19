# 运行此py前务必先把“pdf转图片”主py文件运行窗口关掉，否则有占用
import os

address = 'c:\\users\\vh\\desktop'
os.chdir(address)
with open('1.txt', 'r') as f:
    text = f.read()

order = text[:-1]
next_dir_index = int(text[-1])
os.chdir(address + '\\{}'.format(next_dir_index))
os.system(order)

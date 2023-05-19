import os
import chardet

path = input('文件地址：')
file_name = input('文件名(要加后缀)：')
f = open(path + '\\' + file_name, 'rb')  # 由于chardet.detect只接收bytes型，所以用rb
content = f.read()
data_dict = chardet.detect(content)
print(data_dict)
print(data_dict['encoding'])


'''
a = '123'.encode('utf-8')
print(type(a)) # ——bytes
'''

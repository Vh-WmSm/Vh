# coding=gbk
import os

path = 'E:\\Python1\\总结\\os.listdic()和join()的用法'
list_ = os.listdir(path)
print(list_)

list_.remove('代码.py')
str_ = ''.join(list_)
print(str_)

lis = str_.split('.txt')
print(lis)

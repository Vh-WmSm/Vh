# coding=gbk
import os

path = 'E:\\Python1\\�ܽ�\\os.listdic()��join()���÷�'
list_ = os.listdir(path)
print(list_)

list_.remove('����.py')
str_ = ''.join(list_)
print(str_)

lis = str_.split('.txt')
print(lis)

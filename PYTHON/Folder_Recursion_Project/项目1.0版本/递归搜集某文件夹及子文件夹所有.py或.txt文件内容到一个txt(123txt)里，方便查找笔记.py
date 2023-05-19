import os
import sys
import chardet

origin_address = input('地址（一定是直接复制下来的，不能自己手打）：')
address_list = [origin_address]

def fun(next_address):
    global origin_address
    os.chdir(next_address)
    lis = os.listdir()
    for li in lis:
        if os.path.isdir(li):
            next_address = os.getcwd() + '\\{}'.format(li)
            address_list.append(next_address)
            fun(next_address)
        else:
            pass
    os.chdir(origin_address)


def encoding_type_detective(file_name):
    f = open(file_name, 'rb')  # 由于chardet.detect只接收bytes型，所以用rb
    content = f.read()
    data_dict = chardet.detect(content)
    return data_dict['encoding']


def write(origin_address, address, file_type):
    os.chdir(address)
    lis = os.listdir()
    for li in lis:
        if os.path.isfile(li):
            if file_type in li:
                with open(li, 'r', encoding='utf-8', errors='ignore') as f_r:
                    with open('{}\\123.txt'.format(origin_address), 'a', encoding='utf-8') as f_w:
                        f_w.write(li + '\n\n\n' + f_r.read() + '\n\n\n')


fun(origin_address)

file_type = input('1.py 2.txt:')
if file_type == '1':
    file_type = '.py'
elif file_type == '2':
    file_type = '.txt'
else:
    print('输入有误，退出程序！')
    sys.exit()

print('递归搜索到以下文件夹，现将其中的{}文件内容写入123.txt并存放于路径{}中\n\n{}'.format(file_type, origin_address, address_list))

os.chdir(origin_address)
lis = os.listdir()
if '123.txt' in lis:
    os.remove('123.txt')

for address in address_list:
    write(origin_address, address, file_type)

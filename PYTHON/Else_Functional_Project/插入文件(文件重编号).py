# 此文件用法：
# 例如：某文件夹有文件1.txt、2.txt、3.txt、4.txt
# 我想在2和3中间插入文件，则3.txt、4.txt要分别重命名为4.txt、5.txt
# 如果文件多，人工重命名处理比较麻烦，可用此py处理
import os

address = input('位置：')
os.chdir(address)
lis = os.listdir()
insert_file = input('插入文件名（要加后缀）：')
if insert_file[0].isdigit():
    insert_file_0 = insert_file[2:]
else:
    insert_file_0 = insert_file
num_ins_file = int(input('插入位置：'))
os.rename(insert_file, '{}.{}'.format(num_ins_file, insert_file_0))
# 接下来遍历文件夹内所有文件：
try:
    for li in lis:
        if str(num_ins_file) in li:
            os.rename(li, '{}.{}'.format(num_ins_file + 1, li[2:]))
            num_ins_file += 1
except:
    print('完成！')

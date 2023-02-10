import os
import sys

file_list = []
order_list = []
origin_address = input('地址（一定是直接复制下来的，不能自己手打）：')
os.chdir(origin_address)
last_address = origin_address

def fun(last_address):
    lis = os.listdir()
    if lis == []:
        return
    for li in lis:
        if os.path.isdir(li):
            last_address = os.getcwd()
            os.chdir(li)
            fun(os.getcwd())
        elif os.path.isfile(li):
            file_list.append(li)
            now_address = os.getcwd()
            order_list.append('chdir {} && move "{}" "{}"'.format(now_address, li, origin_address))
        os.chdir(last_address)

        
fun(last_address)
print('递归搜索到以下文件：\n{}'.format(file_list), end='\n\n')
judge = input('是否转移到当前目录？y/n（直接回车默认为yes）：')
if judge == 'y' or 'Y' or '':
    os.system('&&'.join(order_list))
else:
    print('退出程序……')
    sys.exit()
# judge = input('所有文件已经转移到当前目录，是否删除空文件夹？（y/n）(直接回车默认yes)：')
# if judge == 'y' or 'Y' or '':
#     lis = os.listdir()
#     for li in lis:
#         if os.path.isdir(li):
#             print('rmdir {}'.format(li))
# else:
#     print('退出程序……')
#     sys.exit()

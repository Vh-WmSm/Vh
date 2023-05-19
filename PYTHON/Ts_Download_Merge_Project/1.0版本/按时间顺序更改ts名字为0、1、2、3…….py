import os


def get_file_list(file_path):
    dir_list = os.listdir(file_path)
    if not dir_list:
        return
    else:
        '''注意，这⾥使⽤
        表达式，将⽂件按照最后修改时间顺序升序排列
        lambda
        函数是获取⽂件最后修改时间
         os.path.getmtime() 
        函数是获取⽂件最后创建时间
        os.path.getctime()'''
        dir_list = sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x)))
    return dir_list


address = input('ts文件位置：')
os.chdir(address)
list = get_file_list(address)
for i in range(len(list)):
    os.rename('{}'.format(list[i]), '{}'.format(str(i) + '.ts'))

'''
Author: Vh-WmSm    time: 2023.2.12    version: 2.0

更新内容：
①2.0版本集成了1.0所有功能，且优化了递归代码的编写，使代码简洁易懂的同时也消除了上一版本在递归中的某些未知bug
②新增了chardet库的使用，自动化识别文件编码格式并对应编码格式读取，消除了乱码情况
③新增了shutil库的使用，可以删除非空文件夹

此文件功能介绍：
①递归扫描某目录内部所有文件并转移到此目录
②递归搜集某文件夹及子文件夹所有文件或某后缀文件内容到All_content.txt里（方便ctrl + f查找笔记）

更多功能敬请期待……

'''


import os
import sys
import shutil
import chardet


def fun(father_path, son_path):
    # global target_list, file_list  # 由于列表是可变类型，所以不需要global

    os.chdir(son_path)
    subfolder_list = os.listdir()
    for s_li in subfolder_list:  # 扫描子文件夹列表
        if os.path.isdir(s_li):  # 若扫描到的是文件夹，此时father_path就变为现在的文件夹了，所以第一个参数传入son_path，son_path就是s_li了
            fun(son_path, f'{son_path}\\{s_li}')
        else:  # 若扫描到的是文件，则将该文件绝对地址加入到target_list中
            target_list.append(f'{son_path}\\{s_li}')
            file_list.append(s_li)
    os.chdir(father_path)  # 子文件夹扫描完后返回father_path


def check_file_code(target_file):
    f = open(target_file, 'rb')  # 由于chardet.detect只接收bytes型，所以用rb
    content = f.read()
    data_dict = chardet.detect(content)
    return data_dict['encoding']


if __name__ == '__main__':
    origin_path = input('原始目录：')
    os.chdir(origin_path)
    origin_list = os.listdir()
    target_list = []  # 用来存文件的绝对地址
    file_list = []  # 单纯存文件的文件名
    for li in origin_list:
        if os.path.isdir(li):  # 若扫描到的是文件夹，调用fun函数
            fun(origin_path, f'{origin_path}\\{li}')

    print('递归扫描到以下文件：')
    print(file_list)
    judge = input('现在，你想做什么？\n①把后缀为xxx的文件(非文件夹)全部移到origin_path。\n②把后缀为xxx的文件内容写入All_Content.txt中\n请选择（1 or 2）：')
    suffix = input('文件后缀(e.g: txt)（直接回车默认全部文件）：')
    if judge == '1':
        jud = input(f'即将把此目录及其所有子目录下的所有{suffix}文件全部移动到此目录，请了解清楚后谨慎操作，操作不可逆！！！\n确认请输入yes：')
    if judge == '1' and jud == 'yes':
        for target_file in target_list:
            if suffix == target_file[target_file.rfind('.') + 1:] or suffix == '':
                file_name = target_file[target_file.rfind('\\') + 1:]
                os.rename(target_file, origin_path + '\\' + file_name)  # rename函数可以更改文件绝对地址，也即移动了文件
            else:
                print('请检查输入的文件后缀是否正确，正在退出程序……')  # 若后缀输入错误，直接退出程序，不做多余的判断判断判断。。。杜绝遍历完了啥也没做才退出程序情况的发生
                sys.exit()
        jud_rm_empty_dir = input("操作完成，是否删除当前目录的空文件夹？（直接回车默认“确认删除”）")
        if jud_rm_empty_dir == '':
            for li in origin_list:
                if os.path.isdir(li):
                    shutil.rmtree(li)  # 笔记：os.rmdir()只能删除非空文件夹（若内部包含空文件夹也不叫非空），shutil.rmtree()可以删除非空文件夹
    elif judge == '2':
        os.chdir(origin_path)
        if 'All_Content.txt' in os.listdir():
            os.remove('All_content.txt')  # 若之前已存在All_content.txt，则先删除，因为f_w是“a”
        f_w = open(origin_path + '\\All_Content.txt', 'a', encoding='utf-8')
        for target_file in target_list:
            if suffix == target_file[target_file.rfind('.') + 1:] or suffix == '':
                encoding = check_file_code(target_file)  # 用chardet.detect查询该文件内容的编码，并匹配之再读取，这样写入才不会乱码
                with open(target_file, 'r', encoding=encoding) as f_r:
                    file_name = target_file[target_file.rfind('\\') + 1:]
                    f_w.write(file_name + '\n' + f_r.read() + '\n\n')  # 每个文件之间用文件名区分，并加以若干换行符
            else:
                print('请检查输入的文件后缀是否正确，正在退出程序……')
                sys.exit()
        f_w.close()

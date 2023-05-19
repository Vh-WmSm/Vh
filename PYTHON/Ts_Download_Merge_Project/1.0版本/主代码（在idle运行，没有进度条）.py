# coding=gbk
import requests
import time
import os


def menu():
    print('*'*10 + '欢迎来到ts文件批量下载并连接程序' + '*'*10, end='\n\n')
    print('温馨提示：运行代码前请确保桌面有两个东西：in.txt、in。\n\n\t其中in.txt放ts所有下载网址，in为空文件夹')
    print("\n\t而且，in.txt中，一行为一个下载网址，最后一个网址之后不要留'\\n'")
    judge = input('\n\t确认无误输入y/Y运行：')
    if judge == 'y' or judge == 'Y':
        return
    else:
        print('\n\t输入非y/Y，退出程序！')
        exit()
    
# 此函数曾在我调试bug时错删了我的ts文件，所以不如废置它了
# 废置理由：
# ①保证in一开始是空文件夹即可，没必要一开始便清空in文件夹，万一删错了呢
# ②为防止用其中一种方法连接出现错误，故结束后先不删除in文件夹内的所有ts文件
def del_file():
    os.chdir('C:\\users\\vh-暖夏\\desktop\\in')
    os.system('@echo y|del *.*')


def ord_9632(i, length):  # ord(9632) == '■'，故以此作为函数命名
    num = round((i / length) * 100)
    return '■' * num


def percent(i, length):
    percent_ = format(round(i / length, 3) * 100, '.1f')
    return str(percent_) + '%'


def ts_download():
    with open('C:\\users\\vh-暖夏\\desktop\\in.txt', 'r') as l:
        url_list = l.read().split('\n')  # 读取ts文件下载地址
    length = len(url_list)
    j = 0
    for i in range(length):
        url = url_list[i]
        res = requests.get(url)
        with open('C:\\users\\vh-暖夏\\desktop\\in\\{}.ts'.format(i), 'wb') as f:
            f.write(res.content)
        if j - i == 0 or i == length - 1:
            j += 1  # 每下载1个文件，打印一次进度
            print('\n\t下载进度：{}'.format(percent(i + 1, length)))
    print('\n\tts文件爬取完毕!')
    return length


class concat:
# 注：此处self会自动将__init__代码放到主函数的位置，故不用传name和contact_method参数
    def __init__(self): 
        # 由于可能其中一种方法连接出来的视频有问题，所以供两种方法可选择：
        if contact_method == '1':
            print('\n\t正在使用第copy方法连接ts文件：')
            self.ts_concat_copy(length, name)
        elif contact_method == '2':
            print('\n\t正在使用ffmpeg方法连接ts文件：')
            self.ts_concat_ffmpeg(length, name)
        # 若选择的方法有问题，可以运行同文件夹下的“两种方法连接ts”选择另一种方法再次连接


    # ffmpeg -i "concat:01.mp4|02.mp4|03.mp4" -c copy out.mp4
    def ts_concat_ffmpeg(self, length, name):
        time.sleep(1)
        s = ''
        for i in range(length - 1):
            s += '{}.ts|'.format(i)
        s += '{}.ts'.format(length - 1)
        order = 'ffmpeg -i "concat:{}" -c copy {}.mp4'.format(s, name)
        os.chdir('C:\\users\\vh-暖夏\\desktop\\in')
        os.system(order)
        
    # 运用cmd命令连接：copy /b *.ts name.mp4
    def ts_concat_copy(self, length, name):
        time.sleep(1)
        str_ = ''
        for i in range(length):
            str_ += "{}.ts+".format(i)
        # 去除最后一个加号
        str1 = str_[:len(str_) - 1]  # 生成str1 = '0.ts+1.ts+...+n.ts'
        order = 'copy /b {} {}.mp4'.format(str1, name)
        os.chdir('C:\\users\\vh-暖夏\\desktop\\in')
        os.system(order)
        
class move:
    def __init__(self):
        self.move(move_adress, name)
        
    def move(self, move_adress, name):
        os.chdir('C:\\users\\vh-暖夏\\desktop\\in')
        order = 'move {}.mp4 {}'.format(name, move_adress)
        os.system(order)
        if move_adress == 'C:\\users\\vh-暖夏\\desktop':
            print('\n\t合成文件已移动到桌面！')
        else:
            print('\n\t合成文件已移动到指定位置')


if __name__ == '__main__':
    menu()
    name = input('\n\t请输入输出文件名（不用写后缀）：')
    contact_method = input('\n\t等下采用哪种方法连接？1.copy。2.ffmpeg。其他：不连接\n\t请选择：')
    key = 0
    if contact_method == '1' or contact_method == '2':
        key = 1
    if key == 1:
        judge = input('\n\t连接完成后把文件移动到什么位置？1.指定位置。其他：desktop：')
        if judge == '1':
            move_adress = input('\n\t请输入目标位置：')
        else:
            move_adress = 'C:\\users\\vh-暖夏\\desktop'
    length = ts_download()
    if key == 1:
        # 定义concat_变量属于类concat并自动运行__init__()
        concat_ = concat()
        # 定义move_变量属于move并自动运行__init__()
        move_ = move()
    print('\n\t全部完成！')

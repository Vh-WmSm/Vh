import os
import time
import requests


# 主菜单
def menu():
    print('*' * 10 + '【欢迎来到学习通任务点中ppt图片爬取程序 4.0版本(2022.6.3)】' + '*' * 10)
    print('【程序使用方法】')
    print('①先确定你的桌面地址，如：C:\\Users\\Vh\\Desktop')
    print('②确保你的桌面中有一个按要求做好的url.txt文本文档')
    print('Tips:桌面地址确定方法和文本文档创建方法在代码的注释中', end='\n\n')
    '''注：
        ①桌面地址确定方法：确保未选中桌面任何文件的情况下，在桌面空白处按住shift再点击鼠标右键，弹出菜单中点击
        "打开PowerShell"，然后复制桌面地址(复制“C——p”，“>”号和前面的空格不要复制)即可（win11需先按“显示更多选项”）
        ②url.txt创建方法，在桌面右键新建一个文本文档，重命名为url（后缀不用变），然后在网页上打开学习通任务点相应PPT，
            在最后一张图片上，右键鼠标，点击复制图像链接，然后粘贴到url.txt文件里，回车，后续可依次粘贴需要的PPT地址'''

    '''更新历史：1.0版本：可单个下载ppt，需手动更改循环次数和图片地址
                 2.0版本：增加了批量下载功能
                 3.0版本：增加了自动创建文件夹功能、增加了验证码功能、增加了turtle库的应用
                 4.0版本：修复了需手动输入url.txt中url个数的弊端，程序可自动读取'''
    judge = input('看明白并做好准备工作后，输入y/Y开始吧！\n\n' + '请输入：')
    if judge == 'y' or judge == 'Y':
        return
    else:
        print('\n' + '那等你准备好后再来运行我吧！')
        exit()


# 定义获取基础信息的函数(列表按顺序存储：桌面地址、循环次数(url个数)、url列表)
def get_info():
    info_lis = []
    address = input('\n' + '请输入你的桌面地址：')
    info_lis.append(address)
    with open(address + '\\url.txt', 'r') as f:
        urls = f.read().strip('\n').split('\n')  # strip是去除url字符串最后的一些可能存在的空行，split是以换行符的形式分割存放url到列表中
    number = len(urls)
    info_lis.append(number)
    info_lis.append(urls)
    return info_lis


# 定义新建文件夹的函数
def create_folder(number):
    folder_name = [str(i) for i in range(1, number + 1)]  # 利用“列表解析”生成文件夹编号列表  知识点书本 P98
    for name in folder_name:
        try:
            os.makedirs(name)  # 尝试批量生成文件夹，若桌面已经存在该名字的文件夹，则避开报错，继续往下运行
        except:
            continue


# 定义清空该文件夹原先文件的函数
def del_file(i, address):
    local = '{}\\{}'.format(address, i)
    os.chdir(local)
    os.system('@echo y|del *.*')  # @echo y意思是自动输入y，表示“确定删除”


def download_picture(urls, address, number):
    for i in range(1, number + 1):
        del_file(i, address)  # 先删除当下文件夹内所有内容再下载新的（因为有可能该文件夹存在上一次爬取的内容）
        url = urls[i - 1]  # 获取当前循环的url
        start = int(url.rfind('/')) + 1  # 获取页数的最高位下标
        end = int(url.rfind('.'))  # 获取页数的最低位的下一位的下标
        nums = int(url[start:end])  # 获取总页数
        url = url[:start] + '{}' + url[end:]  # 把xxxxx/nums.png换成xxxxx/{}.png
        for num in range(1, nums + 1):
            res = requests.get(url.format(num))  # 利用requests库的get方法获取下载地址响应
            with open("{}\\{}\\{}.png".format(address, i, num), 'wb') as picture:
                picture.write(res.content)  # 从响应中获取图片内容，并写入相应的.png文件中
        print("完成第{}个ppt的爬取！".format(i))


def end(t0, t1):
    print('\n本次爬取所耗时间：{}s\n欢迎下次使用本程序，再见！'.format(round(t1 - t0, 3)), end='')  # round(, 3)四舍五入，保留3位小数
    input('\n\n键入任意继续……')




if __name__ == '__main__':
    menu()  # 显示菜单
    info_lis = get_info()  # 获取基础信息
    address = info_lis[0]  # 得到python工作区位置：即url.txt所在位置
    os.chdir(address)  # 设定python工作区为桌面，而不是此py文件所在位置
    number = info_lis[1]  # 得到循环次数
    create_folder(number)  # 自动在桌面创建文件夹并命名为1、2、3……
    urls = info_lis[2]  # 获取url列表
    t0 = time.time()  # “摁下秒表”，统计爬取所需总时间
    download_picture(urls, address, number)  # 开始爬取（urls列表下标是从0开始，而i从1开始，所以要减1）
    t1 = time.time()
    end(t0, t1)  # 打印所耗时间，结束语

from pyautogui import *
from time import sleep
import subprocess
import pytesseract
from PIL import Image
import os


def screenshot(address_0, for_num, x, y, x1, y1):
    keyDown('alt')  # 快捷键调出截图工具
    keyDown('shift')
    press('a')
    keyUp('alt')
    keyUp('shift')
    moveTo(x, y)  # 移到相应位置截图
    dragTo(x1, y1)
    keyDown('ctrl')  # 保存
    press('s')
    keyUp('ctrl')
    press('enter')
    sleep(0.5)  # 等待保存完毕

    os.chdir(address_0)
    # 重命名截图(之所以可以用*.png，是因为桌面上只有它一张png图片)
    order = 'rename *.png {}.png'.format(for_num)
    os.system(order)
    if for_num < 10:  # 若为时间截图，放到time文件夹里
        order = 'move {}.png {}\\time'.format(for_num, address_0)
    else:  # 若为视频名截图，放到file_name文件夹里
        order = 'move {}.png {}\\file_name'.format(for_num, address_0)
    os.system(order)


# 图片获取文字
def orc(img_address, for_num):
    img = Image.open(img_address)  # 打开图片
    if for_num < 10:
        text = pytesseract.image_to_string(img)  # 识别时间截图字符串
        fen, miao = text.split('/')[1].split(':')  # 从time_text中获取分、秒
        text = int(fen) * 60 + int(miao)
    else:
        text = pytesseract.image_to_string(img, lang='chi_sim')  # 识别视频名截图的文字
        text = text.split('\n')  # 下面一行的去除xx月xx日开课
        text = ''.join(text[0].split())  # 去除字与字间的空格
    return text


# 文件夹初始化——以folder_name为名创建文件夹，该路径已存在该文件夹则跳过，若time、file_name文件夹已存在，清空它们
def init_dir(address_0, folder_name):
    os.chdir(address_0)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    if folder_name == 'time' or folder_name == 'file_name':
        os.chdir(address_0 + '\\' + folder_name)
        order = '@echo y|del *.*'
        os.system(order)


def start(address_0, for_num):
    #  第一次循环进行各文件夹的初始化
    if for_num == 1:
        init_dir(address_0, 'rec')
        init_dir(address_0, 'time')
        init_dir(address_0, 'file_name')
    for_num_time = for_num
    for_num_name = for_num + 10  # for_num+10，是为了区分time的截图
    # 获取视频名(课程标题)
    screenshot(address_0, for_num_name, 93, 331, 1030, 483)  # 获取视频名截图并保存在file_name文件夹内
    img_name_address = address_0 + '\\file_name\\{}.png'.format(for_num_name)  # 视频名截图的所在地址
    file_name = orc(img_name_address, for_num_name)

    click(200, 590)  # 进入课堂
    sleep(5)  # 等待进入课堂

    screenshot(address_0, for_num_time, 168, 1022, 378, 1067)  # 获取视频总时间截图并保存在time文件夹内
    img_time_address = address_0 + '\\time\\{}.png'.format(for_num)  # 时间截图的所在地址
    time = orc(img_time_address, for_num)
    return [file_name, time]


def rec(file_name):
    os.chdir(address_0 + '\\rec')
    # 运用subprocess.Popen而不用os.system是因为后者cmd必须终止了程序才能继续运行，这样我们无法读秒
    subprocess.Popen(
        'ffmpeg -f dshow -rtbufsize 1000M -i audio="virtual-audio-capturer"'
        ' -f gdigrab -i desktop -r 20 -b:v 150k -b:a 225k -ar 48000 -crf 30 {}.mp4'.format(file_name))
    # 检索是否有“夜深了”弹窗
    location = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\night.png')
    if location != None:
        click(996, 694)  # 弹窗夜深了，点击取消开启护眼模式
    moveTo(2000, 300)  # 把鼠标移到最右边防止影响视野


def end(time):
    sleep(time)
    keyDown('alt')
    press('tab')
    keyUp('alt')
    sleep(0.5)
    press('shift')
    sleep(0.5)
    press('q')
    sleep(0.5)
    click(50, 30)  # 按“离开教室”
    for i in range(5):
        click(1910, 1100)  # 点击右下角的下滑箭头五次，定位到下一课


if __name__ == '__main__':
    sleep(3)  # 按”运行“后， 3秒时间切换到高途，然后程序开始
    address_0 = 'C:\\Users\\vh\\Desktop'
    for for_num in range(1, 6):
        file_name, time = start(address_0, for_num)
        rec(file_name)
        end(time)

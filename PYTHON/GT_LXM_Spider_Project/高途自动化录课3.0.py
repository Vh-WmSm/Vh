# 注意使用前需先随便用alt+shift+a截一个图然后保存到桌面，使得默认保存位置为桌面
from pyautogui import *
from time import sleep
import subprocess
import pytesseract
from PIL import Image
import os


def screenshot(address_0, img_name, x, y, x1, y1):
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
    order = 'rename *.png {}.png'.format(img_name)
    os.system(order)
    if img_name < 20:  # 若为时间截图，放到time文件夹里
        order = 'move {}.png {}\\time'.format(img_name, address_0)
    else:  # 若为视频名截图，放到mp4_name文件夹里
        order = 'move {}.png {}\\mp4_name'.format(img_name, address_0)
    os.system(order)


# 图片获取文字
def orc(img_address, img_name):
    img = Image.open(img_address)  # 打开图片
    if img_name < 20:
        text = pytesseract.image_to_string(img)  # 识别时间截图字符串
        fen, miao = text.split('/')[1].split(':')  # 从time_text中获取分、秒
        text = int(fen) * 60 + int(miao)
    else:
        text = pytesseract.image_to_string(img, lang='chi_sim')  # 识别视频名截图的文字
        text = ''.join(text.split())  # 去除字与字间的空格
    return text


# 文件夹初始化——以folder_name为名创建文件夹，该路径已存在该文件夹则跳过，若time、mp4_name文件夹已存在，清空它们
def init_dir(address_0, folder_name):
    os.chdir(address_0)
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    if folder_name == 'time' or folder_name == 'mp4_name':
        os.chdir(address_0 + '\\' + folder_name)
        order = '@echo y|del *.*'
        os.system(order)


def start(address_0, for_num, x, y):
    #  第一次循环进行各文件夹的初始化并获取y值
    if for_num == 1:
        init_dir(address_0, 'rec')
        init_dir(address_0, 'time')
        init_dir(address_0, 'mp4_name')
        now_khf_img_address = address_0 + '\\desktop\\khf.png'  # 第一课的”看回放“截图地址
        now_khf_img_location = locateOnScreen(now_khf_img_address, confidence=0.97)
        y = now_khf_img_location[1] - 170
    time_img_name = for_num
    mp4_name_img_name = for_num + 20  # for_num+20，是为了区分time的截图
    # 获取视频名(课程标题)
    screenshot(address_0, mp4_name_img_name, x, y, x + 741, y + 52)  # 获取视频名截图并保存在mp4_name文件夹内
    mp4_name_img_address = address_0 + '\\mp4_name\\{}.png'.format(mp4_name_img_name)  # 视频名截图的所在地址
    mp4_name = orc(mp4_name_img_address, mp4_name_img_name)  # orc函数从mp4_name_img_name截图中识别mp4_name

    click(x + 95, y + 176)  # 进入课堂
    sleep(8)  # 等待进入课堂

    # 检索是否有“夜深了”弹窗
    for i in range(2):
        location = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\night.png', confidence=0.97)
        if location != None:
            click(996, 694)  # 弹窗夜深了，点击取消开启护眼模式

    screenshot(address_0, time_img_name, 168, 1022, 378, 1067)  # 获取视频总时间截图并保存在time文件夹内
    time_img_address = address_0 + '\\time\\{}.png'.format(time_img_name)  # 时间截图的所在地址
    time = orc(time_img_address, time_img_name)
    return [mp4_name, time]


def rec(mp4_name):
    os.chdir(address_0 + '\\rec')
    # 运用subprocess.Popen而不用os.system是因为后者cmd必须终止了程序才能继续运行，这样我们无法读秒
    subprocess.Popen(
        'ffmpeg -f dshow -rtbufsize 1000M -i audio="virtual-audio-capturer"'
        ' -f gdigrab -i desktop -r 20 -b:v 150k -b:a 225k -ar 48000 -crf 30 {}.mp4'.format(mp4_name))
    sleep(0.5)
    keyDown('alt')  # 隐藏录屏窗口
    press('tab')
    keyUp('alt')
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
    sleep(1)
    click(50, 30)  # 按“离开教室”
    moveTo(500, 0)  # 移开鼠标，防止一直触发左上角的流量监控
    sleep(6)  # 等待离开教室完成


def find_next_lesson(address_0, for_num, now_class, last_class):
    last_mp4_name_img_name = for_num + 20  # 上一课视频名截图文件名
    last_mp4_name_img_address = address_0 + '\\mp4_name\\{}.png'.format(last_mp4_name_img_name)  # 上一课视频名截图地址
    new_khf_img_address = address_0 + '\\desktop\\khf.png'  # 新一课的”看回放“截图地址
    now_class_img_address = address_0 + '\\desktop\\{}.png'.format(now_class)  # “当前栏目”图片地址
    last_class_img_address = address_0 + '\\desktop\\{}.png'.format(last_class)  # “上一栏目”图片地址
    while True:
        last_mp4_name_img_location = locateOnScreen(last_mp4_name_img_address, confidence=0.97)  # 上一课视频名截图的定位
        if not last_mp4_name_img_location:  # 上一课的视频名截图没找到，考虑是高途刷新了，点击上箭头十次，开始往上找
            for i in range(10):
                press('up')
        else:  # 上一课的视频名截图找到了
            # 调用“找下一课”助手函数，减少代码臃肿
            return find_next_lesson_assistant(last_mp4_name_img_location, last_mp4_name_img_address, new_khf_img_address)
        # 若已经检索到“当前栏目”图片，而还未被上一部分return，说明上一课在“上一栏目”中
        now_class_location = locateOnScreen(now_class_img_address, confidence=0.97)
        if now_class_location:
            sleep(0.5)  # 让系统反应过来
            click(center(now_class_location))  # 点击“当前栏目”中心点，关闭这一栏
            while True:
                press('up')  # 继续往上查找“上一栏目”图片
                last_class_location = locateOnScreen(last_class_img_address, confidence=0.97)
                if last_class_location:
                    sleep(0.5)  # 让系统反应过来
                    click(center(last_class_location))  # 点击“上一栏目”中心点，打开这一栏
                    break
            while True:
                last_mp4_name_img_location = locateOnScreen(last_mp4_name_img_address, confidence=0.97)  # 上一课视频名截图的定位
                if not last_mp4_name_img_location:
                    for i in range(10):
                        press('down')  # 继续往下查找
                else:  # 若找到上一课视频名截图的定位
                    return find_next_lesson_assistant(last_mp4_name_img_location, last_mp4_name_img_address, new_khf_img_address)


def find_next_lesson_assistant(last_mp4_name_img_location, last_mp4_name_img_address, new_khf_img_address):
    while last_mp4_name_img_location[1] > 373:  # 若距离上边沿大于373，下滑一格
        press('down')
        last_mp4_name_img_location = locateOnScreen(last_mp4_name_img_address, confidence=0.97)  # 更新上一课视频名截图的定位
        '''确实是找到了上一课，也确实找到时y轴坐标大于373，所以下滑了一格，但是可能此时刚好是差不多到373临界位置，所以上一课
        的视频名截图刚好上了去被遮住了，此时若无if跳出循环，则会导致while判断出错，因为location是None，而不能location[1]'''
        if last_mp4_name_img_location == None:
            press('up')  # 往上回一格
            break
    for i in range(4):
        press('down')  # 再往下4格，让上一课的”看回放“消失，使得获得的是下一课的”看回放“坐标
    sleep(1)  # 等待1秒，让电脑反应过来再下一步
    new_khf_img_location = locateOnScreen(new_khf_img_address, confidence=0.97)
    y = new_khf_img_location[1] - 170
    return y


#  异常情况重命名视频——orc无法识别文字，返回了None，则视频名为.mp4只有后缀，若等下还有无法识别的，则还是.mp4，名字重复，录屏不会继续
def out_abnormal_mp4(address_0, for_num):
    os.chdir(address_0 + '\\rec')
    lis = os.listdir()
    if '.mp4' in lis:
        order = 'rename .mp4 {}.mp4'.format(address_0, for_num)  # 以当前循环次数进行命名，永远不会重复
        os.system(order)


# 录了10个视频电脑睡眠
def shut_down_or_sleep(judge):
    keyDown('win')  # 返回桌面
    press('d')
    keyUp('win')
    sleep(1)
    click(955, 500)  # 点两次桌面，确认未选中桌面任何东西
    sleep(0.5)
    click(955, 500)
    sleep(0.5)
    keyDown('alt')  # alt+f4
    press('f4')
    keyUp('alt')
    if judge == '2':
        press('up')  # 按上键选择为“睡眠”
    press('enter')  # judge=='1'或其他，直接关机了


if __name__ == '__main__':
    how_many = int(input('要录几个视频？：'))
    judge = input('录完后关机：1，还是睡眠：2：')
    sleep(3)  # 按”运行“后， 3秒时间切换到高途并把将录的课放到第一位(如何看是否第一位？，在当前屏幕中，这一课的”看回放“在第一位置)，然后程序开始
    address_0 = 'C:\\Users\\vh\\Desktop'
    x, y = [93, 0]
    for_num = 1
    while for_num <= how_many:  # 设定录x个视频就睡眠
        out_abnormal_mp4(address_0, for_num)
        mp4_name, time = start(address_0, for_num, x, y)
        rec(mp4_name)
        end(time)
        sx_img_address = address_0 + '\\desktop\\sx.png'  # ”数学科“图片地址
        yy_img_address = address_0 + '\\desktop\\yy.png'  # ”英语科“图片地址
        if locateOnScreen(sx_img_address, confidence=0.97):
            y = find_next_lesson(address_0, for_num, 'glqh', 'gsqh')
        elif locateOnScreen(yy_img_address, confidence=0.97):
            y = find_next_lesson(address_0, for_num, 'sqjd', 'jcjd')
        for_num += 1
    shut_down_or_sleep(judge)

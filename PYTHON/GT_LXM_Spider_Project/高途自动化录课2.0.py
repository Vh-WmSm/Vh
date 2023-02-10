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
        now_khf_img_location = locateOnScreen(now_khf_img_address, confidence=0.95)
        y = now_khf_img_location[1] - 170
    time_img_name = for_num
    mp4_name_img_name = for_num + 20  # for_num+20，是为了区分time的截图
    # 获取视频名(课程标题)
    screenshot(address_0, mp4_name_img_name, x, y, x + 741, y + 52)  # 获取视频名截图并保存在mp4_name文件夹内
    mp4_name_img_address = address_0 + '\\mp4_name\\{}.png'.format(mp4_name_img_name)  # 视频名截图的所在地址
    mp4_name = orc(mp4_name_img_address, mp4_name_img_name)  # orc函数从mp4_name_img_name截图中识别mp4_name

    click(x + 95, y + 176)  # 进入课堂
    sleep(5)  # 等待进入课堂

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
    sleep(2)
    keyDown('alt')  # 隐藏录屏窗口
    press('tab')
    keyUp('alt')
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
    sleep(2)
    click(50, 30)  # 按“离开教室”
    moveTo(500, 0)  # 移开鼠标，防止一直触发左上角的流量监控
    sleep(5)  # 等待离开教室完成


def find_next_lesson(address_0, for_num):
    last_mp4_name_img_name = for_num + 20  # 上一课视频名截图文件名
    last_mp4_name_img_address = address_0 + '\\mp4_name\\{}.png'.format(last_mp4_name_img_name)  # 上一课视频名截图地址
    last_mp4_name_img_location = locateOnScreen(last_mp4_name_img_address, confidence=0.95)  # 上一课视频名截图的定位
    new_khf_img_address = address_0 + '\\desktop\\khf.png'  # 新一课的”看回放“截图地址
    # 若last_mp4_name_img_location非空，说明离开教室后检测到上一课视频名截图仍在屏幕上，说明高途没有刷新网页，滑到下一课即可
    if last_mp4_name_img_location:
        while last_mp4_name_img_location[1] > 373:  # 若距离上边沿大于373，需下滑才能找到下一课的定位了
            click(1907, 1070)
            last_mp4_name_img_location = locateOnScreen(last_mp4_name_img_address, confidence=0.95)  # 更新上一课视频名截图的定位
        for i in range(4):
            click(1907, 1070)  # 再往下4格，让上一课的”看回放“消失，使得获得的是下一课的”看回放“坐标
        sleep(1)  # 等待1秒，让电脑反应过来再下一步
        new_khf_img_location = locateOnScreen(new_khf_img_address, confidence=0.95)
        y = new_khf_img_location[1] - 170
    # last_mp4_name_img_location是空的，说明高途刷新了页面
    else:
        sx_img_address = address_0 + '\\desktop\\sx.png'  # ”数学科“图片地址
        # yy_img_address = address_0 + '\\desktop\\yy.png'  # ”英语科“图片地址
        # 若此时是数学科
        if locateOnScreen(sx_img_address, confidence=0.95):
            xdqh_img_address = address_0 + '\\desktop\\xdqh.png'  # “线性强化”图片地址
            gsqh_img_address = address_0 + '\\desktop\\gsqh.png'  # ”高数强化“图片地址
            while True:
                for i in range(5):
                    click(1913, 48)  # 点5次右上角箭头，然后查找一次”线代强化“图片
                location = locateOnScreen(xdqh_img_address, confidence=0.95)
                if location:  # location为真值(不为None)则进入if
                    sleep(0.5)  # 让系统反应过来
                    click(center(location))  # 点击“线性强化”中心点，关闭这一栏
                    while True:
                        click(1913, 48)  # 继续往上查找”高数强化“图片
                        location = locateOnScreen(gsqh_img_address, confidence=0.95)
                        if location:
                            sleep(0.5)  # 让系统反应过来
                            click(center(location))  # 点击“高数强化”中心点，打开这一栏
                            break
                    break
        # else:  # 英语科的情况
        while True:
            click(1907, 1070)  # 往下查找
            last_mp4_name_img_location = locateOnScreen(last_mp4_name_img_address, confidence=0.95)  # 上一课视频名截图的定位
            if last_mp4_name_img_location:  # 若找到上一课视频名截图的定位
                for i in range(15):  # 往下走15格，方便对下一课进行操作
                    click(1907, 1070)
                sleep(1)  # 稍等一会，让系统反应过来
                new_khf_img_location = locateOnScreen(new_khf_img_address, confidence=0.95)
                y = new_khf_img_location[1] - 170
                break
    return y

def shut_down():
    keyDown('win')  # 返回桌面
    press('d')
    keyUp('win')
    sleep(1)
    click(955, 500)  # 点两次桌面，确认未选中桌面任何东西
    sleep(0.5)
    click(955, 500)
    keyDown('alt')  # alt+f4
    press('f4')
    keyUp('alt')
    press('enter')
    

if __name__ == '__main__':
    sleep(3)  # 按”运行“后， 3秒时间切换到高途并把将录的课放到第一位(如何看是否第一位？，在当前屏幕中，这一课的”看回放“在第一位置)，然后程序开始
    address_0 = 'C:\\Users\\vh\\Desktop'
    x, y = [93, 0]
    for_num = 1
    while True:
        if for_num == 11:  # 录了10个视频就关机，否则一天刷太多视频不真实
            shut_down()
            break
        mp4_name, time = start(address_0, for_num, x, y)
        rec(mp4_name)
        end(time)
        y = find_next_lesson(address_0, for_num)
        for_num += 1
        

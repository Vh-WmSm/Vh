from pyautogui import *
import time
import pytesseract
from PIL import Image


def screen_shot(x, y, x1, y1):
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


def save_img(address_0, target_add, num):
    os.chdir(address_0)
    # 重命名截图(之所以可以用*.png，是因为桌面上只有它一张png图片)
    order = 'rename *.png {}.png'.format(num)
    os.system(order)
    order = 'move {}.png {}\\{}'.format(num, address_0, target_add)
    os.system(order)


def start(address_0, num, key):
    # if num == 0:
    #     location = list(locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\xx.png', confidence=0.97))
    #     x = location[:2][0] - 1000
    #     y = location[:2][1] - 45
    #     x1 = x + 500
    #     y1 = y + 55
    #     screen_shot(x, y, x1, y1)
    #     save_img(address_0, 'time', i)
    #     location = locateOnScreen('C:\\Users\\Vh\\Desktop\\time\\{}.png'.format(i), confidence=0.97)
    #     click(center(location))
    # 
    # sleep(2)  # 等待进入这一系列课程

    location = list(locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\hd.png', confidence=0.97))
    if num == 0 and key == '':
        location = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\ml.png', confidence=0.97)
        x, y = center(location)
        x -= 180
        y += 60
    else:
        x, y = location[:2]
        x += 45
        y += 66
    x1 = x + 270
    y1 = y + 40
    screen_shot(x, y, x1, y1)
    save_img(address_0, 'mp4_name', num)

    img = Image.open('c:\\users\\vh\\desktop\\mp4_name\\{}.png'.format(num))  # 打开图片
    text = pytesseract.image_to_string(img)

    if text == '':
        screen_shot(x, y + 60, x1, y1 + 60)
        save_img(address_0, 'rec', num)
        img = Image.open('c:\\users\\vh\\desktop\\rec\\{}.png'.format(num))  # 打开图片
        text1 = pytesseract.image_to_string(img)
        if text1 == '':
            return 0  # 本系列课已经结束，返回

    moveTo(2000, 300)  # 把鼠标移走防止课程名称字体变红色
    location = locateOnScreen('C:\\Users\\Vh\\Desktop\\mp4_name\\{}.png'.format(num), confidence=0.97)
    click(center(location))
    while True:
        location_wqgk = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\wqgk.png', confidence=0.97)
        location_jxgk = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\jxgk.png', confidence=0.97)
        if location_wqgk != None or location_jxgk != None:
            break
    if location_wqgk != None:
        x, y = center(location_wqgk)
        click(x, y + 90)
    elif location_jxgk != None:
        x1, y1 = center(location_jxgk)
        click(x1, y1)
    elif location_ztj != None:
        x2, y2 = center(location_ztj)
        click(x2, y2)
    moveTo(2000, 300)
    return 1


def find_pop_up():
    while True:
        location = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\zt.png', confidence=0.97)
        time.sleep(1)
        if location != None:
            x = center(location)[0]
            y = center(location)[1] + 100
            click(x, y)
            sleep(1)
            try:
                location_ = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\ztj.png', confidence=0.97)
                click(center(location_))
            except:
                pass
            moveTo(2000, 300)  # 把鼠标移到最右边防止影响视野
        location_ = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\spbfwb.png', confidence=0.97)
        if location_:
            x = center(location_)[0]
            y = center(location_)[1] + 100
            click(x, y)
            sleep(2)
            return


def next_lesson(i):
    location = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\fhkcy.png', confidence=0.97)
    click(center(location))
    sleep(0.6)
    location = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\lwh.png', confidence=0.97)
    click(center(location))
    sleep(0.6)
    location = locateOnScreen('C:\\Users\\Vh\\Desktop\\desktop\\wdkc.png', confidence=0.97)
    click(center(location))
    sleep(0.6)
    # while True:
    #     last_lesson_location = locateOnScreen('C:\\Users\\Vh\\Desktop\\time\\{}.png'.format(i - 1), confidence=0.97)
    #     if last_lesson_location == None:
    #         for j in range(5):
    #             press('down')
    #     else:
    #         while last_lesson_location != None:
    #             press('down')
    #             last_lesson_location = locateOnScreen('C:\\Users\\Vh\\Desktop\\time\\{}.png'.format(i - 1),
    #                                                   confidence=0.97)
    #         press('down')
    #         return


if __name__ == '__main__':
    while True:
        key = input('是否从第一课开始(若否则按空格再回车，若是则直接回车)：')
        sleep(2)
        address_0 = 'c:\\users\\vh\\desktop'
        os.chdir('c:\\users\\vh\\desktop\\mp4_name')
        os.system('@echo y | del *.*')
        os.chdir('c:\\users\\vh\\desktop\\rec')
        os.system('@echo y | del *.*')
        num = -1
        while True:
            num += 1
            if start(address_0, num, key) == 0:
                next_lesson(0)
                break
            find_pop_up()

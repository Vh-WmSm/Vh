# coding=gbk
import os
import time


def menu():
    folder_name = []
    print('----------批量转换文件夹中视频音量----------')
    print('Tips：①转换较慢，15分钟的视频转换大概需30秒。②音量转换幅度太大，会导致失真。')
    desktop_file = os.listdir('C:\\users\\vh\\desktop')
    while True:
        folder_name.append(input('请输入文件夹名称（此文件夹放在桌面，且存放着要转换的视频）：'))
        folder_name.append(input('请输入输出文件夹名称：'))
        if folder_name[0] in desktop_file and folder_name[1] in desktop_file:
            return folder_name
        else:
            print('文件夹不在桌面上，请重新输入！')


def transform(lis, path_in, path_out):
    while True:
        print('按什么方式转换？1：倍数；2：分贝；3：静音输出')
        judge_volume = input('请输入1/2/3：')
        if judge_volume == '1':
            volume = input('将音量转换为原文件的多少倍：（例：3、0.3）')
            key = 1
            break
        elif judge_volume == '2':
            volume = input('将音量增加/减少多少分贝：（例：10、-10）')
            volume += 'dB'
            key = 1
            break
        elif judge_volume == '3':
            key = 0
            break
        else:
            print('输入有误，重新输入！')
    # judge_del = input('转换完成后是否删除原文件？y/n：')
    t0 = time.time()
    os.chdir(path_in)
    i = 1
    if key == 1:
        for li in lis:
            order = 'ffmpeg -i {} -filter:a "volume = {}" -vcodec copy o_{}'.format(li, volume, li)
            i += 1
            os.system(order)
            move(path_out, 'o_{}'.format(li))
    else:
        for li in lis:
            order = 'ffmpeg -i {} -an -vcodec copy o_{}'.format(li, li)
            i += 1
            os.system(order)
            move(path_out, 'o_{}'.format(li))
    # return judge_del
    return t0


# def del_original(lis):
#     print('正在删除原文件……')
#     time.sleep(1.5)
#     for li in lis:
#         os.system("@echo y|del {}".format(li))
#     print('已经删除原文件！')
#     time.sleep(0.5)

def move(path_out, name):
    os.system('move {} {}'.format(name, path_out))

if __name__ == '__main__':
    folder_name = menu()
    path_in = 'C:\\users\\vh\\desktop\\{}'.format(folder_name[0])
    path_out = 'C:\\users\\vh\\desktop\\{}'.format(folder_name[1])
    lis = os.listdir(path_in)
    t0 = transform(lis, path_in, path_out)
    # if judge_del == 'y' or judge_del == 'Y':
    # del_original(lis)
    print('全部完成！')
    time.sleep(0.5)
    t1 = time.time()
    print("此次转换所耗时间：" + str(t1 - t0))

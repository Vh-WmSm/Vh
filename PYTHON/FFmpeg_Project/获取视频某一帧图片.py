# coding=gbk
import os
import PySimpleGUI as sg
import sys
location = ''
name_in = ''
out_location = ''
while True:
    layout = [
        [sg.Text('{:<21}'.format('请输入文件所在地址:')), sg.In(location)],
        [sg.Text('{:<15}'.format('请输入文件名(要加上后缀名):')), sg.Input(name_in)],
        [sg.Text('{:<33}'.format('图片时间:')), sg.In()],
        [sg.Text('{:<17}'.format('输出文件名(不用写后缀名):')), sg.In()],
        [sg.Text('{:<32}'.format('输出位置:')),sg.In(out_location)],
        [sg.Button('开始获取')]  # 设置“开始获取”按钮
    ]
    windows = sg.Window('获取视频某一帧图片', layout, keep_on_top=True)  # 显示窗口
    while True:  # 设置窗口循环
        event, values = windows.read()  # 设置变量作为窗口显示内容
        if event == None:  # 设置关闭窗口事件
            sys.exit()
        if event == '开始获取':  # 设置点击“开始获取”按钮事件
            # 设置返回内容
            location = values[0]
            name_in = values[1]
            start = values[2].split()
            start = ':'.join(start)
            name_out = values[3]
            out_location = values[4]
            os.chdir(location)
            # 自动生成序号：
            lis = os.listdir(out_location)
            lis_t = []
            max = 0
            for i in lis:
                if '.mp4' in i or '.png' in i:
                    l = i.split('.', 1)[0]
                    if l.isdigit():
                        if int(l) > max:
                            max = int(l)
            name_i = '"' + '{}'.format(name_in) + '"'
            name_o = '"' + '{}.{}.png'.format(max + 1, name_out) + '"'
            order = 'ffmpeg -ss {} -i {} -vframes 1 {}'.format(start, name_i, name_o)
            os.system(order)
            print(order)
            file = '"' + "{}.{}.png".format(max + 1, name_out) + '"'
            out_loca = '"' + '{}'.format(out_location) + '"'
            move_order = "move {} {}".format(file, out_loca)
            print(move_order)
            os.system(move_order)
            print('完成！')
            break
    windows.close()

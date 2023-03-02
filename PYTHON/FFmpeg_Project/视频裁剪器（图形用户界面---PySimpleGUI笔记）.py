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
        [sg.Text('{:<28}'.format('裁剪开始时间:')), sg.In()],
        [sg.Text('{:<28}'.format('裁剪结束时间:')), sg.In()],
        [sg.Text('{:<17}'.format('输出文件名(不用写后缀名):')), sg.In()],
        [sg.Text('{:<32}'.format('输出位置:')), sg.In(out_location)],
        [sg.Button('开始裁剪')]  # 设置“开始裁剪”按钮
    ]
    windows = sg.Window('视频裁剪器', layout, keep_on_top=True)  # 显示窗口
    while True:  # 设置窗口循环
        event, values = windows.read()  # 设置变量作为窗口显示内容
        if event == None:  # 设置关闭窗口事件
            sys.exit()
        if event == '开始裁剪':  # 设置点击“开始裁剪”按钮事件
            # 设置返回内容
            location = values[0]
            name_in = values[1]
            start = values[2].split()
            start = ':'.join(start)
            end = values[3].split()
            end = ':'.join(end)
            name_out = values[4]
            out_location = values[5]
            suffix = name_in.rsplit('.', 1)[1]  # 获取后缀
            os.chdir(location)

            # 自动生成序号：
            if out_location != '':
                lis = os.listdir(out_location)
            else:
                lis = os.listdir(location)
            lis_t = []
            max = 0
            for i in lis:
                if '.mp4' in i or '.png' in i:
                    l = i.split('.', 1)[0]
                    if l.isdigit():
                        if int(l) > max:
                            max = int(l)
            if name_out != '':
                name_o = '"' + '{}.{}.{}'.format(max + 1, name_out, suffix) + '"'
            else:
                name_o = '"' + '{}.{}'.format(max + 1, suffix) + '"'
            name_i = '"' + '{}'.format(name_in) + '"'
            order = 'ffmpeg -ss {} -to {} -i {} -c copy {}'.format(start, end, name_i, name_o)
            os.system(order)
            print(order)
            if out_location != '':
                out_loca = '"' + '{}'.format(out_location) + '"'
                move_order = "move {} {}".format(name_o, out_loca)
                os.system(move_order)
                print(move_order)
            print('完成！')
            break
    windows.close()

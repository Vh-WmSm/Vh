# coding=gbk
import os
import PySimpleGUI as sg
import sys
location = ''
name_in = ''
out_location = ''
while True:
    layout = [
        [sg.Text('{:<21}'.format('�������ļ����ڵ�ַ:')), sg.In(location)],
        [sg.Text('{:<15}'.format('�������ļ���(Ҫ���Ϻ�׺��):')), sg.Input(name_in)],
        [sg.Text('{:<33}'.format('ͼƬʱ��:')), sg.In()],
        [sg.Text('{:<17}'.format('����ļ���(����д��׺��):')), sg.In()],
        [sg.Text('{:<32}'.format('���λ��:')),sg.In(out_location)],
        [sg.Button('��ʼ��ȡ')]  # ���á���ʼ��ȡ����ť
    ]
    windows = sg.Window('��ȡ��Ƶĳһ֡ͼƬ', layout, keep_on_top=True)  # ��ʾ����
    while True:  # ���ô���ѭ��
        event, values = windows.read()  # ���ñ�����Ϊ������ʾ����
        if event == None:  # ���ùرմ����¼�
            sys.exit()
        if event == '��ʼ��ȡ':  # ���õ������ʼ��ȡ����ť�¼�
            # ���÷�������
            location = values[0]
            name_in = values[1]
            start = values[2].split()
            start = ':'.join(start)
            name_out = values[3]
            out_location = values[4]
            os.chdir(location)
            # �Զ�������ţ�
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
            print('��ɣ�')
            break
    windows.close()

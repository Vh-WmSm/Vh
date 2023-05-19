# coding=gbk
import os

# ffmpeg -i "concat:01.mp4|02.mp4|03.mp4" -c copy out.mp4
def ts_concat_ffmpeg(length, name):
    s = ''
    for i in range(length-1):
        s += '{}.ts|'.format(i)
    s += '{}.ts'.format(length-1)
    order = 'ffmpeg -i "concat:{}" -c copy {}.mp4'.format(s, name)
    os.chdir('C:\\users\\vh-ů��\\desktop\\in')
    os.system(order)

# ����cmd���copy /b *.ts name.mp4
def ts_concat_copy(length, name):
    str_ = ''
    for i in range(length):
        str_ += "{}.jc+".format(i)
    # ȥ�����һ���Ӻ�
    str1 = str_[:len(str_) - 1]  # ����str1 = '0.ts+1.ts+...+n.ts'
    order = 'copy /b {} {}.mp4'.format(str1, name)
    os.chdir('C:\\users\\vh-ů��\\desktop\\in')
    os.system(order)

if __name__ == '__main__':
    length = int(input('������ts�ļ����һ�����(ts�ļ�Ӧ���������in�ļ���)��')) + 1
    name = input('����ļ���������д��׺����')
    judge = input('1.copy��2.ffmpeg��3.�������˳���')
    if judge == '1':
        ts_concat_copy(length, name)
    elif judge == '2':
        ts_concat_ffmpeg(length, name)
    else:
       exit() 

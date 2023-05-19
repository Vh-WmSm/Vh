# coding=gbk
import os

# ffmpeg -i "concat:01.ts|02.ts|03.ts" -c copy out.mp4�����ַ������ӳ��������Ͼ���mp4�ļ��ˣ����Ҿ������±�����ļ����ܻ��С�������Ƽ���ffmpeg���ӣ�
def ts_concat_ffmpeg(start, length, name):
    s = ''
    for i in range(start, length-1):
        s += '{}.ts|'.format(i)
    s += '{}.ts'.format(length-1)
    order = 'ffmpeg -i "concat:{}" -c copy {}.mp4'.format(s, name)
    print(order)
    #os.system(order)

# ����cmd���copy /b *.ts name.mp4�����ַ������ӳ����ı��ʻ���ts�ļ���ֻ�Ǹ��˺�׺��
def ts_concat_copy(start, length, name):
    str_ = ''
    for i in range(start, length):
        str_ += "{}.ts+".format(i)
    # ȥ�����һ���Ӻ�
    str1 = str_[:len(str_) - 1]  # ����str1 = '0.ts+1.ts+...+n.ts'
    order = 'copy /b {} {}.mp4'.format(str1, name)
    os.system(order)

if __name__ == '__main__':
    address = input('ts�ļ���ַ��')
    os.chdir(address)
    num = input('������ts�ļ���һ�������һ����ţ��ո�ָ�����')
    start = int(num.split()[0])
    length = int(num.split()[1]) + 1
    name = input('����ļ���������д��׺����')
    judge = input('1.copy��2.ffmpeg��3.�������˳���')
    if judge == '1':
        ts_concat_copy(start, length, name)
    elif judge == '2':
        ts_concat_ffmpeg(start, length, name)
    else:
       exit() 

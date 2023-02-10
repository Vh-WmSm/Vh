# coding=gbk
import os

# ffmpeg -i "concat:01.mp4|02.mp4|03.mp4" -c copy out.mp4
def ts_concat_ffmpeg(length, name):
    s = ''
    for i in range(length-1):
        s += '{}.ts|'.format(i)
    s += '{}.ts'.format(length-1)
    order = 'ffmpeg -i "concat:{}" -c copy {}.mp4'.format(s, name)
    os.chdir('C:\\users\\vh-暖夏\\desktop\\in')
    os.system(order)

# 运用cmd命令：copy /b *.ts name.mp4
def ts_concat_copy(length, name):
    str_ = ''
    for i in range(length):
        str_ += "{}.jc+".format(i)
    # 去除最后一个加号
    str1 = str_[:len(str_) - 1]  # 生成str1 = '0.ts+1.ts+...+n.ts'
    order = 'copy /b {} {}.mp4'.format(str1, name)
    os.chdir('C:\\users\\vh-暖夏\\desktop\\in')
    os.system(order)

if __name__ == '__main__':
    length = int(input('请输入ts文件最后一个编号(ts文件应放在桌面的in文件夹)：')) + 1
    name = input('输出文件名（不用写后缀）：')
    judge = input('1.copy。2.ffmpeg。3.其他：退出：')
    if judge == '1':
        ts_concat_copy(length, name)
    elif judge == '2':
        ts_concat_ffmpeg(length, name)
    else:
       exit() 

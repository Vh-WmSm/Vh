# coding=gbk
import os

# ffmpeg -i "concat:01.ts|02.ts|03.ts" -c copy out.mp4（这种方法连接出来本质上就是mp4文件了，而且经过重新编码后文件可能会变小，所以推荐用ffmpeg连接）
def ts_concat_ffmpeg(start, length, name):
    s = ''
    for i in range(start, length-1):
        s += '{}.ts|'.format(i)
    s += '{}.ts'.format(length-1)
    order = 'ffmpeg -i "concat:{}" -c copy {}.mp4'.format(s, name)
    print(order)
    #os.system(order)

# 运用cmd命令：copy /b *.ts name.mp4（这种方法连接出来的本质还是ts文件，只是改了后缀）
def ts_concat_copy(start, length, name):
    str_ = ''
    for i in range(start, length):
        str_ += "{}.ts+".format(i)
    # 去除最后一个加号
    str1 = str_[:len(str_) - 1]  # 生成str1 = '0.ts+1.ts+...+n.ts'
    order = 'copy /b {} {}.mp4'.format(str1, name)
    os.system(order)

if __name__ == '__main__':
    address = input('ts文件地址：')
    os.chdir(address)
    num = input('请输入ts文件第一个和最后一个编号（空格分隔）：')
    start = int(num.split()[0])
    length = int(num.split()[1]) + 1
    name = input('输出文件名（不用写后缀）：')
    judge = input('1.copy。2.ffmpeg。3.其他：退出：')
    if judge == '1':
        ts_concat_copy(start, length, name)
    elif judge == '2':
        ts_concat_ffmpeg(start, length, name)
    else:
       exit() 

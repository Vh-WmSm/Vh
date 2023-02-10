import os


def time_f(time):
    if len(time) == 1:
        if len(str(time)) == 1:
            time = '00 00 0{}'.format(''.join(time))
        else:
            time = '00 00 {}'.format(''.join(time))
        time = time.split()
    elif len(time) == 2:
        time = ' '.join(time)
        time = '00 ' + time
        time = time.split()
    return time


def time_add(start, add):
    start_ = time_f(start.split(':'))
    add_ = time_f(add.split(':'))
    end = []
    up = 0
    sec = int(start_[2]) + int(add_[2])
    if sec >= 60:
        up = 1
        end.append(sec - 60)
    else:
        end.append(sec)
    min = int(start_[1]) + int(add_[1]) + up
    if min >= 60:
        up = 1
        end.append(min - 60)
    else:
        up = 0
        end.append(min)
    hour = int(start_[0]) + int(add_[0]) + up
    if hour >= 24:
        end.append(hour - 24)
    else:
        end.append(hour)
    end.reverse()
    end_ = []
    for i in end:
        if len(str(i)) == 1:
            end_.append('0' + str(i))
        else:
            end_.append((str(i)))
    return ':'.join(end_)


location = input('文件位置：')
file_in = input('要拆分的文件(不加后缀)：')
file_in_ = '"' + file_in + '.mp4' + '"'
file_txt = input('txt文件名(不加后缀)：')
time_difference = input('时间差：')
out_location = input('输出位置：')
start = ':'.join(input('裁剪开始时间：').split())
os.chdir(location)
with open(location + '\\{}.txt'.format(file_txt), 'r', encoding='utf-8-sig') as f:
    content = f.read().split('\n')
for con in content:
    lis = con.split()
    time_add_ = time_add(start, lis[1])
    file_out = '"' + lis[0] + '.mp4' + '"'
    order = 'ffmpeg -ss {} -to {} -i {} -c copy {}'.format(start, time_add_, file_in_, file_out)
    os.system(order)
    move_order = 'move {} {}'.format(file_out, out_location)
    os.system(move_order)
    start = time_add(time_add_, time_difference)

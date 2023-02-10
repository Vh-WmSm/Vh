import os


def time_add(start, add):
    start_ = start.split(':')
    add_ = add.split(':')
    if len(add_) == 1:
        if len(str(add_)) == 1:
            add_ = '00 00 0{}'.format(''.join(add_))
        else:
            add_ = '00 00 {}'.format(''.join(add_))
        add_ = add_.split()
    elif len(add_) == 2:
        add_ = ' '.join(add_)
        add_ = '00 ' + add_
        add_ = add_.split()
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


if __name__ == '__main__':
    judge = input('输入两个时间还是读取txt的时间？：1 or 2：')
    if judge == '1':
        start = ':'.join(input('被加时间：(空格分隔)').split())
        add = ':'.join(input('所加时间：').split())
        print(time_add(start, add))
    elif judge == '2':
        location = input('文件位置：')
        file = input('文件名(不加后缀)：')
        time_different = input('时间差：')
        os.chdir(location)
        with open('{}.txt'.format(file), 'r', encoding='utf-8') as f:
            lis = f.read().split('\n')
        lis_ = []
        for li in lis:
            lis_.append(li.split()[1])
        time_s = '00:00:00'
        for li_ in lis_:
            start = time_s
            add = li_
            time_s = time_add(start, add)
            time_s = time_add(time_s, time_different)
        print(time_s)
    else:
        print('输入有误！')
    input('键入任意继续……')

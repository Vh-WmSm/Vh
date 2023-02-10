import os


#  去掉某个符号之前的字符串，保留后面的字符串
def keep_back(same, lis):
    judge = input('1.从前数第一个这个字符。2.从后数第一个这个字符：')
    if judge == '1':
        for i in lis:
            if same in i:
                new = i.split(same, 1)[1]
                os.rename(i, new)
    elif judge == '2':
        for i in lis:
            if same in i:
                rsame_index = i.rfind(same)
                new = i[rsame_index + 1:]
                os.rename(i, new)

#  去掉某个符号之后的字符串，保留之前的字符串但保留后缀
def del_back(same, lis):
    judge = input('1.从前数第一个这个字符。2.从后数第一个这个字符：')
    if judge == '1':
        for i in lis:
            if same in i:
                suffix_index = i.rfind('.')
                suffix = i[suffix_index:]
                new = i.split(same, 1)[0] + suffix
                os.rename(i, new)
    elif judge == '2':
        for i in lis:
            if same in i:
                suffix_index = i.rfind('.')
                suffix = i[suffix_index:]
                rsame_index = i.rfind(same)
                new = i[:rsame_index] + suffix
                os.rename(i, new)
# 删除某个字符
def del_mark(x, lis):
    judge = input('1.删除所有这个字符。2.删除从前数第一个这个字符。3.删除从后数第一个：')
    if judge == '1':
        new_name = ''
        for li in lis:
            if x in li:
                for i in li:
                    if i != x:
                        new_name += i
                os.rename(li, new_name)
                new_name = ''
    elif judge == '2':
        for li in lis:
            if x in li:
                index = li.find(x)
                new_name = li[:index] + li[index + 1:]
                os.rename(li, new_name)
    elif judge == '3':
        for li in lis:
            if x in li:
                index = li.rfind(x)
                new_name = li[:index] + li[index + 1:]
                os.rename(li, new_name)


# 替换某个字符串
def replace(x, x_replace, lis):  # 事实上有一个方法叫replace()，不用下面这么麻烦，而现在懒得改了
    while True:
        judge = input('1.替换所有这个字符。2.替换从前数第一个这个字符。3.替换从后数第一个：')
        if judge == '1':
            for li in lis:
                if x in li:
                    new_name = x_replace.join(li.split(x))
                    os.rename(li, new_name)
            break

        elif judge == '2':
            for li in lis:
                if x in li:
                    new_name = x_replace.join(li.split(x, 1))
                    os.rename(li, new_name)
            break

        elif judge == '3':
            for li in lis:
                if x in li:
                    find_index = li.rfind(x)
                    new_name = li[:find_index] + x_replace + li[find_index + 1:]
                    os.rename(li, new_name)
            break

        else:
            print('输入错误，请重新输入……')


# 在某个字符后n个位置加入某个字符
def add(x, add_x, lis):
    place_index = int(input('把字符add_x加入字符x的后多少位？（若就放x的后面，就写1）：'))
    for li in lis:
        if x in li:
            x_index = li.find(x)
            new_name = li[:x_index + 1 + place_index - 1] + add_x + li[x_index + place_index - 1 + 1:]
            os.rename(li, new_name)
            # print(new_name)


if __name__ == '__main__':
    address = input('地址（不写默认py文件所在地址）：')
    if address == '':
        address = os.getcwd()
    os.chdir(address)

    while True:
        lis = os.listdir()
        judge = input(
            '1.del *.xml\n2.去掉前或后数第一个字符以及前面的，保留其后面的\n3.去掉某个符号之后的字符串，保留之前的字符串但保留后缀\n'
            '4.删除某个字符\n5.替换某个字符串\n6.在某个字符x后n个位置加入某个字符add_x（x仅从前数第一个）\n请选择：')

        if judge == '1':
            os.system('del *.xml')
        elif judge == '2':
            same = input('请输入相同部分（这个部分之后的都会保留）：')
            keep_back(same, lis)
        elif judge == '3':
            same = input('请输入相同部分（这个部分之前的及.后缀都会保留）：')
            del_back(same, lis)
        elif judge == '4':
            x = input('删除哪个符号：')
            del_mark(x, lis)

        elif judge == '5':
            x = input('替换哪个字符串？')
            x_replace = input('替换为：')
            replace(x, x_replace, lis)
        elif judge == '6':
            x = input('以哪个字符为基准：')
            add_x = input('加入什么字符：')
            add(x, add_x, lis)
        else:
            print('输入有误，请重新输入')
            continue

        print('重命名完成')
        jud = input('继续直接回车，退出则任意键再回车：')
        if jud != '':
            break

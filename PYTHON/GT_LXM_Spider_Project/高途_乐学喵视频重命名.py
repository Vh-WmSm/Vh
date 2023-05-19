import os
import sys

choice = input('数学1、英语2、政治3：')
address = input('地址(不填默认py文件当前位置)：')
if address != '':
    os.chdir(address)
lis = os.listdir()
order_list = []


def xiaoguo(order_list):
    print('以下为order的效果：')
    for order in order_list:
        print(order)
    judge = input('是否确认rename？Y(或直接回车)/N：')
    if judge == 'y' or judge == 'Y' or judge == '':
        for order in order_list:
            os.rename(order[0], order[1])
    else:
        sys.exit()
if choice == '1':
    key_word = ['高数', '线代', '零基础', '概率']
    for li in lis:
        for key in key_word:
            if key in li:
                new_name_ = '.'.join(li.split(key)[1].split('-'))
                order = [li, new_name_]
                order_list.append(order)
        
            
    
elif choice  == '2':
    lis = os.listdir()
    for li in lis:
        if '讲' in li:
            num = li.split('第')[1].split('讲')[0]
            for i in range(len(li)):
                if li[i] == '讲':
                    if li[i + 1] == ' ':
                        name = li[i + 2:]
                    else:
                        name = li[i + 1:]
            new_name = num + '.' + name
            order = [li, new_name]
            order_list.append(order)
            
        
elif choice == '3':
    lis = os.listdir()
    for li in lis:
        if '：' in li:
            name = li.split('：')[1]
            num = li.split('：')[0].split('课时')[1]
        
            new_name = num + '.' + name
            if '沐' in new_name or '怡' in new_name:
                try:
                    new_name = '讲'.join(new_name.split('沐'))
                except:
                    continue
                try:
                    new_name = '思'.join(new_name.split('怡'))
                except:
                    continue
            if '技' in new_name:
                start = new_name.find('技') + 1
                end = new_name.rfind('0')
                els = new_name[start:end]
                new_name = '巧'.join(new_name.split(els))
            order = [li, new_name]
            order_list.append(order)
else:
    print('输入有误，退出程序！')
    sys.exit()
xiaoguo(order_list)


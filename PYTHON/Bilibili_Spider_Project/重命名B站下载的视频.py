import os
# 【考研必备】信号与系统专业基础复习课      《信号与系统》郑君里 (P1. 信号与系统-第1课_高清)


lis = os.listdir()
s = '【考研 北邮】 通信原理【雪山灰虎】 (P'
for li in lis:
    if s in li:
        start = s.rfind('P')
        new_name = ''.join(li[start + 1:].split(')'))  # 去除P及之前的和')'
        new_name_ = '.'.join(new_name.split('. '))  # 根据需要自行添加代码
        order = 'rename "{}" "{}"'.format(li, new_name)
        # print(order)
        os.system(order)


        # 笔记：os还有这个功能
        # os.rename(i, i[start:])用这个可以不用system
        

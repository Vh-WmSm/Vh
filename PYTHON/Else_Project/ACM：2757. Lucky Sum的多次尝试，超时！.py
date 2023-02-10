# coding=gbk
import time
import math
from bisect import bisect  # 终于找到了一个很牛逼的东西，呜呜呜！可以返回列表或元组中比某数大的下一个位置的下标

# 就是可以，比如a = [2,3,4,5]  print(a[bisect(2.5)])--->3

# t0 = time.time()
a = [4, 7]
b = []
con = [(4, 7)]
for j in range(9):
    for i in a:
        b.append(i * 10 + 4)
        b.append(i * 10 + 7)
    a = b
    con.append(tuple(b))
    b = []
l, r = map(int, input().split())
s = 0
for i in range(l, r + 1):
    k = len(str(i)) - 1
    tup_t = con[k]
    if tup_t[len(tup_t) - 1] < i:  # 假如i为8，大于(4, 7)元组的最后一个数，不应该取元组(4, 7)，应取(44, 47, 74, 77)，故有此if
        tup_t = con[k + 1]

# 结果还是不尽如人意，这个bisect函数本质上还是二分法，只不过不需要我手动编写罢了，还是太耗时了，放弃！
    e = bisect(tup_t, i)
    if tup_t[e - 1] == i:
        s += tup_t[e - 1]
    else:
        s += tup_t[e]
print(s)


#     得到美丽数列表并将他们按位数分类放入元组后，下一步操作以下采用二分法求与比i大的那个完美数，比较耗时，淘汰
#     while True:
#         cut = (x + y) / 2
#         cut_down = math.floor(cut) - 1
#         cut_up = math.ceil(cut) - 1
#         if i < tup_t[0]:
#             s += tup_t[0]
#             break
#
#         else:
#             if tup_t[cut_down] < i and tup_t[cut_up] > i:
#                 s += tup_t[cut_up]
#                 break
#             elif tup_t[cut_down] < i and tup_t[cut_up] < i:
#                 x = cut_up + 1
#             elif tup_t[cut_down] > i and tup_t[cut_up] > i:
#                 y = cut_down + 1
#             elif tup_t[cut_down] == i:
#                 s += tup_t[cut_down]
#                 break
#             else:
#                 s += tup_t[cut_up]
#                 break
# print(s)


# 得到美丽数列表的第一次尝试，此法比较耗时，淘汰

# datas = [4, 7]
# for i in range(2000):
#     datas.append(datas[i] * 10 + 4)
#     datas.append(datas[i] * 10 + 7)
# t1 = time.time()
# print(datas)
# print(len(datas))

# coding=gbk
import time
import math
from bisect import bisect  # �����ҵ���һ����ţ�ƵĶ����������أ����Է����б��Ԫ���б�ĳ�������һ��λ�õ��±�

# ���ǿ��ԣ�����a = [2,3,4,5]  print(a[bisect(2.5)])--->3

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
    if tup_t[len(tup_t) - 1] < i:  # ����iΪ8������(4, 7)Ԫ������һ��������Ӧ��ȡԪ��(4, 7)��Ӧȡ(44, 47, 74, 77)�����д�if
        tup_t = con[k + 1]

# ������ǲ��������⣬���bisect���������ϻ��Ƕ��ַ���ֻ��������Ҫ���ֶ���д���ˣ�����̫��ʱ�ˣ�������
    e = bisect(tup_t, i)
    if tup_t[e - 1] == i:
        s += tup_t[e - 1]
    else:
        s += tup_t[e]
print(s)


#     �õ��������б������ǰ�λ���������Ԫ�����һ���������²��ö��ַ������i����Ǹ����������ȽϺ�ʱ����̭
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


# �õ��������б�ĵ�һ�γ��ԣ��˷��ȽϺ�ʱ����̭

# datas = [4, 7]
# for i in range(2000):
#     datas.append(datas[i] * 10 + 4)
#     datas.append(datas[i] * 10 + 7)
# t1 = time.time()
# print(datas)
# print(len(datas))

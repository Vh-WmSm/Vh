def switch_case(op):
    ops = {
        '+': 1,
        '-': 2,
        '*': 3,
        '/': 4,
    }
    return ops.get(op, None) # None为default的意思，若op不是加减乘除，则返回None


if __name__ == '__main__':
    datas = list(input().split())
    datas[0] = int(datas[0])
    datas[1] = int(datas[1])
    if switch_case(datas[2]) == 1:
        print(datas[0] + datas[1])
    elif switch_case(datas[2]) == 2:
        print(datas[0] - datas[1])
    elif switch_case(datas[2]) == 3:
        print(datas[0] * datas[1])
    else:
        out = datas[0] / datas[1]
        out_t = datas[0] % datas[1]
        if out_t == 0:
            print("{:.0f}".format(out))
        else:
            print("{:.2f}".format(out))


import phone
from time import *
import re


def menu():
    print("欢迎来到查询小程序")
    print("1.查询")
    print("2.用户")


def p(n):
    if re.match(r'1[3,4,5,7,8]\d{9}', n):
        if re.match(r'13[0,1,2]\d{8}', n) or \
                re.match(r"15[5,6]\d{8}", n) or \
                re.match(r"18[5,6]", n) or \
                re.match(r"145\d{8}", n) or \
                re.match(r"176\d{8}", n):
            return True
        elif re.match(r"13[4,5,6,7,8,9]\d{8}", n) or \
                re.match(r"147\d{8}|178\d{8}", n) or \
                re.match(r"15[0,1,2,7,8,9]\d{8}", n) or \
                re.match(r"18[2,3,4,7,8]\d{8}", n):
            return True
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    s = 0
    menu()
    while True:
        op = int(input("请输入:"))
        if op == 1:
            phoneNum = str(input("请输入你的电话号码:"))
            if p(phoneNum) == False:
                print("该手机号无效")
                for i in range(100):
                    print('\n')
                menu()
            else:
                info = phone.Phone().find(phoneNum)
                print("手机号码:" + str(info["phone"]))
                print("手机所属地:" + str(info["province"]) + "省" + str(info["city"]) + "市")
                print("邮政编号:" + str(info["zip_code"]))
                print("区域号码:" + str(info["area_code"]))
                print("手机类型:" + str(info["phone_type"]))
                s += 1
                i = input("输入任意数退出...")
                menu()
        if op == 2:
            print("使用次数:" + str(s))
            i = input("输入任意数退出...")
            menu()

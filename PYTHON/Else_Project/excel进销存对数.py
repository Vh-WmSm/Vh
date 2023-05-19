import openpyxl
import os

location = input('文件位置：')
os.chdir(location)
file = input('文件名(要加后缀)：')
line = int(input('行数：'))
wb = openpyxl.load_workbook(file)
sheet = wb.active
for i in range(2, line + 1):
    a = sheet['C{}'.format(i)].value
    if a == None:
        continue
    key = 0
    for j in range(2, line + 1):
        if a == sheet['A{}'.format(j)].value:
            key = j
            break
    if key == 0:
        sheet['G{}'.format(i)] = '左边无这个产品名'
        continue
    judge = sheet['C{}'.format(i + 1)].value
    judge_ = sheet['C{}'.format(i + 2)].value
    judge__ = sheet['C{}'.format(i + 3)].value
    judge___ = sheet['C{}'.format(i + 4)].value
    if judge != None or (judge == None and judge_ == None and judge__ == None and judge___ == None):
        x = str(sheet['F{}'.format(i)].value)
    else:
        x = str(sheet['F{}'.format(i)].value) + '+' + str(sheet['F{}'.format(i + 1)].value)
    y = str(sheet['B{}'.format(key)].value)
    if '=' in x:
        x = x[1:]
    else:
        x = x
    if '=' in y:
        y = y[1:]
    else:
        y = y
    sheet['G{}'.format(i)] = float(eval(x)) - float(eval(y))
wb.save('py_{}'.format(file))
wb.close()


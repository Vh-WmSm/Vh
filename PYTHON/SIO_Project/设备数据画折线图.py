import openpyxl
from openpyxl.chart import *
import os
# # 获取桌面路径
# desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
path = input('位置(请把所有xls文件放在一个以时间区间命名的文件夹)：')
# 从路径地址获取时间区间
during_time = path.split('\\')[-1]
os.chdir(path)
lis = os.listdir()
for li in lis:
    suffix = li.split('.')[1]
    # 找到xls的文件
    if suffix in ('xls', 'xlsx'):
        # 重命名后缀为xlsx（因为openpyxl不能打开xls）
        if suffix == 'xls':
            os.rename(li, li + 'x')
            name = li + 'x'
        else:
            name = li
        # 打开文件
        wb = openpyxl.load_workbook(path + '\\' + name)
        # 获取第一个表
        sheet = wb.active
        # 获取行数
        sheet_row = sheet.max_row
        # 让设备名-变量名称-从机名称为保存的文件名
        file_name = sheet['a2'].value + '-' + sheet['c2'].value + '-' + sheet['e2'].value
        # 遍历每一行，把值一列的str类型改为int类型（int类型才可作出折线图）
        for i in range(2, sheet_row + 1):
            try:
                sheet[f'G{i}'] = int(sheet[f'G{i}'].value)
            except:
                pass
        # 画折线图，定义LineChart对象
        chart = LineChart()
        # 定义x坐标的数据
        x_data = Reference(sheet, min_col=6, min_row=2, max_col=6, max_row=sheet_row)
        # 定义作图数据列
        data = Reference(sheet, min_col=7, min_row=1, max_col=7, max_row=sheet_row)
        # 添加数据到chart（from_rows=False说明是以列数据来画图，titles_from_data=False说明不画图例，若为True则以第一行文字写图例，这时上方的data处应min_row=1）
        chart.add_data(data, from_rows=False, titles_from_data=True)
        # 添加x坐标数据
        chart.set_categories(x_data)
        # 定义纵坐标名称
        chart.y_axis.title = '值'
        # 定义横坐标名称
        chart.x_axis.title = '时间'
        # 定义折线图标题
        chart.title = during_time + '-' + file_name
        # 把折线图画在sheet表的i2处
        chart.anchor = 'i2'
        # 设置折线图大小
        chart.height = 50
        chart.width = 150
        sheet.add_chart(chart)
        # 保存
        wb.save(f'{path}\\{file_name}.xlsx')
        # 关闭
        wb.close()


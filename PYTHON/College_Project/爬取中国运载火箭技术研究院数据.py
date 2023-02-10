# coding=gbk
import requests
import bs4
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '卫星'
title_data = ['发射时间', '发射卫星']
sheet.append(title_data)
k = 1
for i in range(9):
    if i == 0:
        url = 'http://www.calt.com/n482/n505/index.html'
        j = 9
    else:
        url = 'http://www.calt.com/n482/n505/index_3805_' + str(9 - i) + '.html'
        j = 1
    res = requests.get(url)
    res.encoding = 'utf-8'
    bs_satellite = BeautifulSoup(res.text, 'html.parser')
    items = bs_satellite.find_all('table')[j].find_all('tr')

    for item in items:
        if item == items[0]:
            continue
        k = k+1
        date = item.find_all('td')[0]
        satellite = item.find_all('td')[2]
        # sheet['A'+str(k)] = date.text
        # sheet['B'+str(k)] = satellite.text
        # 或
        data_satellite = [date.text, satellite.text]
        sheet.append(data_satellite)
wb.save('2019——2021中国发射的卫星.xlsx')
wb.close()

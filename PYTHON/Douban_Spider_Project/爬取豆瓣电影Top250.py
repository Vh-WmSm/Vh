# coding=gbk
import openpyxl
import requests
from bs4 import BeautifulSoup

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '�����Ӱ'
column_name = ['��Ӱ����', '����', 'ժҪ', '����', '��ַ']
sheet.append(column_name)

headers = {'User-Agent': 'Mozilla/5.0 '
                         '(Windows NT 10.0; Win64; x64) AppleWebKit'
                         '/537.36 (KHTML, like Gecko) Chrome/99.0.48'
                         '44.74 Safari/537.36 Edg/99.0.1150.52'}
for i in range(0, 226, 25):
    if i == 0:
        url = 'https://movie.douban.com/top250'
    else:
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i)
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    lis = bs.find_all('div', class_="info")
    for li in lis:
        title = li.find('div', class_='hd').find('a').find('span').text
        score = li.find('div', class_="star").find_all('span')[1].text
        try:
            summary = li.find('div', class_='bd').find_all('p')[1].text.replace(' ', '').replace('\n', '')
        except:
            summary = ''
        property_ = li.find('div', class_='bd').find('p').text.replace(' ', '').encode('gbk', 'ignore').decode('gbk')
        l_property = property_.split('\n')
        url_mov = li.find("div", class_='hd').find('a')['href']
        li_data = [title, score, summary, l_property[2], url_mov]
        sheet.append(li_data)
wb.save('C:\\users\\vh-ů��\\desktop\\����Top250��Ӱ.xlsx')
wb.close()
print('Done')



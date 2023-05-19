# coding=gbk
import requests
from bs4 import BeautifulSoup
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = '�����Ӱ'
column_name = ['��Ӱ����', '����', '��ַ']
sheet.append(column_name)

url = 'https://movie.douban.com/cinema/nowplaying/foshan/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win'
                         '64; x64) AppleWebKit/537.36 (KHTML,'
                         ' like Gecko) Chrome/99.0.4844.74 Safa'
                         'ri/537.36 Edg/99.0.1150.52'}
res = requests.get(url, headers=headers)
bs = BeautifulSoup(res.text, 'html.parser')
lis = bs.find('ul', class_='lists').find_all('ul', class_='')
for li in lis:
    title = li.find('li', class_="stitle").text.replace(' ', '').replace('\n', '')
    try:
        score = li.find('li', class_="srating").text
    except:
        score = ''
    url = li.find('li', class_="stitle").find('a')['href']
    data = [title, score, url]
    sheet.append(data)
wb.save("C:\\users\\vh-ů��\\desktop\\������ӳ��Ӱ��.xlsx")
wb.close()
print('Done!')

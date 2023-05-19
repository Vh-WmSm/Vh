from PIL import Image
import pytesseract
import os
import time

address = input('图片所在地址（直接回车默认py文件所在位置）：')
if address == '':
    img_names = os.listdir()
else:
    os.chdir(address)
    img_names = os.listdir(address)
img_names_ = []
judge = input('需要重命名.png文件吗？（直接回车则不需要），按1需要：')
if judge == '1':
    same_name = input('输入名字相同的部分：')
    for i in img_names:
        newname = ''.join(i.split(same_name))
        os.rename(i, newname)
        

for i in img_names:
    if '.png' in i:
        img_names_.append(i)
img_names_.sort(key=lambda x:int(x[:-4]))  # 对os.listdir()列表进行排序


judge = input('这一系列的图片是：英文1；中文2：')

f = open('C:\\users\\vh\\desktop\\1.txt', 'a', encoding='utf-8')
for img_name in img_names_:
    if address != '':
        img = Image.open(address + '\\{}'.format(img_name))
    else:
        img = Image.open('{}.png'.format(img_name))
    if judge == '1':
        text = pytesseract.image_to_string(img)
    else:
        text = ''.join(pytesseract.image_to_string(img, lang='chi_sim').split())
    f.write(text)
f.close

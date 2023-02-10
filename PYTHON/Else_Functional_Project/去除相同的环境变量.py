import os

os.chdir('c:\\users\\vh\\desktop')
with open('1.txt', 'r', encoding='utf-8') as f:
    content_list = f.read().split(';')
re_li = []
for li in content_list:
    if li not in re_li:
        re_li.append(li)
print(';'.join(re_li))

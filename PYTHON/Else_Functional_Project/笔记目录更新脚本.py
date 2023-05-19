import os

path = input('地址：')
name = input('文件名(不用写.txt)：')
class_ = input('标题级数：')
if '' in (path, name, class_):
    print('未完全填写信息！')
    exit(0)
class_ = int(class_)
os.chdir(path)
f_r = open(f'{name}.txt', 'r', encoding='utf-8')
catalogue = '目录：'
content = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
coun = 0
tem_lis = []
for i in range(class_ - 1, -1, -1):
    tem_lis.append(i) # 生成对应列表
    
while True:
    line = f_r.readline()
    try:
        if line[0] == '~': # 用while True找到第一个分割线（目录与正文的分割线）
            break
    except Exception:
        pass
while line != '':
    line = f_r.readline()
    content += line
    coun = line.count('*', 0, 4) # 数数多少个*，最多四级标题
    
    try:
        if coun == class_: # 一级标题
            catalogue += '\n' + line
        elif line[0] == '*':
            catalogue += '     ' * tem_lis[coun - 1] + line
    except Exception:
        pass
f_r.close()
with open(f'{name}.txt', 'w', encoding='utf-8') as f_w:
    f_w.write(catalogue + '\n' + content)

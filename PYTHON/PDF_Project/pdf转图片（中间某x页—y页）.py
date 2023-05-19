from pdf2image import convert_from_path
import os


def rename(address, next_dir_index):
    same = '-'  # 删除从后往前数第一个相同字符same以及它前面的，保留后面的（重命名措施）
    os.chdir(address + '\\{}'.format(next_dir_index))
    lis = os.listdir()
    rname = ''
    for i in lis:
        if same in i:
            rsame_index = i.rfind(same)
            new = i[rsame_index + 1:]
            rname += 'rename {} {}&&'.format(i, new)
    rname = rname[:-2]
    rname += str(next_dir_index)
    with open(address + '\\1.txt', 'w', encoding='utf-8') as f:
        f.write(str(rname))

address, name = input('地址 文件名：').strip().split()
name += '.pdf'
first_page, last_page = map(int, input('开始页 结束页：').strip().split())
os.chdir(address)

lis = os.listdir()
find_max_num = []
for li in lis:
    if os.path.isdir(li):
        try:
            float(li)  # 使用float()方法转换数字，要是是数字不会报错，否则会报错
            find_max_num.append(int(li))  # 是数字则把它加入这个列表暂存
        except:
            pass
try:  # 若try出错，说明find_max_num为空，max函数无效了
    next_dir_index = max(find_max_num) + 1
except:
    next_dir_index = 1
os.mkdir(str(next_dir_index))

image = convert_from_path(name, dpi=150, fmt='jpeg', output_folder=address + '\\{}'.format(next_dir_index), first_page=first_page,
                          last_page=last_page, thread_count=3,
                          poppler_path=r'C:\poppler-23.05.0')

rename(address, next_dir_index)

import os

os.chdir('C:\\Users\\Vh\\OneDrive\\my_project\\NOTES\\Linux_Git_Notes')
f_r = open('Linux_Git_Study_Notes.txt', 'r', encoding='utf-8')
catalogue = '目录：'
content = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
while True:
    line = f_r.readline()
    try:
        if line[0] == '~':
            break
    except Exception:
        pass
while line != '':
    line = f_r.readline()
    content += line
    # 如果是章节里的子标题
    try:
        if line[0] == '*' and line[1] != '*':
            if line[-2] == ':' or line[-2] == '：':
                catalogue += line[:-2] + '\n'
            else:
                catalogue += line
    # 如果是章节标题
        elif line[:2] == '**':
            if line[-2] == ':' or line[-2] == '：':
                catalogue += '\n' + line[:-2] + '\n'
            else:
                catalogue += '\n' + line
    except Exception:
        pass
f_r.close()
with open('Linux_Git_Study_Notes.txt', 'w', encoding='utf-8') as f_w:
    f_w.write(catalogue + '\n' + content)

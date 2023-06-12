import os
import public_tools
import openpyxl


def fun(lastPath, path):
    global s, needSuffix
    os.chdir(path)
    lis = os.listdir()
    for li in lis:
        if os.path.isdir(f'{path}\\{li}'):
            fun(os.getcwd(), f'{os.getcwd()}\\{li}')
        else:
            if needSuffix == '2':
                li = li.rsplit('.', 1)[0]
            s += li + ' '
            xl.append(li)
    os.chdir(lastPath)



if __name__ == '__main__':
    desktop_path = public_tools.My_Tool.get_desktop_path()
    title_name_lis = ['请选择要递归的文件夹(默认桌面):', '是否需要文件名后缀(1.是/2.否):', '选择什么容器(1.xlsx/2.txt):', '存储方式(1.横竖排列/2.仅横排)', '容器文件生成位置(默认桌面):']
    windows_name = '文件夹内递归搜集所有文件名小工具'
    button_name = '开始递归'
    default_value_lis = [desktop_path, '2:2', '2:2', '2:2', desktop_path]
    GUI = public_tools.PySimpleGUI_Tool(title_name_lis, windows_name, button_name, default_value_lis)
    originPath, needSuffix, containerSelect, storageMode, targetPath = GUI.gui_windows()
    s = ''
    xl = []
    fun(originPath, originPath)

    if(containerSelect == '2'):
        with open(f'{targetPath}\\AllFileName.txt', 'w', encoding='utf-8') as f:
            f.write(s)
            if storageMode == '1':
                s = '\n'.join(s.split(' '))
                f.write('\n\n' + s)
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(xl)
        if storageMode == '1':
            count = 3
            for x in xl:
                ws[f'a{count}'] = x
                count += 1
        wb.save(f'{targetPath}\\AllFileName.xlsx')
        wb.close()

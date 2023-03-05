'''
Author: Vh-WmSm
Date: 2023.3.2
Version: Object oriented 4.0
Updated Content:
Add: 1.新增了默认参数记录，每次循环默认参数自动改为上一次
     2.新增了GUI图形用户界面，参数更直观且更容易输入与修改。
Optimize: 1.GUI图形用户界面优化了的模块之间的对齐格式、模块大小控制，使看起来更美观整齐
          2.对识别内容的字符串处理新增了一个字符串处理类，对繁琐的代码进行了分类与整合，使代码更加简洁直观
'''
import sys
from os import path
from PIL import Image
import PySimpleGUI as sg
from pytesseract import image_to_string


# 我的工具类
class My_Tool(object):
    @staticmethod
    def get_desktop_path():
        """
        function: 可以获取当前用户的桌面地址，有这项技术后，换到别的电脑就不需要该代码了
        :return: 当前用户的桌面地址
        """
        return path.join(path.expanduser('~'), 'Desktop')

    @staticmethod
    def enumerate_tuple_switch_to_list(text):
        '''
        :target:enumerate得到的是[(0, x1), (0, x2), ...] 内部修改为列表
        :param text: 一个待枚举的字符串
        :return: [[0, x1], [0, x2], ...]
        '''
        enumerate_tuple_text = enumerate(text)
        enumerate_list_text = []
        for t in enumerate_tuple_text:
            enumerate_list_text.append(list(t))
        return enumerate_list_text

    @staticmethod
    def suffix_dot_judge(str):
        '''
        :target: 判断该“.”是某文件名的后缀或是某个编号的后面的”.“，还是一句话的“。”
        :param str: 输入第二个字符是“.”的字符串
        :return: “.” 或 "。"
        '''
        file_suffix = ['.py', '.txt', '.png', '.jpg', '.mp4', '.mp3', '.m4a', '.docx', '.doc', '.xls', '.xlsx', '.ppt',
                       '.pptx']
        if str[0].isdigit():
            return '.'
        if len(str) == 2:  # 如果str长度为2，说明是句末的句号
            return '。'
        case1 = str[1] + str[2] + str[3]  # 如.py
        case2 = case1 + str[4]  # 如.txt
        case3 = case2 + str[5]  # 如.docx
        if case1 in file_suffix or case2 in file_suffix or case3 in file_suffix:
            return '.'
        else:
            return '。'

    @staticmethod
    def PySimpleGUI_Tool(windows_name, title_name_lis, default_value_lis, button_name, **kwargs):
        # 设置定义布局的列表
        layout = []
        for num in range(len(title_name_lis)):  # 根据title_name_lis的长度动态添加窗口栏目列表
            # layout.append([sg.Column([[sg.Text(f'{title_name_lis[num]}', size=(25, 1)), sg.In(default_value_lis[num], size=(50, 1))]],
            #                         element_justification='right', size=(400, 30))])
            layout.append(
                [sg.Text(f'{title_name_lis[num]}', size=(25, 1)), sg.In(default_value_lis[num], size=(30, 1))])
        # 最后追加一个开始按钮
        layout.append([sg.Button(button_name)])
        windows = sg.Window(windows_name, layout, keep_on_top=kwargs['keep_on_top'])  # 显示窗口
        # 设置窗口循环
        while True:
            # 获取事件和值
            event, values = windows.read()
            # 如果是关闭窗口或者None事件，退出循环
            if event in (sg.WIN_CLOSED, None):
                sys.exit()
            # 如果是点击button_name按钮事件，利用列表解析动态对应返回所有参数
            elif event == button_name:
                windows.close()  # 释放资源
                return [values[num] for num in range(len(title_name_lis))]


# 字符串处理类
class Str_Prossing_Tool(object):
    @staticmethod
    # 删除字符串中的空格
    def del_blank_space(s):
        return ''.join(s.split(' '))

    @staticmethod
    # 删除字符串中多余的空行
    def del_blank_line(s):
        # 把字符串转换为列表，使得一个字符为一个列表元素，这样操作可以避免split('\n')会删除\n的缺点
        s_lis = list(s)
        # 赋初值，防止下方temp_list[-1]访问越界
        temp_list = [s[0]]
        for t in s_lis[1:]:
            # 如果temp_list最后是\n且t本身还是\n，则跳过，以此法删除多余行
            if s_lis[-1] == '\n' and t == '\n':
                continue
            else:
                temp_list.append(t)
        # 再直接起来返回即可
        return ''.join(temp_list)

    @staticmethod
    # 删除字符串中所有的换行符，使行与行之间紧密相连
    def del_n(s):
        s_lis_temp = []
        # split('\n')若遇到两个及以上的\n，会转化为''放入列表元素中，故需剔除。注意，此处不能使用split()，因为这个是删除包括空格、\t等，而这个方法只删除所有\n
        for i in s.split('\n'):
            if i != '':
                s_lis_temp.append(i)
        # 连接起来返回即可
        return ''.join(s_lis_temp)

    @staticmethod
    # 字符串中英文标点符号改为中文
    def English_punctuation_to_Chinese(s):
        s_temp = ''
        # 枚举字符串并把枚举后的格式元组改为列表
        for i in My_Tool.enumerate_tuple_switch_to_list(s):
            if i[1] == ',':
                i[1] = '，'
            elif i[1] == ':':
                i[1] = '：'
            elif i[1] == '.':
                # 判断这个点是句号还是真的点(可能是文件名的后缀的点或序号的点，也可能是句号)
                i[1] = My_Tool.suffix_dot_judge(s[i[0] - 1:])
            elif i[1] == '(':
                i[1] = '（'
            elif i[1] == ')':
                i[1] = '）'
            s_temp += i[1]
        return s_temp


# 截图识字类
class Screenshot_Translator(object):
    @staticmethod
    def Menu(count):
        print(' ' + '=' * 46 + f'\n| 欢迎使用PY截图识字小工具4.0，现在是第{count}次运行 |\n' + ' ' + '=' * 46 + '\n\n请在弹出的窗口中写入相应参数')

    def __init__(self, count, default_parameter):
        self.Menu(count)
        # 窗口栏目标题列表
        title_name_lis = ['截图地址', '截图名', '模式(1.英文/2.中文)', '删除空白行(1.删除/2.不删除)', '删除所有换行符(1.删除/2.不删除)']
        # 调用GUI窗口工具并将其返回值拆包
        self.img_address, self.img_name, self.mode, self.del_blank_line, self.del_n = My_Tool.PySimpleGUI_Tool(
            '截图识字小工具4.0', title_name_lis, default_parameter, '开始识别', keep_on_top=True)

    # 识别截图文字
    def Identify_Screenshots(self):
        img = Image.open(self.img_address + f'\\{self.img_name}')
        # 识别英文
        if self.mode == '1':
            self.text = image_to_string(img)
        # 识别中文
        else:
            self.text = image_to_string(img, lang='chi_sim')

    # 处理识别后的文本
    def Text_Processor(self):
        # 若模式是中文，则先处理
        if self.mode == '2':
            # 中文识别后会一个字空一个空格，所以先删除空格
            self.text = Str_Prossing_Tool.del_blank_space(self.text)
            # 中文模式识别标点符号默认会识别成英文的标点符号，所以先更改标点符号
            self.text = Str_Prossing_Tool.English_punctuation_to_Chinese(self.text)
        # 剩下的两项操作中文、英文都通用，则后处理
        if self.del_blank_line == '1':
            self.text = Str_Prossing_Tool.del_blank_line(self.text)
        if self.del_n == '1':
            self.text = Str_Prossing_Tool.del_n(self.text)

    # 打印处理后的文本
    def Text_Printer(self):
        print('\n识别结果如下：\n\n' + self.text, end='\n\n')

    # 记录上一次执行的参数
    def Parameter_Recorder(self):
        # 参数自动组包后返回
        return self.img_address, self.img_name, self.mode, self.del_blank_line, self.del_n


if __name__ == '__main__':
    # 设置默认参数，自动组包赋给default_parameter
    default_parameter = My_Tool.get_desktop_path(), '1.png', '2', '2', '2'
    # 设置循环次数，方便识别一张截图后继续识别下一张
    for count in range(1, 100):
        # 创建实例对象s并代入count进行初始化
        s = Screenshot_Translator(count, default_parameter)
        # 识别截图内容
        s.Identify_Screenshots()
        # 把识别结果按要求进行处理
        s.Text_Processor()
        # 打印处理后的结果
        s.Text_Printer()
        # 接收上一次的默认参数
        default_parameter = s.Parameter_Recorder()

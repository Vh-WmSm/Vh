'''
Author: Vh-WmSm
Version: 3.0
Form: Object oriented
'''
from os import path
from PIL import Image
from pytesseract import image_to_string


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


class Screenshot_Translator(object):
    @staticmethod
    def Menu(count):
        print(' ' + '=' * 43 + f'\n| 欢迎使用PY截图识字小工具，现在是第{count}次运行 |\n' + ' ' + '=' * 43)

    def __init__(self, count):
        self.Menu(count)
        self.img_address = My_Tool.get_desktop_path()  # 获取桌面地址
        self.img_name = '1.png'
        self.mode = '中文'
        self.del_blank = '不删除'
        self.text = ''

    def Info_Change(self):
        jud = input('0.全更改；1.只更改截图位置；2.只更改截图名；3，只更改识别模式；4.只更改删除空行模式（不更改直接回车）：')
        if jud == '0':
            self.img_address = input('截图位置：')
            self.img_name = input('截图名（要带后缀）：')
            self.mode = input('识别模式：1.英文；2.中文：')
            self.del_blank = input('是否删除多余空行：1.删除；2.不删除：')
        elif jud == '1':
            self.img_address = input('截图位置：')
        elif jud == '2':
            self.img_name = input('截图名（要带后缀）：')
        elif jud == '3':
            self.mode = '1'
        elif jud == '4':
            self.del_blank = '1'
        else:
            pass

    def __str__(self):
        s = f'当前默认设置：\n截图所在地址：{self.img_address}\n截图名：{self.img_name}\n识别模式：{self.mode}\n是否删除空行：{self.del_blank}'
        return s

    # 初步识别截图的方法
    def Identify_Screenshots(self):
        img = Image.open(self.img_address + f'\\{self.img_name}')
        if self.mode == '1':
            self.text = image_to_string(img)
        else:
            self.text = image_to_string(img, lang='chi_sim')  # 识别中文
        return self.text

    # 识别后的字符串处理方法
    def Text_Processor(self):
        if self.mode == '1':
            # 英文模式不需处理
            pass
        else:
            self.text = ''.join(self.text.split(' '))  # 不知何原因，识别中文会一个字空一格，先作处理
            if self.del_blank == '1':  # 选择1，删除多余空行
                text_list = list(self.text)  # 把字符串转换为列表，使得一个字符为一个列表元素，这样操作可以避免split('\n')会删除\n的缺点
                temp_list = [text_list[0]]  # 赋初值，防止下方temp_list[-1]访问越界
                for t in text_list[1:]:
                    if temp_list[-1] == '\n' and t == '\n':  # 如果temp_list最后是\n且t本身还是\n，则跳过，以此法删除多余行
                        continue
                    else:
                        temp_list.append(t)
                self.text = ''.join(temp_list)  # 再直接连接字符串即可
            else:
                pass
            # 把英文标点符号改为中文的
            text_temp = ''
            for i in My_Tool.enumerate_tuple_switch_to_list(self.text):  # 枚举识别后的字符串
                if i[1] == ',':
                    i[1] = '，'
                elif i[1] == ':':
                    i[1] = '：'
                elif i[1] == '.':
                    i[1] = My_Tool.suffix_dot_judge(self.text[i[0] - 1:])
                elif i[1] == '(':
                    i[1] = '（'
                elif i[1] == ')':
                    i[1] = '）'
                text_temp += i[1]
            self.text = text_temp
        return self.text

    # 处理完成后的字符串打印方法
    def Text_Printer(self):
        print('\n\n识别结果如下：\n\n' + self.text, end='\n\n')


if __name__ == '__main__':
    for count in range(1, 100):
        s = Screenshot_Translator(count)
        print(str(s))
        s.Info_Change()
        s.Identify_Screenshots()
        s.Text_Processor()
        s.Text_Printer()

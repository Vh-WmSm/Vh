'''
Author: Vh-WmSm
Version: 3.0
Form: Object oriented
'''
import os
from PIL import Image
import pytesseract


class My_Tool(object):
    @staticmethod
    def get_desktop_path():
        """
        function: 可以获取当前用户的桌面地址，有这项技术后，换到别的电脑就不需要该代码了
        :return: 当前用户的桌面地址
        """
        return os.path.join(os.path.expanduser('~'), 'Desktop')

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
        :target: 判断该“.”是某文件名的后缀，还是一句话的“。”
        :param str: 输入一个由“.”开始的字符串
        :return: “.” 或 "。"
        '''
        file_suffix = ['py', 'txt', 'png', 'jpg', 'mp4', 'mp3', 'm4a', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx']
        temp = ''
        for x in str:
            if My_Tool.is_English(x):  # 如果x是字母或数字，则加入字符串temp
                temp += x
            elif x == '.':  # 给一个elif判断是不是.因为若此时是句末的句号，则text[count+1:]会越界，只能返回空字符串而不是'.'
                pass
            else:
                break  # 遇到其他字符，如中文，则退出循环
        if temp not in file_suffix:
            return '。'  # 如得到的temp与file_suffix列表比较，若不在其中，则说明不是后缀名的点，返回句号
        else:
            return '.'

    @staticmethod
    def is_English(s):
        '''
        target: 做一个识别英文字母的函数，因为isalpha()或isalnum()中文字符和英文字符都会返回True，不符合要求
        return: 如果字符串s所有字符都是英文字母，则返回True，否则返回False
        '''
        for i in s:
            if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
                return False
        else:
            return True


class Screenshot_Translator(object):
    def __init__(self):
        self.img_address = My_Tool.get_desktop_path()  # 获取桌面地址
        self.img_name = '1.png'
        self.judge = '中文'
        self.text = ''

    def Info_Change(self):
        jud = input('若要全更改请输入1，只变换识别模式请输入2（不更改直接回车）：')
        if jud == '1':
            self.img_address = input('截图位置：')
            self.img_name = input('截图名（要带后缀）：')
            print('识别模式已自动改为英文')
            self.judge = '1'
        elif jud == '2':
            self.judge = '1'

    def __str__(self):
        s = f'当前默认设置：\n截图所在地址：{self.img_address}\n截图名：{self.img_name}\n识别模式：{self.judge}'
        return s

    # 初步识别截图的方法
    def Identify_Screenshots(self):
        img = Image.open(self.img_address + f'\\{self.img_name}')
        if self.judge == '1':
            self.text = pytesseract.image_to_string(img)
        else:
            self.text = pytesseract.image_to_string(img, lang='chi_sim')  # 识别中文
        return self.text

    # 识别后的字符串处理方法
    def Text_Processor(self):
        if self.judge == '1':
            # 英文模式不需处理
            pass
        else:
            self.text = ''.join(self.text.split())  # 不知何原因，识别中文会一个字空一格，所以先作处理
            # 把英文标点符号改为中文的
        text_temp = ''
        for i in My_Tool.enumerate_tuple_switch_to_list(self.text):  # 枚举识别后的字符串
            if i[1] == ',':
                i[1] = '，'
            elif i[1] == ':':
                i[1] = '：'
            elif i[1] == '.':
                i[1] = My_Tool.suffix_dot_judge(self.text[i[0]:])
            elif i[1] == '(':
                i[1] = '（'
            elif i[1] == ')':
                i[1] = '）'
            text_temp += i[1]
        self.text = text_temp
        return self.text

    # 处理完成后的字符串打印方法
    def Text_Printer(self):
        print(self.text, end='\n\n\n')


if __name__ == '__main__':
    while True:
        s = Screenshot_Translator()
        print(str(s))
        s.Info_Change()
        s.Identify_Screenshots()
        s.Text_Processor()
        s.Text_Printer()

# 我的第一个面向对象项目
import os
from PIL import Image
import pytesseract


class My_Str_Jud(object):
    @staticmethod
    def is_English(s):  # 做一个识别英文字母的函数，因为isalpha()或isalnum()中文字符和英文字符都会返回True，不符合要求
        '''
        如果字符串s所有字符都是英文字母，则返回True
        '''
        for i in s:
            if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
                return False
        else:
            return True


class Screenshot_Translator(object):
    def __init__(self):
        self.img_address = self.get_desktop_path()
        self.img_name = '1.png'
        self.judge = '中文'
        self.text = ''

    def get_desktop_path(self):
        return os.path.join(os.path.expanduser('~'), 'Desktop')  # 可以获取当前用户的桌面地址，有这项技术后，换到别的电脑就不需要该代码了

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
            text_ = ''
            temp = ''
            count = 0
            file_suffix = ['py', 'txt', 'png', 'jpg', 'mp4', 'mp3', 'm4a', 'docx', 'doc', 'xls', 'xlsx', 'ppt', 'pptx']
            for i in self.text:
                if i == ',':
                    i = '，'
                elif i == ':':
                    i = '：'
                elif i == '.':
                    for x in self.text[count:]:  # 判断此.是句号还是一个文件名的后缀的点
                        if My_Str_Jud.is_English(x):  # 如果x是字母或数字，则加入字符串temp
                            temp += x
                        elif x == '.':  # 给一个elif是否是.因为若此时是句末的句号，则text[count+1:]会越界，只能返回空字符串而不是'.'
                            pass
                        else:
                            break  # 遇到其他字符，如中文，则退出循环
                    if temp not in file_suffix:
                        i = '。'  # 如得到的temp与file_suffix列表比较，若不在其中，则说明不是后缀名的点，可更改为句号
                elif i == '(':
                    i = '（'
                elif i == ')':
                    i = '）'
                text_ += i
                count += 1
            self.text = text_
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

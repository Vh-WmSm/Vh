'''
Author: Vh-WmSm
Date: 2023.5.18
Version: 7.0
Updated Content:
1.添加了是否转换为中文标点选项
2.优化了代码
3.删除了输出时最后多余的空行
'''

from PIL import Image
from os import path
from pytesseract import image_to_string
from public_tools import My_Tool, Str_Prossing_Tool, PySimpleGUI_Tool

# 截图识字类
class Screenshot_Translator(object):
    def __init__(self):
        file_suffix = ['.png', '.jpg', 'jpeg', '.mp4', '.mp3', '.m4a']
        suffix_in_size = 25
        folder_browse_size=6
        # 设置默认参数(截图地址，截图名，模式(英/中)，删除空白行(删/不删)，删除所有换行符(删/不删))（其中3:2代表有三个参数选第二个），自动组包赋给default_parameter
        self.default_parameter = My_Tool.get_desktop_path(), '1.png', '2:2', '2:1', '2:2', '2:2'
        # 窗口栏目标题列表
        self.title_name_lis = ['截图地址', '截图名', '模式(1.英文/2.中文)', '删除空白行(1.删除/2.不删除)', '删除所有换行符(1.删除/2.不删除)', '符号换成中文的（1.换/2.不换）']
        # 调用GUI类，创建w对象，再调用其中的gui_windows方法，将返回值拆包分别赋值
        self.w = PySimpleGUI_Tool(self.title_name_lis, windows_name='截图识字小工具7.0', button_name='开始识别',
                                  default_value_lis=self.default_parameter, file_suffix=file_suffix,
                                  suffix_in_size=suffix_in_size, folder_browse_size=folder_browse_size)

    # 识别截图文字
    def Identify_Screenshots(self):
        re_data = self.w.gui_windows()
        self.img_address, self.img_name, self.mode, self.del_blank_line, self.del_n, self.change_punctuation = re_data
        img = Image.open(self.img_address + f'\\{self.img_name}')
        # 识别英文
        if self.mode == '1':
            self.text = image_to_string(img)
        # 识别中文
        else:
            self.text = image_to_string(img, lang='chi_sim')

    # 处理识别后的文本
    def Text_Processor(self):
        # 若模式为中文，则先处理
        if self.mode == '2':
            # 对空格问题的处理
            self.text = Str_Prossing_Tool.address_space(self.text)
            # 对标点符号的处理
            if(self.change_punctuation == '1'):
                self.text = Str_Prossing_Tool.English_punctuation_to_Chinese(self.text)
        # 剩下的两项操作中文、英文都通用，则后处理
        if self.del_blank_line == '1':
            self.text = Str_Prossing_Tool.del_blank_line(self.text)
        if self.del_n == '1':
            self.text = Str_Prossing_Tool.del_n(self.text)
        self.text = self.text.strip()
        return self.text


if __name__ == '__main__':
    # 创建截图识字实例对象s
    s = Screenshot_Translator()
    while True:
        # 识别截图内容
        re_jud = s.Identify_Screenshots()
        # 把识别结果按要求进行处理，并用text接收返回内容
        text = s.Text_Processor()
        # 调用文字显示模块，弹出一个框框显示识别内容
        PySimpleGUI_Tool.popup_scrolled(text, title='识别结果')

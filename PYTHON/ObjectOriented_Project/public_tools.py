import os
import sys
from os import path
import PySimpleGUI as sg
from copy import deepcopy


# 我的工具类
class My_Tool(object):
    @staticmethod
    def get_desktop_path():
        """
        可以获取当前用户的桌面地址，有这项技术后，换到别的电脑也自动获取该电脑桌面地址，不需要改代码了
        :return: 当前用户的桌面地址
        """
        return path.join(path.expanduser('~'), 'Desktop')

    @staticmethod
    def is_English(s):
        '''
        target:做一个识别英文字母的函数，因为isalpha()或isalnum()中文字符和英文字符都会返回True，不符合要求
        param s:一个待判断的字符串或字符
        return:如果字符串s所有字符都是英文字母，则返回True
        '''
        for i in s:
            if not ('a' <= i <= 'z' or 'A' <= i <= 'Z'):
                return False
        else:
            return True

    @staticmethod
    # 很鸡肋，发现并不需要这样做，在本项目中已弃用，放着不删，可能以后有用
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
        :target: 判断该“.”是某文件名的后缀或是某个编号的后面的”.“或是某个方法的调用，还是一句话的“。”
        :param str: 输入第二个字符是“.”的字符串
        :return: “.” 或 "。"
        '''
        # 如果第一个字符是数字，说明是某个编号后面的.
        if str[0].isdigit():
            return '.'
        # 如果str长度为1或2，说明是句末的句号
        if len(str) <= 2:
            return '。'
        # 如果str长度大于2，则判断点的两侧是否有英文字母，有则返回"."，否则就返回句号
        else:
            if My_Tool.is_English(str[0]) or My_Tool.is_English(str[2]):
                return '.'
            else:
                return '。'


# 字符串处理类
class Str_Prossing_Tool(object):
    @staticmethod
    # 中英文混合时，判断该空格是英文单词的空格还是识别中文时产生的空格
    def address_space(s):
        target_s = ''
        # 遍历枚举后的s
        for i in enumerate(s):
            # 如果是空格，则判断一下再考虑是否加入target_s字符串
            if i[1] == ' ':
                # 把该空格的前后两个字符进行判断是否是英文，若两边都是英文，则说明是单词间的空格，这个空格要被保留
                if My_Tool.is_English(s[i[0] - 1] + s[i[0] + 1]):
                    target_s += i[1]
                # 若该空格不符合要求，则不加入target_s字符串，pass跳过它即可
                else:
                    pass
            # 如果不是空格，则加入target_s字符串即可
            else:
                target_s += i[1]
        return target_s

    @staticmethod
    # 删除字符串中多余的空行
    def del_blank_line(s):
        # 把字符串转换为列表，使得一个字符为一个列表元素，这样操作可以避免split('\n')会删除\n的缺点
        s_lis = list(s)
        # 赋初值，防止下方temp_list[-1]访问越界
        temp_list = [s[0]]
        for t in s_lis[1:]:
            # 如果temp_list最后是\n且t本身还是\n，则跳过，以此法删除多余行
            if temp_list[-1] == '\n' and t == '\n':
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
        # 枚举s后遍历
        for i in enumerate(s):
            # 如果上一次循环已经在s_temp连入了省略号，说明后面的点都是省略号识别出来的点，可以忽略了
            if s_temp != '' and s_temp[-1] == '……' and i[1] == '.':
                continue
            if i[1] == ',':
                s_temp += '，'
                continue
            elif i[1] == ':':
                s_temp += '：'
                continue
            if i[1] == '(':
                s_temp += '（'
                continue
            elif i[1] == ')':
                s_temp += '）'
                continue
            if i[1] == ';':
                s_temp += '；'
                continue
            # 如果是一个点，这个点后面不是点，说明这是一个独立的点而不是省略号识别出来的点
            if i[1] == '.' and s[i[0] + 1] != '.':
                # 判断这个点是句号还是真的点(可能是文件名的后缀的点或序号的点，也可能是句号)
                s_temp += My_Tool.suffix_dot_judge(s[i[0] - 1:])
            # 反之，是一个省略号
            elif i[1] == '.' and s[i[0] + 1] != '.':
                s_temp += '……'
            else:
                s_temp += i[1]
        return s_temp


# GUI图形窗口类
class PySimpleGUI_Tool(object):
    def __init__(self, title_name_lis, windows_name='小工具', button_name='OK', default_value_lis=None,
                 file_suffix=['1'],
                 keep_on_top=False, title_size=25, in_size=10, suffix_in_size=5, folder_browse_size=5):
        self.windows_name = windows_name
        self.title_name_lis = title_name_lis
        self.default_value_lis = default_value_lis
        self.button_name = button_name
        self.keep_on_top = keep_on_top
        self.title_size = title_size
        self.in_size = in_size
        self.suffix_in_size = suffix_in_size
        self.folder_browse_size = folder_browse_size
        self.count = 0
        # 可能的后缀
        self.file_suffix = file_suffix
        # 设置定义布局的列表
        self.layout = []
        self.choice_num_list = []

    def __Layout_selection(self, title_name=None, default_value=None):
        '''
        私有方法，为公有方法return_parameter_by_window提供个性化窗口设置
        :param title_name: 当前循环下（即对当前行的设置），当前行的title_name标题
        :param default_value: 当前循环下，该行的窗口模块的默认值
        :return: 该行以列表封装的一个sg对象
        '''
        # 如果没写默认值，则和else情况处理一致
        if default_value == None:
            return [sg.Text(title_name, size=(self.title_size, 1)), sg.In('', size=(self.in_size, 1))]
        # 是字符串情况
        elif isinstance(default_value, str):
            # 如果default_value是文件夹，则该行加入一个“浏览”选项
            if path.isdir(default_value):
                return [sg.Text(f'{title_name}', size=(self.title_size, 1)), sg.In(default_value, size=(25, 1)),
                        sg.FolderBrowse('浏览', size=(self.folder_browse_size, 1))]
            # 第一个if已经筛除c:\\users\\..这种情况，所以要是还有”:“说明是一个选择行
            elif ':' in default_value:  # 因为default_value输入的是类似：3:2这样的，其中3就是该行选项的个数，2就是默认选择第二个选项
                # 确定冒号的下标
                colon_index = default_value.find(':')
                # 确定该行有多少个选项
                num = default_value[:colon_index]
                # 把该行的选项数添加到choice_num_list，一轮过后，这个列表就是按顺序存着为选项行的选项数
                self.choice_num_list.append(int(num))
                # 确定选择的选项（选择的选项也就是选项的位置，因为选项是从1开始的）
                choice = default_value[colon_index + 1:]
                # 该行第一个模块是title_name，先写进列表
                target_list = [sg.Text(f'{title_name}', size=(self.title_size, 1))]
                # 设置Radio所属群组（只有在同一组的单选按钮才有排他性）
                Radio_group = title_name + 'Radio1'
                # 从1开始遍历，这样可以和选项位置一一对应，范围：range(该行选项数)
                for n in range(1, int(num) + 1):
                    # 若遍历的当前位置和选择的选项位置相同，则执行default=True，使得默认选中该选项
                    if str(n) == choice:
                        target_list.append(sg.Radio(str(n), Radio_group, default=True))
                    else:
                        target_list.append(sg.Radio(str(n), Radio_group))
                return target_list
            # 疑似文件名
            elif '.' in default_value:
                # 如果default_value是一个文件名，则加入一个末尾有下拉选择菜单的模块（选择后缀）
                if default_value[default_value.find('.'):] in self.file_suffix:
                    # 把default_value以.分隔
                    lis = default_value.split('.')
                    default_name = lis[0]
                    default_suffix = '.' + lis[1]
                    return [sg.Text(title_name, size=(self.title_size, 1)), sg.In(default_name, size=(self.suffix_in_size, 1)),
                            sg.Combo(self.file_suffix, default_value=default_suffix, size=(5, 1))]
            # 若还有其他情况则直接用In输入框
            else:
                return [sg.Text(title_name, size=(self.title_size, 1)), sg.In(default_value, size=(self.in_size, 1))]
        # 列表情况（说明这是一个下拉菜单模块）
        elif isinstance(default_value, list):
            return [sg.Text(title_name, size=(self.title_size, 1)), sg.Combo(default_value, default_value=default_value[0], size=(25, 1))]
        # 若还有其他情况则直接用In输入框
        else:
            return [sg.Text(title_name, size=(self.title_size, 1)), sg.In(default_value, size=(self.in_size, 1))]

    def __return_parameter_by_window(self):
        # 此处获取的选择行的value是有冗余的，因为一个sg.Radio模块就返回一个True或False，所以设置一个truly_values列表，方便对原始values字典进行处理
        truly_values = []
        # 定义一个临时列表，处理values字典时使用的
        temp_list = []
        # 备份，因为choice_num_list确定了就不需要改变了，以后的循环都可直接知道选项个数是多少，不需要重新数（要用深拷贝，因为pop和append都默认是浅拷贝，不用深拷贝会跟随改变的）
        temp_choice_num_list = deepcopy(self.choice_num_list)
        # 若values字典不为空，继续循环
        while self.values != {}:
            # 因为每次都是用一个删一个，所以i一直获取values字典的第一个键即可，并不会获取到重复的
            i = list(self.values.keys())[0]
            # 注：values字典排布是{0: 'C:\\Users\\Vh\\Desktop', '浏览': '', 1: '1', 2: '.png', 3: False, 4: True, 5: False, 6: True, 7: False, 8: False, 9: True}
            # 如果这个键不是整型，说明是“浏览”字样模块，不是有用信息，删除该键值对，continue即可
            if not isinstance(i, int):
                self.values.pop(i)
                continue
            # 如果当前键对应的值不是True或False，说明是其他的有用的东西，加入该列表，然后删除values中该键值对
            if not isinstance(self.values[i], bool):
                truly_values.append(self.values[i])
                self.values.pop(i)
            # 如果遍历到当前是True或False，说明这是一行选择模块，应该根据该行有多少个选择模块把这一行的所有True或False都放在一起
            else:
                # 因为temp_choice_num_list元素也是用一个删一个，所以0号元素对应的刚好是当前行选择模块的个数，然后用j遍历
                for j in range(temp_choice_num_list[0]):
                    # values[i + 0]是当前行的第一个选择模块的结果（True或False），那么i+1就是第二个，所以我觉得这里的i+j非常精妙
                    temp_list.append(self.values[i + j])
                    # 用一个删一个，然后这一行的选择模块整完后，到下一行选择模块时i = list(values.keys())[0]才能准确获取到下一行的第一个选择模块
                    self.values.pop(i + j)
                # 把当前行整合后的True、False结果以列表形式加入到truly_values列表
                truly_values.append(temp_list)
                # 重置临时列表temp_list，方便处理下一行选择模块的整合
                temp_list = []
                # 当前行选择模块已经整合完，可删除当前行的“选择模块个数”
                temp_choice_num_list.pop(0)

        return_values = []
        # 处理完后，truly_values列表模样：['C:\\Users\\Vh\\Desktop', '1', '.png', [False, True, False], [True, False], [False, True]]
        # 继续处理truly_values
        for i in truly_values:
            # 判断i是字符串还是列表
            if isinstance(i, str):
                # 如果是地址
                if os.path.isdir(i):
                    return_values.append(i)
                # 如果i是一个后缀，说明上一个append到return_values的是文件名，所以这个后缀需要和上一个连在一起
                elif '.' in i:
                    if i in self.file_suffix:
                        # 记录上一个元素 —— 文件名
                        file_name = return_values[-1]
                        # 删除上一个元素
                        return_values.pop()
                        # 文件名与后缀连接再append到return_values列表中
                        return_values.append(file_name + i)
                else:
                    return_values.append(i)
            # 如果i是列表，说明是一行选择模块
            elif isinstance(i, list):
                # 遍历枚举后的i
                for j in enumerate(i):
                    # 如果当前元素是True说明这行选择模块选择的就是它，由于单选只有一个True的原理，返回它即可退出循环
                    if j[1] == True:
                        # 返回的是枚举列表i的索引加1（假如选的是第二个选项，那么第二个位置枚举的就是1，再加1就是2了
                        return_values.append(str(j[0] + 1))
                        break
            # 其他情况，直接append到return_values列表即可
            else:
                return_values.append(i)

        # 返回最终处理好的参数列表：['C:\\Users\\Vh\\Desktop', '1.png', '2', '1', '2']
        return return_values

    def gui_windows(self):
        # 第一次运行则需新建windows对象
        if self.count == 0:
            self.count = 1
            for num in range(len(self.title_name_lis)):  # 根据title_name_lis的长度设置循环次数，然后调用上面的函数，识别参数特征并个性化添加窗口栏目列表
                if self.default_value_lis == None:
                    self.layout.append(self.__Layout_selection(self.title_name_lis[num]))
                else:
                    self.layout.append(self.__Layout_selection(self.title_name_lis[num], self.default_value_lis[num]))
            # 最后追加一个开始按钮
            self.layout.append(
                [sg.Column([[sg.Button(self.button_name, size=(50, 1))]], expand_x=True,
                           element_justification='center')])
            # 显示窗口
            self.windows = sg.Window(self.windows_name, self.layout, keep_on_top=self.keep_on_top)

        # 获取事件和值字典（如果未触发event，则会卡在这一步，不会往下执行，也即窗口不会关闭，除非触发了event（按了关闭按钮或按了button））
        event, self.values = self.windows.read()
        # 如果是关闭窗口或者None事件，直接退出程序
        if event in (sg.WIN_CLOSED, None):
            sys.exit()
        # 如果是点击button_name按钮事件，开始对values字典参数进行处理
        elif event == self.button_name:
            return self.__return_parameter_by_window()

    @staticmethod
    # 弹出一个框框显示文字
    def popup_scrolled(text, title='Text'):
        sg.popup_scrolled(text, title=title)

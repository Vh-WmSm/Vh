# coding=gbk
import requests
import time
import os


def menu():
    print('*'*10 + '��ӭ����ts�ļ��������ز����ӳ���' + '*'*10, end='\n\n')
    print('��ܰ��ʾ�����д���ǰ��ȷ������������������in.txt��in��\n\n\t����in.txt��ts����������ַ��inΪ���ļ���')
    print("\n\t���ң�in.txt�У�һ��Ϊһ��������ַ�����һ����ַ֮��Ҫ��'\\n'")
    judge = input('\n\tȷ����������y/Y���У�')
    if judge == 'y' or judge == 'Y':
        return
    else:
        print('\n\t�����y/Y���˳�����')
        exit()
    
# �˺��������ҵ���bugʱ��ɾ���ҵ�ts�ļ������Բ����������
# �������ɣ�
# �ٱ�֤inһ��ʼ�ǿ��ļ��м��ɣ�û��Ҫһ��ʼ�����in�ļ��У���һɾ������
# ��Ϊ��ֹ������һ�ַ������ӳ��ִ��󣬹ʽ������Ȳ�ɾ��in�ļ����ڵ�����ts�ļ�
def del_file():
    os.chdir('C:\\users\\vh-ů��\\desktop\\in')
    os.system('@echo y|del *.*')


def ord_9632(i, length):  # ord(9632) == '��'�����Դ���Ϊ��������
    num = round((i / length) * 100)
    return '��' * num


def percent(i, length):
    percent_ = format(round(i / length, 3) * 100, '.1f')
    return str(percent_) + '%'


def ts_download():
    with open('C:\\users\\vh-ů��\\desktop\\in.txt', 'r') as l:
        url_list = l.read().split('\n')  # ��ȡts�ļ����ص�ַ
    length = len(url_list)
    j = 0
    for i in range(length):
        url = url_list[i]
        res = requests.get(url)
        with open('C:\\users\\vh-ů��\\desktop\\in\\{}.ts'.format(i), 'wb') as f:
            f.write(res.content)
        if j - i == 0 or i == length - 1:
            j += 1  # ÿ����1���ļ�����ӡһ�ν���
            print('\n\t���ؽ��ȣ�{}'.format(percent(i + 1, length)))
    print('\n\tts�ļ���ȡ���!')
    return length


class concat:
# ע���˴�self���Զ���__init__����ŵ���������λ�ã��ʲ��ô�name��contact_method����
    def __init__(self): 
        # ���ڿ�������һ�ַ������ӳ�������Ƶ�����⣬���Թ����ַ�����ѡ��
        if contact_method == '1':
            print('\n\t����ʹ�õ�copy��������ts�ļ���')
            self.ts_concat_copy(length, name)
        elif contact_method == '2':
            print('\n\t����ʹ��ffmpeg��������ts�ļ���')
            self.ts_concat_ffmpeg(length, name)
        # ��ѡ��ķ��������⣬��������ͬ�ļ����µġ����ַ�������ts��ѡ����һ�ַ����ٴ�����


    # ffmpeg -i "concat:01.mp4|02.mp4|03.mp4" -c copy out.mp4
    def ts_concat_ffmpeg(self, length, name):
        time.sleep(1)
        s = ''
        for i in range(length - 1):
            s += '{}.ts|'.format(i)
        s += '{}.ts'.format(length - 1)
        order = 'ffmpeg -i "concat:{}" -c copy {}.mp4'.format(s, name)
        os.chdir('C:\\users\\vh-ů��\\desktop\\in')
        os.system(order)
        
    # ����cmd�������ӣ�copy /b *.ts name.mp4
    def ts_concat_copy(self, length, name):
        time.sleep(1)
        str_ = ''
        for i in range(length):
            str_ += "{}.ts+".format(i)
        # ȥ�����һ���Ӻ�
        str1 = str_[:len(str_) - 1]  # ����str1 = '0.ts+1.ts+...+n.ts'
        order = 'copy /b {} {}.mp4'.format(str1, name)
        os.chdir('C:\\users\\vh-ů��\\desktop\\in')
        os.system(order)
        
class move:
    def __init__(self):
        self.move(move_adress, name)
        
    def move(self, move_adress, name):
        os.chdir('C:\\users\\vh-ů��\\desktop\\in')
        order = 'move {}.mp4 {}'.format(name, move_adress)
        os.system(order)
        if move_adress == 'C:\\users\\vh-ů��\\desktop':
            print('\n\t�ϳ��ļ����ƶ������棡')
        else:
            print('\n\t�ϳ��ļ����ƶ���ָ��λ��')


if __name__ == '__main__':
    menu()
    name = input('\n\t����������ļ���������д��׺����')
    contact_method = input('\n\t���²������ַ������ӣ�1.copy��2.ffmpeg��������������\n\t��ѡ��')
    key = 0
    if contact_method == '1' or contact_method == '2':
        key = 1
    if key == 1:
        judge = input('\n\t������ɺ���ļ��ƶ���ʲôλ�ã�1.ָ��λ�á�������desktop��')
        if judge == '1':
            move_adress = input('\n\t������Ŀ��λ�ã�')
        else:
            move_adress = 'C:\\users\\vh-ů��\\desktop'
    length = ts_download()
    if key == 1:
        # ����concat_����������concat���Զ�����__init__()
        concat_ = concat()
        # ����move_��������move���Զ�����__init__()
        move_ = move()
    print('\n\tȫ����ɣ�')

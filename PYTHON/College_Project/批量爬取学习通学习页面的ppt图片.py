import os
import time
import requests


# ���˵�
def menu():
    print('*' * 10 + '����ӭ����ѧϰͨ�������pptͼƬ��ȡ���� 4.0�汾(2022.6.3)��' + '*' * 10)
    print('������ʹ�÷�����')
    print('����ȷ����������ַ���磺C:\\Users\\Vh\\Desktop')
    print('��ȷ�������������һ����Ҫ�����õ�url.txt�ı��ĵ�')
    print('Tips:�����ַȷ���������ı��ĵ����������ڴ����ע����', end='\n\n')
    '''ע��
        �������ַȷ��������ȷ��δѡ�������κ��ļ�������£�������հ״���סshift�ٵ������Ҽ��������˵��е��
        "��PowerShell"��Ȼ���������ַ(���ơ�C����p������>���ź�ǰ��Ŀո�Ҫ����)���ɣ�win11���Ȱ�����ʾ����ѡ���
        ��url.txt�����������������Ҽ��½�һ���ı��ĵ���������Ϊurl����׺���ñ䣩��Ȼ������ҳ�ϴ�ѧϰͨ�������ӦPPT��
            �����һ��ͼƬ�ϣ��Ҽ���꣬�������ͼ�����ӣ�Ȼ��ճ����url.txt�ļ���س�������������ճ����Ҫ��PPT��ַ'''

    '''������ʷ��1.0�汾���ɵ�������ppt�����ֶ�����ѭ��������ͼƬ��ַ
                 2.0�汾���������������ع���
                 3.0�汾���������Զ������ļ��й��ܡ���������֤�빦�ܡ�������turtle���Ӧ��
                 4.0�汾���޸������ֶ�����url.txt��url�����ı׶ˣ�������Զ���ȡ'''
    judge = input('�����ײ�����׼������������y/Y��ʼ�ɣ�\n\n' + '�����룺')
    if judge == 'y' or judge == 'Y':
        return
    else:
        print('\n' + '�ǵ���׼���ú����������Ұɣ�')
        exit()


# �����ȡ������Ϣ�ĺ���(�б�˳��洢�������ַ��ѭ������(url����)��url�б�)
def get_info():
    info_lis = []
    address = input('\n' + '��������������ַ��')
    info_lis.append(address)
    with open(address + '\\url.txt', 'r') as f:
        urls = f.read().strip('\n').split('\n')  # strip��ȥ��url�ַ�������һЩ���ܴ��ڵĿ��У�split���Ի��з�����ʽ�ָ���url���б���
    number = len(urls)
    info_lis.append(number)
    info_lis.append(urls)
    return info_lis


# �����½��ļ��еĺ���
def create_folder(number):
    folder_name = [str(i) for i in range(1, number + 1)]  # ���á��б�����������ļ��б���б�  ֪ʶ���鱾 P98
    for name in folder_name:
        try:
            os.makedirs(name)  # �������������ļ��У��������Ѿ����ڸ����ֵ��ļ��У���ܿ�����������������
        except:
            continue


# ������ո��ļ���ԭ���ļ��ĺ���
def del_file(i, address):
    local = '{}\\{}'.format(address, i)
    os.chdir(local)
    os.system('@echo y|del *.*')  # @echo y��˼���Զ�����y����ʾ��ȷ��ɾ����


def download_picture(urls, address, number):
    for i in range(1, number + 1):
        del_file(i, address)  # ��ɾ�������ļ��������������������µģ���Ϊ�п��ܸ��ļ��д�����һ����ȡ�����ݣ�
        url = urls[i - 1]  # ��ȡ��ǰѭ����url
        start = int(url.rfind('/')) + 1  # ��ȡҳ�������λ�±�
        end = int(url.rfind('.'))  # ��ȡҳ�������λ����һλ���±�
        nums = int(url[start:end])  # ��ȡ��ҳ��
        url = url[:start] + '{}' + url[end:]  # ��xxxxx/nums.png����xxxxx/{}.png
        for num in range(1, nums + 1):
            res = requests.get(url.format(num))  # ����requests���get������ȡ���ص�ַ��Ӧ
            with open("{}\\{}\\{}.png".format(address, i, num), 'wb') as picture:
                picture.write(res.content)  # ����Ӧ�л�ȡͼƬ���ݣ���д����Ӧ��.png�ļ���
        print("��ɵ�{}��ppt����ȡ��".format(i))


def end(t0, t1):
    print('\n������ȡ����ʱ�䣺{}s\n��ӭ�´�ʹ�ñ������ټ���'.format(round(t1 - t0, 3)), end='')  # round(, 3)�������룬����3λС��
    input('\n\n���������������')




if __name__ == '__main__':
    menu()  # ��ʾ�˵�
    info_lis = get_info()  # ��ȡ������Ϣ
    address = info_lis[0]  # �õ�python������λ�ã���url.txt����λ��
    os.chdir(address)  # �趨python������Ϊ���棬�����Ǵ�py�ļ�����λ��
    number = info_lis[1]  # �õ�ѭ������
    create_folder(number)  # �Զ������洴���ļ��в�����Ϊ1��2��3����
    urls = info_lis[2]  # ��ȡurl�б�
    t0 = time.time()  # �����������ͳ����ȡ������ʱ��
    download_picture(urls, address, number)  # ��ʼ��ȡ��urls�б��±��Ǵ�0��ʼ����i��1��ʼ������Ҫ��1��
    t1 = time.time()
    end(t0, t1)  # ��ӡ����ʱ�䣬������

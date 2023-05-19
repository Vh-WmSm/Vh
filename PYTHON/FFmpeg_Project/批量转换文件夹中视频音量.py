# coding=gbk
import os
import time


def menu():
    folder_name = []
    print('----------����ת���ļ�������Ƶ����----------')
    print('Tips����ת��������15���ӵ���Ƶת�������30�롣������ת������̫�󣬻ᵼ��ʧ�档')
    desktop_file = os.listdir('C:\\users\\vh\\desktop')
    while True:
        folder_name.append(input('�������ļ������ƣ����ļ��з������棬�Ҵ����Ҫת������Ƶ����'))
        folder_name.append(input('����������ļ������ƣ�'))
        if folder_name[0] in desktop_file and folder_name[1] in desktop_file:
            return folder_name
        else:
            print('�ļ��в��������ϣ����������룡')


def transform(lis, path_in, path_out):
    while True:
        print('��ʲô��ʽת����1��������2���ֱ���3���������')
        judge_volume = input('������1/2/3��')
        if judge_volume == '1':
            volume = input('������ת��Ϊԭ�ļ��Ķ��ٱ���������3��0.3��')
            key = 1
            break
        elif judge_volume == '2':
            volume = input('����������/���ٶ��ٷֱ���������10��-10��')
            volume += 'dB'
            key = 1
            break
        elif judge_volume == '3':
            key = 0
            break
        else:
            print('���������������룡')
    # judge_del = input('ת����ɺ��Ƿ�ɾ��ԭ�ļ���y/n��')
    t0 = time.time()
    os.chdir(path_in)
    i = 1
    if key == 1:
        for li in lis:
            order = 'ffmpeg -i {} -filter:a "volume = {}" -vcodec copy o_{}'.format(li, volume, li)
            i += 1
            os.system(order)
            move(path_out, 'o_{}'.format(li))
    else:
        for li in lis:
            order = 'ffmpeg -i {} -an -vcodec copy o_{}'.format(li, li)
            i += 1
            os.system(order)
            move(path_out, 'o_{}'.format(li))
    # return judge_del
    return t0


# def del_original(lis):
#     print('����ɾ��ԭ�ļ�����')
#     time.sleep(1.5)
#     for li in lis:
#         os.system("@echo y|del {}".format(li))
#     print('�Ѿ�ɾ��ԭ�ļ���')
#     time.sleep(0.5)

def move(path_out, name):
    os.system('move {} {}'.format(name, path_out))

if __name__ == '__main__':
    folder_name = menu()
    path_in = 'C:\\users\\vh\\desktop\\{}'.format(folder_name[0])
    path_out = 'C:\\users\\vh\\desktop\\{}'.format(folder_name[1])
    lis = os.listdir(path_in)
    t0 = transform(lis, path_in, path_out)
    # if judge_del == 'y' or judge_del == 'Y':
    # del_original(lis)
    print('ȫ����ɣ�')
    time.sleep(0.5)
    t1 = time.time()
    print("�˴�ת������ʱ�䣺" + str(t1 - t0))

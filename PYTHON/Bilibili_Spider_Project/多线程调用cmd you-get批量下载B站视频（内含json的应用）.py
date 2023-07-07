import os
import sys
import threading
import requests
import PySimpleGUI as sg
import public_tools


def url_txt_creator(desktop_path, judge):
    if judge == '1':
        url = input('输入其中一个url（例如：https://www.bilibili.com/video/BV1aT411T7nr?p=1）（一定要包含“?p=”）：')
        url_same = url.split('?')[0]
        episode_selete = input('要下载第几集到第几集？（空格分隔）：')
        start = int(episode_selete.split()[0])
        end = int(episode_selete.split()[1])
        f = open(desktop_path + '\\url.txt', 'a', encoding='gb18030')
        for i in range(start, end + 1):
            f.write(url_same + f'?p={i}\n')
        f.close()
        return url
    else:
        print('下面则通过一个弹窗帮助你生成url.txt，请找到BV号所在的json文件……')

        page_num = ''
        url_ = ''
        mid = ''
        season_id = ''
        sort_reverse = ''
        page_size = ''
        spm_id_from = ''
        layout = [
            [sg.Text('{:<21}'.format('该合集有多少页？：')), sg.In()],
            [sg.Text('{:<21}'.format('url头：')), sg.In()],
            [sg.Text('{:<15}'.format('mid:')), sg.Input()],
            [sg.Text('{:<28}'.format('season_id:')), sg.In()],
            [sg.Text('{:<28}'.format('sort_reverse:')), sg.In()],
            [sg.Text('{:<17}'.format('page_size:')), sg.In()],
            [sg.Text('{:<32}'.format('spm_id_from（这个是点进视频，看网址的部分，一般来说一个合集的spm_id_from都一样）:')), sg.In()],
            [sg.Button('确认参数')]  # 设置“开始裁剪”按钮
        ]
        windows = sg.Window('B站视频下载引导', layout, keep_on_top=True)  # 显示窗口
        while True:  # 设置窗口循环
            event, values = windows.read()  # 设置变量作为窗口显示内容
            if event == None:  # 设置关闭窗口事件
                break
            if event == '确认参数':  # 设置点击“开始裁剪”按钮事件
                # 设置返回内容
                page_num = int(values[0])
                url_ = values[1]
                mid = values[2]
                season_id = values[3]
                sort_reverse = values[4]
                page_size = values[5]
                spm_id_from = values[6]
                windows.close()

                # url_ = 'https://api.bilibili.com/x/polymer/space/seasons_archives_list'
                # url = 'https://api.bilibili.com/x/polymer/space/seasons_archives_list?mid=384234870&season_id=295885&sort_reverse=false&page_num=1&page_size=30'
        for i in range(1, page_num + 1):
            params = {
                'mid': mid,
                'season_id': season_id,
                'sort_reverse': sort_reverse,
                'page_num': f'{i}',
                'page_size': page_size
            }
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                                     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
                                     '/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}  # 由于B站对爬虫不限制，以所也可以不用headers
            res = requests.get(url_, params=params, headers=headers)
            lis = res.json()['data']['archives']
            f = open(desktop_path + '\\url.txt', 'a', encoding='gb18030')
            for li in lis:
                f.write('https://www.bilibili.com/video/' + li['bvid'] + f'/?spm_id_from={spm_id_from}' + '\n')
            f.close()

        print('请先检查url.txt网址是否正确（主要检查spm_id_from有没有哪个视频不是当前编号的，如果有，则删除或更改再继续运行程序！）')
        judge_check = input('检查好了吗？（直接回车默认好了）')
        if judge_check == '':
            return


def switch_case(Format_judge):
    Formats = {
        '1': '360',
        '2': '480',
        '3': '720',
        '4': '1080',
    }
    return Formats.get(Format_judge, None)


def download():
    global lock, re_key, f_r, download_path, judge_F, Format
    

    lock.acquire()

    url = f_r.readline()
    if url == '':
        re_key = 0
        lock.release()  # 若某子线程发现获取的url是空的，说明已经爬取结束了，为全局变量re_key赋值0，然后解开线程锁，让当前主线程下剩下的子线程继续获取“空”后返回，等消耗完剩下子线程后即可
        return

    lock.release()
    if judge_F == '1':
        order = f'you-get -F dash-flv{Format} {url}'
        with open('c:\\users\\vh\\desktop\\1.txt', 'w', encoding='gb18030') as f:
            f.write(order)
    else:
        order = f'you-get {url}'
    os.chdir(download_path)
    os.system(order)
def Video_clarity():
    global judge_F, Format
    judge_F = input('对清晰度有要求吗？（直接回车默认没有）有则按1：')
    if judge_F == '1':
        judge_F_f = input('是否查看这个playlist的视频清晰度都有哪几个？（直接回车则不查看）：')
        if judge_F_f != '':
            order_test = f'start cmd /K you-get -i {url}'  # 用命令start cmd /K 让os.system结束后cmd窗口不会自动关闭
            print(order_test)
            os.system(order_test)
        Format_judge = input('现在请选择一个清晰度输入：1.360、2.480、3.720、4.1080：')
        Format = switch_case(Format_judge)

def Set_the_thread():
    global f_r, lock, re_key
    thread_num = int(input('每次调用多少个cmd下载子线程？：'))

    f_r = open(desktop_path + '\\url.txt', 'r', encoding='gb18030')
    lock = threading.Lock()
    re_key = 1

    while re_key == 1:
        threads = [threading.Thread(target=download) for _ in range(thread_num)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()  # 设置线程等待，等该轮主线程结束后才进行下一轮，否则所有cmd将全部弹出
if __name__ == '__main__':
    judge_F = Format = ''
    desktop_path = public_tools.My_Tool.get_desktop_path()
    download_path = input('下载到：')
    os.chdir(desktop_path)
    judge1 = input('是否已经有url.txt且待下载视频链接都在内了？1.是。2.否：')
    if judge1 == '1':
        Video_clarity()
        Set_the_thread()
        sys.exit()
    if 'url.txt' in os.listdir(desktop_path):
        os.system('del url.txt')
    judge2 = input('有共同的url吗？（是不是一个playlist？）：1.有。2.没有：')
    if judge2 == '1':
        url = url_txt_creator(desktop_path, judge2)
    elif judge2 == '2':
        ju = input('是否通过引导自动生成url.txt？（注意，只适用于在一个合集里，但并不是一个playlist）（若不是合集，请自己制作url.txt）（直接回车默认进行引导）：')
        if ju == '':
            url_txt_creator(desktop_path, judge2)
        with open(desktop_path + '\\url.txt', 'r', encoding='gb18030') as f_:
            url = f_.readline()  # 取url.txt中第一个作为样本，为下面可能查看视频有哪些清晰度做准备
            # （但有个缺点就是可能其他视频清晰度又有不同，所以如果是url.txt中不是一个playlist建议用默认清晰度下载就好了，不要自定义清晰度）
    else:
        print('输入有误，退出程序……')
        sys.exit()

    Video_clarity()
    Set_the_thread()

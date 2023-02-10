import os
import wget
import requests


def res_download(url, ts_path):
    url_index = url.find('?')
    url_ = url[:url_index]
    name_index = url.rfind('/')
    name = url_[name_index + 1:]

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'}
    res = requests.get(url, headers=headers)
    with open('{}\\{}'.format(ts_path, name), 'wb') as f:
        f.write(res.content)


def wget_download(url, ts_path, temp_path, count, key):
    if key == '1':
        wget.download(url, temp_path)
        os.chdir(temp_path)
        lis = os.listdir()
        os.rename(''.join(lis), str(count) + '.ts')
        os.system('move *.ts {}'.format(ts_path))
    else:
        wget.download(url, ts_path)

def ts_concat_ffmpeg(start, end, name):
    s = ''
    for i in range(start, end - 1):
        s += '{}.ts|'.format(i)
    s += '{}.ts'.format(end - 1)
    order = 'ffmpeg -i "concat:{}" -c copy "{}.mp4"'.format(s, name)
    os.system(order)


if __name__ == '__main__':
    desktop_path = 'c:\\users\\vh\\desktop'
    os.chdir(desktop_path)
    try:
        os.mkdir('temp_path')
    except:
        pass
    try:
        os.mkdir('ts_path')
    except:
        pass
    temp_path = 'c:\\users\\vh\\desktop\\temp_path'
    ts_path = 'c:\\users\\vh\\desktop\\ts_path'

    head = input('请求标头：')
    url_txt_path = input('url.txt文件地址（直接回车默认在桌面）：')
    if url_txt_path == '':
        url_txt_path = desktop_path
    judge = input('使用哪种方法下载：1.requests。2.wget：')  # 如果猫抓抓到的ts文件复制它的链接在浏览器中打开后不能正常播放这一片段，说明requests下载失效，需用wget下载
    connect = input('下载完成后是否连接为mp4文件？（直接回车默认连接）：')
    if connect == '':
        name = input('连接后的文件名（不加后缀，默认.mp4）：')
    key = input('是否需要重命名ts文件名为n.ts、n+1.ts……（直接空格默认不需要）需要则输入1：')
    if key == '1':
        n = int(input('确定n.ts的初始n值：'))
    os.chdir(url_txt_path)

    count = n - 1
    with open('url.txt', 'r', encoding='gb18030') as f:
        while True:
            count += 1
            text = f.readline()
            while '#' in text:
                text = f.readline()
            if text == '':
                break
            url = '{}{}'.format(head, text)
            print('正在下载：' + url, end='')
            if judge == '1':
                res_download(url, ts_path)
            elif judge == '2':
                wget_download(url, ts_path, temp_path, count, key)
                print('下载成功', end='\n\n')
    if connect == '':
        os.chdir(ts_path)
        print('爬取结束！\n\n下面开始连接……\n')
        lis = os.listdir()
        lis.sort(key=lambda x: int(x[:-3]))
        start = int(lis[0].split('.')[0])
        end = int(lis[-1].split('.')[0])
        ts_concat_ffmpeg(start, end, name)

        os.system('move "{}.mp4", {}'.format(name, desktop_path))
        os.system('del *.ts')


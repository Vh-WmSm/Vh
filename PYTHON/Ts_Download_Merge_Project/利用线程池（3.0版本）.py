# 3.0版本使用了线程池，大大提高了下载效率，带宽可跑满，而2.0版本最多才2M/s

import os
import wget
import chardet
import concurrent.futures


def wget_download(url, file_name):
    wget.download(url, ts_path + '\\' + file_name)
    return f'{file_name}已下载'


def check_encoding(url_txt_path):
    with open(url_txt_path, 'rb') as f:
        content = f.read()
        return chardet.detect(content)['encoding']


if __name__ == '__main__':
    desktop_path = 'c:\\users\\vh\\desktop'
    os.chdir(desktop_path)
    try:
        os.mkdir('ts_path')
    except:
        jud_del = input('ts_path文件夹已存在，其中可能存在内容，是否删除（直接回车默认删除）？')
        if jud_del == '':
            os.chdir('ts_path')
            os.system('echo y |del *.*')
    ts_path = 'c:\\users\\vh\\desktop\\ts_path'
    os.chdir(desktop_path)

    url_txt_path = input('url.txt文件地址（直接回车默认在桌面）：')
    if url_txt_path == '':
        url_txt_path = desktop_path + '\\url.txt'

    with open(url_txt_path, 'r', encoding=check_encoding(url_txt_path)) as f_r:
        url_list = f_r.read().strip().splitlines()
    with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
        future_results = [executor.submit(wget_download, url, f'{count}.ts') for count, url in
                          enumerate(url_list)]  # 枚举函数，为每个url都对应一个相应的索引，这样就可以代替队列按顺序下载
        for f in concurrent.futures.as_completed(future_results):
            print(f.result())  # 打印的是wget_download的return值

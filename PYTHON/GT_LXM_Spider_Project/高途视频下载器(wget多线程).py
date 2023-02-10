import os
import wget
import threading
import time


def fun():
    global lock, f, desktop_path, key, name_list, download_path
    lock.acquire()
    info = f.readline()
    if info == '':
        key = 0
        lock.release()
        return
    url, new_name = info.split(' ', 1)
    new_name = new_name.strip()
    old_name_index = url.rfind('/')
    old_name = url[old_name_index + 1:]
    name_list.append([old_name, new_name + '.mp4'])
    lock.release()

    wget.download(url, download_path)


if __name__ == '__main__':
    desktop_path = 'c:\\users\\vh\\desktop'
    os.chdir(desktop_path)
    download_path = input('下载到（直接回车默认下载到desktop下的rec文件夹）：')
    if download_path == '':
        download_path = desktop_path + '\\rec'
    key = 1
    name_list = []
    f = open('url.txt', 'r', encoding='utf-8')
    while key != 0:
        threads = [threading.Thread(target=fun) for i in range(10)]
        lock = threading.Lock()
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    os.chdir(download_path)
    for i in name_list:
        os.rename(i[0], i[1])

import os
import wget
import threading


def fun():
    global head, lock, f, re_key, count, name_list  # 全局变量，相当于C++中的引用

    lock.acquire()  # 调用线程锁，使每个子线程排着队按顺序获取url.txt中的每行url
    count += 1

    text = f.readline().strip()
    while '#' in text:
        text = f.readline()
    if text == '':
        re_key = 0  # 若某子线程发现获取的url是空的，说明已经爬取结束了，为全局变量re_key赋值0，然后解开线程锁，让当前主线程下剩下的子线程继续获取“空”后返回，等消耗完剩下子线程后即可
        lock.release()  # 这里解开线程锁是因为再往后读取都肯定是''了，所以解开，让剩下的子线程全部一拥而上可以快速消耗剩下子线程
        return
    url = f'{head}{text}'
    file_name = count
    print('正在下载：' + url)
    lock.release()

    print(f'当前子线程：{threading.current_thread().name}')
    wget.download(url, ts_path + '\\' + f'{file_name}.ts')



def ts_concat_ffmpeg(start, end, name):
    s = ''
    for i in range(start, end):
        s += '{}.ts|'.format(i)
    s += '{}.ts'.format(end)
    order = 'ffmpeg -i "concat:{}" -c copy "{}.mp4"'.format(s, name)
    os.system(order)


if __name__ == '__main__':
    desktop_path = 'c:\\users\\vh\\desktop'
    os.chdir(desktop_path)
    mk_key = 0
    try:
        os.mkdir('ts_path')
        mk_key = 1
    except:
        pass
    ts_path = 'c:\\users\\vh\\desktop\\ts_path'
    os.chdir(ts_path)
    if mk_key == 0:
        os.system('del *.*')  # 初始化ts_path文件夹
    os.chdir(desktop_path)

    head = input('请求标头(没有则直接回车)：')  # 请求标头示例：https://dtliving-sz.dingtalk.com/live_hp/ Tips:若ts流下载地址只有后半部分，而没有这个“标头”的部分，则需写这个。
    url_txt_path = input('url.txt文件地址（直接回车默认在桌面）：')
    if url_txt_path == '':
        url_txt_path = desktop_path

    count = 0  # 数数下载到第几个ts文件
    name_list = []
    name = ''
    connect = input('下载完成后是否连接为mp4文件？（直接回车默认连接）：')
    if connect == '':
        name = input('连接后的文件名（不加后缀，默认.mp4）：')
    thread_num = int(input('每次调用子线程数：'))

    f = open(f'{url_txt_path}\\url.txt', 'r', encoding='gb18030')
    lock = threading.Lock()
    re_key = 1
    while re_key == 1:
        threads = [threading.Thread(target=fun) for _ in range(thread_num)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        print('当前主线程结束，尝试进入下一线程……')

    f.close()
    print('re_key返回值为0，爬取结束！\n\n')
    
    if connect == '':
        os.chdir(ts_path)
        print('下面开始连接所有ts文件……\n')

        ts_concat_ffmpeg(1, len(os.listdir()), name)

        os.system('move "{}.mp4", {}'.format(name, desktop_path))
        print(f'爬取成功，"{name}.mp4"文件已移动到桌面！')

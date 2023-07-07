import os
# import sys
# from you_get import common
import concurrent.futures
import public_tools


def you_get_download(url, count, target_path):
    # common.any_download(url=f'{url}{count}', info_only=False, output_dir=target_path, merge=True)
    os.system(f'you-get {url}{count}')
if __name__ == '__main__':
    title_name_lis = ['Target_Path:', 'URL:', 'Start:', 'End:']
    windows_name = 'BILIBILI线程池下载小工具'
    button_name = '开始下载'
    default_value_lis = [public_tools.My_Tool.get_desktop_path(), '', '', '']
    gui = public_tools.PySimpleGUI_Tool(title_name_lis, windows_name, button_name, default_value_lis, title_size=10,
                                        in_size=60)
    target_path, url, start, end = gui.gui_windows()
    os.chdir(target_path)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        tasks = [executor.submit(you_get_download, url, count, target_path) for count in range(int(start), int(end) + 1)]
        # for task in tasks:
            # task.result()

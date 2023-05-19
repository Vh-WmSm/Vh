from public_tools import PySimpleGUI_Tool, My_Tool
from ffmpeg import video

desktop_path = My_Tool.get_desktop_path()

title_size = 10
in_size = 25
suffix_in_size = 25
folder_browse_size = 6
file_suffix = ['.mp4', '.flv', '.avi']
default_value_lis = [desktop_path, '.mp4', '', '', '.mp4', desktop_path]
# 创建窗口对象
w = PySimpleGUI_Tool(['视频地址', '输入文件名', '开始时间', '结束时间', '输出文件名', '输出位置'], windows_name='视频裁剪器', button_name='开始裁剪',
                     file_suffix=file_suffix, default_value_lis=default_value_lis, title_size=title_size, in_size=in_size,
                     suffix_in_size=suffix_in_size, folder_browse_size=folder_browse_size)
while True:
    # 获取窗口返回值并解包
    re_data = w.gui_windows()
    video_path, in_name, start_time, end_time, out_name, out_path = re_data
    start_time = ':'.join(start_time.split())
    end_time = ':'.join(end_time.split())
    # 裁剪视频
    video.v_intercept_time(video_path + '\\' + in_name, start_time, end_time, out_path + '\\' + out_name)

import os

location = input('输入视频所在文件夹路径：')
os.chdir(location)
name_in = input('视频的名字(不加后缀，默认mp4，下同)：')
name_out = input('输出视频的名字：')
order = 'ffmpeg -i {}.mp4 -filter_complex "[0:v]setpts=0.5*PTS[v];[0:a]atempo=2.0[a]" -map "[v]" -map "[a]" {}.mp4'.format(name_in, name_out)
os.system(order)

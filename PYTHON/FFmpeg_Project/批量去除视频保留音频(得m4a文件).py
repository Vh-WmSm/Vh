import os

address = input('地址：')
os.chdir(address)
lis = os.listdir()
order = []
for li in lis:
    if '.mp4' in li:
        name = li.split('.mp4')[0]
        order.append('ffmpeg -i "{}" -vn -acodec copy "{}"'.format(li, name+'.m4a'))
order_ = '&&'.join(order)
os.system(order_)

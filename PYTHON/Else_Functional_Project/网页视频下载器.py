import requests
import wget

while True:
    judge = input('采用哪种方式下载？1.requests。2.wget：')
    desktop_path = 'c:\\users\\vh\\desktop'
    path = input('地址(直接回车默认下载到桌面)：')
    url = input('url:')
    if judge == '1':
        if path == '':
            path = desktop_path
        res = requests.get(url)
        with open(f'{path}\\视频.mp4', 'wb') as f:
            f.write(res.content)

    else:
        wget.download(url, path)
    jud = input('继续下载则直接回车')
    if jud == '':
        break
    


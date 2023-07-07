import os

path = r'D:\software\Redis'
os.chdir(path)
os.system('redis-server.exe redis.windows.conf')

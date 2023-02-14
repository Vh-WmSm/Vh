import os

# ts文件超过1000可用此.py工具分批连接ts文件
path = input('ts文件地址：')
os.chdir(path)
ts_list = os.listdir()
ts_list.sort(key=lambda x:int(x[:x.rfind('.')]))
start = int(ts_list[0].split('.')[0])
end = int(ts_list[-1].split('.')[0])
name = input('输出文件名（不带后缀）：')
s = ''
count = 0
for i in range(start, end + 1):
    s += f'{i}.ts|'
    if i % 1000 == 0:
        count += 1
        order = 'ffmpeg -i "concat:{}" -c copy "a{}.mp4"'.format(s, count)
        os.system(order)
        s = ''
    if i == end:
        count += 1
        order = 'ffmpeg -i "concat:{}" -c copy "a{}.mp4"'.format(s, count)
        os.system(order)
        
file = [f'a{i}' for i in range(1, count + 1)]

li = open('list.txt', 'w')
for fi in file:
    li.write('file ' + "'" + '{}'.format(fi) + '.mp4' + "'\n")
li.close()
order = 'ffmpeg -f concat -i list.txt -c copy {}.mp4'.format(name)
os.system(order)
os.system('@echo y|del list.txt')

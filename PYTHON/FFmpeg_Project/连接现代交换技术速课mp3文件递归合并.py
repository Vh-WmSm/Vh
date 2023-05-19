import os


def fun(address1, address2, address_out):
    key = 0
    concat = 'ffmpeg -i "concat:'
    os.chdir(address2)
    lis = os.listdir()

    for li in lis:
        if os.path.isdir(li) and key == 0:
            now_address = os.getcwd()
            next_address = now_address + '\\{}'.format(li)
            last_address = now_address
            fun(last_address, next_address, address_out)
        elif os.path.isfile(li) or key == 1:
            if '.mp3' in li:
                lis.sort(key=lambda x: int(x[:-4]))
                key = 1
                concat += li + '|'
    if key == 1:
        out_name_index = address2.rfind('\\')
        out_name = address2[out_name_index + 1:]
        if out_name.isdigit():
            out_name_index = address2[:out_name_index].rfind('\\')
            out_name = address2[out_name_index + 1:]
            out_name = ' '.join(out_name.split('\\'))
        order = concat + '"' + ' -acodec copy "{}.mp3" && move "{}.mp3" {}'.format(out_name, out_name, address_out)
        print('正在执行命令——{}'.format(order))
        os.system(order)
    os.chdir(address1)


address_in = input('输入地址：')
address_out = input('输出地址：')
fun(address_in, address_in, address_out)

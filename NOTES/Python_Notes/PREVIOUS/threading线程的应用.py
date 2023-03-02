from threading import Thread, current_thread
import time

def tes():
    print(f'子线程开始，名字：{current_thread().name}')
    time.sleep(2)
    print(f'子线程结束，名字：{current_thread().name}')

print('主线程开始')
threads = [Thread(target=tes) for _ in range(3)]  # 其中_为占位符，相当于i
for __ in threads:  # 这里测试了一下两个_是否可以是占位符，看来是可以的， 这说明了所谓“占位符”其实就是一个变量罢了
    __.start()
for __ in threads:
    __.join()
print('主线程结束')

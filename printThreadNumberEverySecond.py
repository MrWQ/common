import threading,time

#         每秒打印线程数目
def pringThreadNumberEverySecond():
    while(threading.activeCount()>1):
        print(str(threading.activeCount()) + 'actived thread')
        time.sleep(1)


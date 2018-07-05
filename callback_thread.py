
#!/usr/bin/env python3

import time
import _thread

import urllib
import urllib.request

import threading


class myThread(threading.Thread):
    def __init__(self):
        thread.Thread.__init__(self)

    def run():
        pass
'''

thread.start()
thread.join()
thread.isAlive()
thread.getName()
thread.setName()



'''


''' _thread apandon '''
def callback_thread(function, args):
    try:
        _thread.start_new_thread(function, args)
    except Exception as e:
        print(e)

def print_time(thread_name, delay):
    count = 0
    while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s"%(thread_name, time.ctime(time.time())))

def crap_web(url, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        html = urllib.request.urlopen(url)
        print('%s'%url)
        print('html: ', html.read())

urls_ = ['http://www.baidu.com', 'http://www.8xyxy.com']
times_ = [1, 2]
#callback_thread(crap_web, ('http://www.baidu.com', 1))
#callback_thread(crap_web, ('http://www.8xyxy.com', 2))









while True:
    time.sleep(1)
    pass

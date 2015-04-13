from threading import Thread
import time
import sys
 
class Thread2(object):
    def __call__(self, left, right):
        for i in range(12):
            time.sleep(1)
            print "%s%d%s " % (left,i,right),
            sys.stdout.flush()
 
t2 = Thread(target=Thread2(), args=('[',']'))
t2.start()        # start thread
t = Thread2()
t('<','>')        # main thread
## Using Thread subclass

from threading import Thread
import time
import sys
 
def thread1(left, right):
    for i in range(12):
        time.sleep(1)
        print "%s%d%s " % (left,i,right),
        sys.stdout.flush()
 
class thread3(Thread):
    def __init__(self, args):
      Thread.__init__(self)
      self.args = args
 
    def run(self):
      for i in range(12):
          time.sleep(1)
          print "%s%d%s " % (self.args[0],i,self.args[1]),
          sys.stdout.flush()
 
t3 = thread3(args=('{','}'))
t3.start()           # start thread

t4 = thread3(args=('(',')'))
t4.start()           # start thread

thread1('<','>')     # main thread
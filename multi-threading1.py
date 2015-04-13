from threading import Thread
import time
import sys

def thread1(left, right):
	for i in range(12):
		time.sleep(1)
		print "%s%d%s" % (left,i,right)
		sys.stdout.flush()


t1 = Thread(target=thread1, args=('[',']'))
t1.start()
thread1('<','>')